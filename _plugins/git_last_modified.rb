# frozen_string_literal: true

require 'open3'
require 'pathname'

module Jekyll
  # Stamps `last_modified_at` on every post and page with the date of the
  # last git commit that changed its BODY — the content after the closing
  # `---` of the front matter. A commit that only touches front matter
  # (tags, reading_time, categories, adding `lang:`, ...) doesn't count as
  # an update a reader would care about, so it's walked past.
  #
  # This means, for each file, walking its whole commit history and diffing
  # the body at each revision against the body at the previous one — more
  # `git show` calls than a plain `git log -1`, but still cheap at this
  # blog's scale (a few dozen posts, a handful of revisions each).
  #
  # Jekyll's own file mtimes are meaningless in a fresh CI checkout
  # (everything lands with the same checkout time), so git history is the
  # only reliable source here — both for the post layout's updated-on date
  # and for jekyll-sitemap's <lastmod>, which already reads
  # `last_modified_at` when present (falls back to `date` for posts, omits
  # <lastmod> entirely for pages otherwise).
  class GitLastModified < Generator
    safe false
    priority :low

    def generate(site)
      cache = {}

      (site.posts.docs + site.pages).each do |item|
        path = item.respond_to?(:path) ? item.path : nil
        next unless path

        item.data['last_modified_at'] = cache.fetch(path) { cache[path] = last_content_change(site.source, path) }
      end
    end

    private

    # Walks the file's revisions newest -> oldest and returns the date of
    # the first one whose body differs from the revision right before it
    # (i.e. the most recent commit that actually changed the content).
    def last_content_change(source, path)
      full_path = File.expand_path(path, source)
      return nil unless File.exist?(full_path)

      relative = Pathname.new(full_path).relative_path_from(Pathname.new(source)).to_s
      revisions = git(source, 'log', '--follow', '--format=%H', '--', relative).lines.map(&:strip)
      return nil if revisions.empty?

      body_cache = {}
      body_at = ->(rev) { body_cache.fetch(rev) { body_cache[rev] = extract_body(git(source, 'show', "#{rev}:#{relative}")) } }

      revisions.each_with_index do |rev, i|
        older_rev = revisions[i + 1]
        return commit_date(source, rev) if older_rev.nil? || body_at.call(rev) != body_at.call(older_rev)
      end

      nil
    rescue StandardError
      nil
    end

    # Front matter is the YAML between the first two `---` lines; everything
    # after the second one is the body readers actually see.
    def extract_body(content)
      parts = content.split(/^---\s*$/m)
      parts.length >= 3 ? parts[2..].join('---') : content
    end

    def commit_date(source, rev)
      date = git(source, 'log', '-1', '--format=%cI', rev).strip
      date.empty? ? nil : Time.iso8601(date)
    end

    def git(source, *args)
      out, status = Open3.capture2('git', *args, chdir: source)
      status.success? ? out : ''
    end
  end
end
