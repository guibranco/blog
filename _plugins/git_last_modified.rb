# frozen_string_literal: true

require 'open3'
require 'pathname'

module Jekyll
  # Stamps `last_modified_at` on every post and page with the timestamp of
  # that file's last git commit. Jekyll's own file mtimes are meaningless in
  # a fresh CI checkout (everything lands with the same checkout time), so
  # git history is the only reliable source for "last updated" — both for
  # the post layout's updated-on date and for jekyll-sitemap's <lastmod>,
  # which already reads `last_modified_at` when present (falls back to
  # `date` for posts, omits <lastmod> entirely for pages otherwise).
  class GitLastModified < Generator
    safe false
    priority :low

    def generate(site)
      cache = {}

      (site.posts.docs + site.pages).each do |item|
        path = item.respond_to?(:path) ? item.path : nil
        next unless path

        item.data['last_modified_at'] = cache.fetch(path) { cache[path] = last_commit_time(site.source, path) }
      end
    end

    private

    def last_commit_time(source, path)
      full_path = File.expand_path(path, source)
      return nil unless File.exist?(full_path)

      relative = Pathname.new(full_path).relative_path_from(Pathname.new(source)).to_s
      out, status = Open3.capture2('git', 'log', '-1', '--format=%cI', '--', relative, chdir: source)
      return nil unless status.success?

      date = out.strip
      date.empty? ? nil : Time.iso8601(date)
    rescue StandardError
      nil
    end
  end
end
