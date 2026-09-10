# frozen_string_literal: true

require 'open3'
require 'set'
require 'time'

module Jekyll
  # Stamps `last_modified_at` on posts and pages with the date of the last git
  # commit that changed the BODY (everything after the front matter). Consumed
  # by jekyll-sitemap (<lastmod>), jekyll-seo-tag (dateModified) and
  # _includes/post-dates.html.
  #
  # A commit does NOT count as an update when:
  #   * it only touched front matter (tags, reading_time, lang, ...)
  #   * it only changed whitespace / line endings in the body
  #   * it only renamed/moved the file (history is followed across renames)
  #   * it created the file (a WordPress import is publication, not an update)
  #   * its message contains `[skip lastmod]`
  #   * its SHA is listed in `.lastmod-ignore-revs` (retroactive skip, same
  #     format as .git-blame-ignore-revs: one SHA per line, `#` comments)
  #
  # An explicit `last_modified_at:` in front matter always wins.
  # Needs full history in CI (`fetch-depth: 0`).
  class GitLastModified < Generator
    safe false
    priority :low

    FRONT_MATTER = if defined?(Jekyll::Document::YAML_FRONT_MATTER_REGEXP)
                     Jekyll::Document::YAML_FRONT_MATTER_REGEXP
                   else
                     %r!\A(---\s*\n.*?\n?)^((---|\.\.\.)\s*$\n?)!m
                   end
    SKIP_MARKER = '[skip lastmod]'
    IGNORE_FILE = '.lastmod-ignore-revs'

    # Survives `jekyll serve` rebuilds; invalidated when HEAD or the ignore file changes.
    @cache = {}
    class << self
      attr_reader :cache
    end

    def generate(site)
      @source = site.source
      return unless git_repo?

      cache_key = [git('rev-parse', 'HEAD').strip, ignore_file_stamp]
      self.class.cache.clear unless self.class.cache[:key] == cache_key
      self.class.cache[:key] = cache_key
      @ignored = load_ignored_revs

      with_cat_file do
        (site.posts.docs + site.pages).each { |item| stamp(item) }
      end
    end

    private

    def stamp(item)
      return if item.data.key?('last_modified_at') # manual override wins

      relative = relative_path(item)
      return unless relative

      changed = self.class.cache.fetch(relative) do
        self.class.cache[relative] = last_content_change(relative)
      end
      return unless changed

      # Edits made before publication (drafts, scheduled posts) aren't updates.
      published = item.data['date']
      changed = published if published.respond_to?(:to_time) && changed < published.to_time
      item.data['last_modified_at'] = changed
    end

    def relative_path(item)
      path = item.respond_to?(:path) ? item.path : nil
      return nil unless path

      full = File.expand_path(path, @source)
      return nil unless File.file?(full) && full.start_with?(@source)

      full.delete_prefix("#{@source}/")
    end

    # One `git log` per file: SHA, committer date, subject+body, and the path
    # the file had in that commit (so renames resolve to the right blob).
    def last_content_change(relative)
      revisions = parse_log(git('log', '--follow', '--name-only',
                                '--format=%x1e%H%x1f%cI%x1f%B%x1f', '--', relative))
      return nil if revisions.empty?

      revisions.each_with_index do |rev, i|
        older = revisions[i + 1]
        return nil if older.nil? # only the creation commit: never updated
        next if skipped?(rev)

        return rev[:date] if body(rev) != body(older)
      end
      nil
    rescue StandardError => e
      Jekyll.logger.warn 'GitLastModified:', "#{relative}: #{e.message}"
      nil
    end

    def parse_log(output)
      output.split("\x1e").filter_map do |record|
        sha, date, message, files = record.split("\x1f", 4)
        next if sha.to_s.strip.empty?

        path = files.to_s.lines.map(&:strip).reject(&:empty?).last
        next unless path

        { sha: sha.strip, date: Time.iso8601(date.strip), message: message.to_s, path: path }
      end
    end

    def skipped?(rev)
      rev[:message].include?(SKIP_MARKER) ||
        @ignored.any? { |prefix| rev[:sha].start_with?(prefix) }
    end

    def body(rev)
      @bodies ||= {}
      @bodies.fetch(rev[:sha] + rev[:path]) do
        content = read_blob("#{rev[:sha]}:#{rev[:path]}").to_s.dup.force_encoding(Encoding::UTF_8)
        text = content.sub(FRONT_MATTER, '')
        @bodies[rev[:sha] + rev[:path]] = normalize(text)
      end
    end

    # Whitespace-only edits (trailing spaces, CRLF, blank lines at the edges)
    # are not content changes.
    def normalize(text)
      text.gsub("\r\n", "\n").lines.map(&:rstrip).join("\n").strip
    end

    # A single long-lived `git cat-file --batch` instead of one `git show`
    # process per revision.
    def with_cat_file
      Open3.popen2('git', 'cat-file', '--batch', chdir: @source) do |stdin, stdout, _thread|
        @cat_in = stdin
        @cat_out = stdout
        yield
      ensure
        stdin.close unless stdin.closed?
      end
    end

    def read_blob(spec)
      @cat_in.puts(spec)
      @cat_in.flush
      header = @cat_out.gets.to_s
      return nil if header.end_with?("missing\n") || header.split.size < 3

      size = header.split[2].to_i
      data = @cat_out.read(size)
      @cat_out.read(1) # trailing newline
      data
    end

    def load_ignored_revs
      file = File.join(@source, IGNORE_FILE)
      return Set.new unless File.file?(file)

      File.readlines(file).map { |l| l.sub(/#.*/, '').strip.downcase }.reject(&:empty?).to_set
    end

    def ignore_file_stamp
      file = File.join(@source, IGNORE_FILE)
      File.file?(file) ? File.mtime(file).to_i : 0
    end

    def git_repo?
      !git('rev-parse', '--is-inside-work-tree').strip.empty?
    end

    def git(*args)
      out, status = Open3.capture2('git', *args, chdir: @source)
      status.success? ? out : ''
    end
  end
end
