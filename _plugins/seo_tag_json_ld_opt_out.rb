# frozen_string_literal: true

require 'jekyll-seo-tag'

module Jekyll
  # Adds a `json_ld=false` flag to jekyll-seo-tag's `{% seo %}`, alongside the
  # gem's own `title=false` and `canonical=false`:
  #
  #   {% seo json_ld=false %}
  #
  # renders every meta tag the gem normally renders (og:*, twitter:*,
  # canonical, article:published_time, ...) but not its
  # `<script type="application/ld+json">`.
  #
  # The post layout uses it. _includes/schema.html emits the post's structured
  # data as one @graph (Article, BreadcrumbList, ItemList, FAQPage, ...), and
  # the BlogPosting node the gem adds to every dated page would describe the
  # same article a second time under a different @type — exactly the duplicate
  # the Rich Results Test and the Schema Markup Validator flag. Pages that do
  # not pass the flag (home, category, tag, series, ...) keep the gem's JSON-LD.
  # See docs/adr/0014-post-json-ld-graph-replaces-seo-tag-node.md.
  module SeoTagJsonLdOptOut
    JSON_LD_SCRIPT = %r{<script type="application/ld\+json">.*?</script>\n?}m

    # Prepended to Jekyll::SeoTag's singleton class. The gem has no hook
    # around its <script>, so the block is wrapped in the flag when the
    # template text is read, before Liquid parses it. The build fails loudly
    # if a gem upgrade changes the template and the block is no longer found:
    # silently emitting two article nodes again is the regression this plugin
    # exists to prevent.
    module TemplateContents
      private

      def template_contents
        @template_contents_with_json_ld_flag ||= begin
          contents = super
          unless contents.match?(JSON_LD_SCRIPT)
            raise Jekyll::Errors::FatalException,
                  'seo_tag_json_ld_opt_out: the jekyll-seo-tag template no longer contains the ' \
                  'JSON-LD <script> this plugin wraps — update JSON_LD_SCRIPT or drop the plugin'
          end

          contents.sub(JSON_LD_SCRIPT) { |script| "{% if seo_tag.json_ld? %}#{script}{% endif %}" }
        end
      end
    end

    # Included in Jekyll::SeoTag::Drop. Mirrors the gem's #title? / #canonical?:
    # the opt-out is a flag in the tag's own text.
    module DropFlag
      def json_ld?
        return @json_ld_enabled if defined?(@json_ld_enabled)

        @json_ld_enabled = (@text !~ /json_ld=false/i)
      end
    end
  end
end

Jekyll::SeoTag.singleton_class.prepend(Jekyll::SeoTagJsonLdOptOut::TemplateContents)
Jekyll::SeoTag::Drop.include(Jekyll::SeoTagJsonLdOptOut::DropFlag)
