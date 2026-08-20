# frozen_string_literal: true

module Jekyll
  # Generates /feed/{slug}.xml and /feed/{cat_slug}-{sub_slug}.xml RSS feeds
  # from _data/categories.yml, replacing the previously committed feed/*.xml
  # stub files — the last piece of the pattern documented in
  # docs/adr/0001-stub-files-for-category-tag-feed-pages.md (see
  # docs/adr/0003 and docs/adr/0004 for the tag/category pages that moved
  # off it first).
  #
  # The RSS body itself still contains Liquid ({% assign %}/{% for %}) —
  # Jekyll renders Liquid in generator-created page content exactly as it
  # does for a file loaded from disk, so this is a straight port of the
  # templates from .github/scripts/create_missing_pages.py's
  # feed_template()/subcategory_feed_template().
  class FeedGenerator < Generator
    safe true
    priority :high

    def generate(site)
      categories = site.data['categories'] || []

      categories.each do |cat|
        cat_name = cat['name']
        cat_slug = cat['slug']
        next if cat_name.nil? || cat_slug.nil?

        site.pages << category_feed(site, cat_name, cat_slug)

        (cat['subcategories'] || []).each do |sub|
          sub_name = sub['name']
          sub_slug = sub['slug']
          next if sub_name.nil? || sub_slug.nil?

          site.pages << subcategory_feed(site, cat_name, cat_slug, sub_name, sub_slug)
        end
      end
    end

    private

    def xml_escape(text)
      text.to_s.gsub('&', '&amp;').gsub('<', '&lt;').gsub('>', '&gt;')
    end

    def item_block
      <<~LIQUID
        <item>
          <title>{{ post.title | xml_escape }}</title>
          <link>{{ post.url | absolute_url }}</link>
          <guid isPermaLink="true">{{ post.url | absolute_url }}</guid>
          <pubDate>{{ post.date | date_to_rfc822 }}</pubDate>
          <description>{{ post.description | xml_escape }}</description>
        </item>
      LIQUID
    end

    def category_feed(site, name, slug)
      page = PageWithoutAFile.new(site, site.source, 'feed', "#{slug}.xml")
      safe = xml_escape(name)
      page.content = <<~XML
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
          <channel>
            <title>{{ site.title | xml_escape }} — #{safe}</title>
            <description>Artigos sobre #{safe} em {{ site.title | xml_escape }}</description>
            <link>{{ site.url }}{{ site.baseurl }}/categorias/#{slug}/</link>
            <atom:link href="{{ site.url }}{{ site.baseurl }}/feed/#{slug}.xml" rel="self" type="application/rss+xml"/>
            <language>pt-BR</language>
            {% assign _cat_posts = site.posts | where_exp: "p", "p.categories contains '#{name}'" | limit: 20 %}
            {% for post in _cat_posts %}
            #{item_block}{% endfor %}
          </channel>
        </rss>
      XML
      page.data.merge!('layout' => nil, 'permalink' => "/feed/#{slug}.xml")
      page
    end

    def subcategory_feed(site, cat_name, cat_slug, sub_name, sub_slug)
      feed_slug = "#{cat_slug}-#{sub_slug}"
      page = PageWithoutAFile.new(site, site.source, 'feed', "#{feed_slug}.xml")
      safe_cat = xml_escape(cat_name)
      safe_sub = xml_escape(sub_name)
      filter_cond = "p.subcategories contains '#{cat_name}/#{sub_name}'"
      page.content = <<~XML
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
          <channel>
            <title>{{ site.title | xml_escape }} — #{safe_cat} › #{safe_sub}</title>
            <description>Artigos sobre #{safe_sub} em {{ site.title | xml_escape }}</description>
            <link>{{ site.url }}{{ site.baseurl }}/categorias/#{cat_slug}/#{sub_slug}/</link>
            <atom:link href="{{ site.url }}{{ site.baseurl }}/feed/#{feed_slug}.xml" rel="self" type="application/rss+xml"/>
            <language>pt-BR</language>
            {% assign _sub_posts = site.posts | where_exp: "p", "#{filter_cond}" | limit: 20 %}
            {% for post in _sub_posts %}
            #{item_block}{% endfor %}
          </channel>
        </rss>
      XML
      page.data.merge!('layout' => nil, 'permalink' => "/feed/#{feed_slug}.xml")
      page
    end
  end
end
