# frozen_string_literal: true

module Jekyll
  # Generates /categorias/{slug}/ and /categorias/{cat_slug}/{sub_slug}/ pages
  # from _data/categories.yml, replacing the previously committed
  # categorias/**/*.md stub files (see
  # docs/adr/0001-stub-files-for-category-tag-feed-pages.md and
  # docs/adr/0004-category-pages-generated-from-data-file.md).
  #
  # Top-level Category pages carry a `pagination` block (consumed by
  # jekyll-paginate-v2); Subcategory pages deliberately do not — the
  # `category` layout filters subcategory posts via plain Liquid, not the
  # paginator (see the comment in _layouts/category.html).
  class CategoryPageGenerator < Generator
    safe true
    priority :high

    def generate(site)
      categories = site.data['categories'] || []

      categories.each do |cat|
        cat_name = cat['name']
        cat_slug = cat['slug']
        next if cat_name.nil? || cat_slug.nil?

        site.pages << category_page(site, cat_name, cat_slug, cat['redirect_from'])

        (cat['subcategories'] || []).each do |sub|
          sub_name = sub['name']
          sub_slug = sub['slug']
          next if sub_name.nil? || sub_slug.nil?

          site.pages << subcategory_page(site, cat_name, cat_slug, sub_name, sub_slug, sub['redirect_from'])
        end
      end
    end

    private

    def category_page(site, name, slug, redirect_from)
      page = PageWithoutAFile.new(site, site.source, File.join('categorias', slug), 'index.html')
      page.content = ''
      page.data.merge!(
        'layout' => 'category',
        'category' => name,
        'permalink' => "/categorias/#{slug}/",
        # offset: 0 overrides the site-wide pagination.offset (set to 1 in
        # _config.yml only so the homepage can show the newest post as its
        # standalone "Destaque" card). Category pages have no such card, so
        # inheriting offset: 1 would silently drop each category's newest post.
        'pagination' => { 'enabled' => true, 'category' => name, 'offset' => 0 }
      )
      page.data['redirect_from'] = redirect_from if redirect_from
      page
    end

    def subcategory_page(site, cat_name, cat_slug, sub_name, sub_slug, redirect_from)
      page = PageWithoutAFile.new(site, site.source, File.join('categorias', cat_slug, sub_slug), 'index.html')
      page.content = ''
      page.data.merge!(
        'layout' => 'category',
        'category' => cat_name,
        'subcategory' => sub_name,
        'permalink' => "/categorias/#{cat_slug}/#{sub_slug}/"
      )
      page.data['redirect_from'] = redirect_from if redirect_from
      page
    end
  end
end
