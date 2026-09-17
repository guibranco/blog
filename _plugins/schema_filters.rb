# frozen_string_literal: true

require 'cgi'
require 'json'

module Jekyll
  # Liquid filters used by _includes/schema.html to build the page's JSON-LD.
  module SchemaFilters
    # ── faq_items ──────────────────────────────────────────────────────────
    #
    # Question/Answer pairs from a post's *rendered* HTML, for the FAQPage
    # node. A post opts in with `faq: true` in its front matter.
    #
    # A question is any <h2>/<h3>/<h4> whose text ends with "?" — kramdown
    # headings and the raw <h2> inside the section-header component both
    # count. Its answer is everything between that heading and the next
    # heading of the same or a higher level, as plain text: tags are
    # stripped, entities decoded, whitespace collapsed, and code blocks,
    # tables, figures, scripts, styles and inline SVG are dropped (they don't
    # read as an answer), and so are the section-header component's number
    # and the "· · ·" divider, which sit between one section's text and the
    # next heading. A heading that is not a question produces no entry of
    # its own, so a post can mix ordinary sections with Q&A ones; a
    # lower-level heading nested under a question (an <h3> under an <h2>)
    # does not end that answer, so its content stays in the parent's answer.
    # A question with nothing but dropped blocks after it is skipped.
    #
    # Google's FAQPage guidelines require every listed question and answer to
    # be visible on the page, which is why the pairs come from the body and
    # not from a hand-written list in the front matter.
    HEADING        = %r{<h([2-4])\b[^>]*>(.*?)</h\1\s*>}mi
    DROPPED_BLOCKS = %r{<(pre|table|figure|script|style|svg)\b[^>]*>.*?</\1\s*>}mi
    DECORATION     = %r{<div class="(?:divider|section-num)"[^>]*>.*?</div>}mi
    HTML_COMMENT   = /<!--.*?-->/m
    HTML_TAG       = %r{</?[A-Za-z][^>]*>}m

    def faq_items(html)
      text = html.to_s
      headings = text.to_enum(:scan, HEADING).map { Regexp.last_match }

      headings.each_with_index.filter_map do |heading, i|
        level = heading[1].to_i
        question = plain_text(heading[2])
        next unless question.end_with?('?')

        stop = headings[(i + 1)..].find { |h| h[1].to_i <= level }
        answer_html = text[heading.end(0)...(stop ? stop.begin(0) : text.length)]
        answer = plain_text(answer_html.gsub(DROPPED_BLOCKS, ' ').gsub(DECORATION, ' '))
        next if answer.empty?

        { 'question' => question, 'answer' => answer }
      end
    end

    # ── json_ld_string ─────────────────────────────────────────────────────
    #
    # A free-text value as a JSON string literal for use inside an inline
    # `<script type="application/ld+json">`: `"` and `\` escaped, and `</`
    # written as `<\/` so no title, description or answer can ever close the
    # <script> early. Use this instead of `escape` (which HTML-escapes — an
    # `&` would come out as the literal text `&amp;` inside a <script>, where
    # entities are not decoded) and instead of `jsonify` for anything that
    # may contain user-written text.
    def json_ld_string(input)
      input.to_s.to_json.gsub('</', '<\/')
    end

    private

    def plain_text(html)
      CGI.unescapeHTML(html.gsub(HTML_COMMENT, ' ').gsub(HTML_TAG, ' ').gsub('&nbsp;', ' '))
         .gsub(/[[:space:]]+/, ' ')
         .strip
    end
  end
end

Liquid::Template.register_filter(Jekyll::SchemaFilters)
