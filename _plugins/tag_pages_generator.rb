# frozen_string_literal: true

module Jekyll
  # Generates one /topicos/{slug}/ page per entry in _data/tags.yml, with
  # layout `tag` and `page.tag` set to the entry's display name.
  #
  # Replaces the previously committed topicos/*.md stub files (see
  # docs/adr/0001-stub-files-for-category-tag-feed-pages.md) — _data/tags.yml
  # is the single source of truth for which tag pages exist, kept in sync by
  # .github/scripts/create_missing_pages.py.
  class TagPageGenerator < Generator
    safe true
    priority :high

    def generate(site)
      tags = site.data['tags'] || []

      tags.each do |entry|
        name = entry['name']
        slug = entry['slug']
        next if name.nil? || slug.nil?

        page = PageWithoutAFile.new(site, site.source, File.join('topicos', slug), 'index.html')
        page.content = ''
        page.data.merge!(
          'layout' => 'tag',
          'tag' => name,
          'permalink' => "/topicos/#{slug}/"
        )
        page.data['redirect_from'] = entry['redirect_from'] if entry['redirect_from']

        site.pages << page
      end
    end
  end
end
