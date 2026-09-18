# frozen_string_literal: true

module Jekyll
  # Fills `reading_time` (whole minutes) on every post that does not set it in
  # front matter, from the word count of the post's body. A manual
  # `reading_time:` in front matter always wins — it is an override, not a
  # requirement (see docs/adr/0013-reading-time-computed-from-body.md).
  #
  # The estimate is made on the *source* body (Markdown + inline HTML) rather
  # than the rendered HTML because a Generator runs before anything is
  # rendered, so the value is already there when listings, the search index
  # and the post page read `post.reading_time`. Counting:
  #
  #   * fenced code blocks (``` / ~~~) and <pre> blocks are counted separately,
  #     at a slower rate — readers scan code, they do not read it as prose;
  #   * HTML tags, comments, <script>/<style>, Liquid tags/objects and entities
  #     are markup, not words;
  #   * Markdown link/image syntax keeps its text and drops the URL;
  #   * every image (Markdown, <img>, or a photo.html include) adds a fixed
  #     number of seconds, so a Gallery-heavy Trip is not a two-minute read.
  #
  # Rates are overridable in _config.yml:
  #
  #   reading_time:
  #     words_per_minute: 200        # prose (pt-BR runs a little slower than en)
  #     code_words_per_minute: 150   # words inside code blocks
  #     seconds_per_image: 10
  #
  # The defaults were calibrated against the hand-authored values the posts
  # carried before this plugin existed (median ratio 1.0 across 60 posts).
  #
  # .github/scripts/reading_time.py is a line-for-line port used by
  # audit_blog.py (drift check) and build_og_cards.py (card label) — keep the
  # two in sync when changing anything below.
  module ReadingTime
    extend self

    DEFAULTS = {
      'words_per_minute' => 200,
      'code_words_per_minute' => 150,
      'seconds_per_image' => 10
    }.freeze

    FENCED_CODE   = /^[ \t]{0,3}((`|~)\2{2,})(?!\2)[^\n]*\n.*?^[ \t]{0,3}\1\2*[ \t]*$\n?/m
    PRE_BLOCK     = %r{<pre\b[^>]*>.*?</pre\s*>}mi
    HTML_COMMENT  = /<!--.*?-->/m
    SCRIPT_STYLE  = %r{<(script|style)\b[^>]*>.*?</\1\s*>}mi
    LIQUID_TAG    = /\{%.*?%\}/m
    LIQUID_OBJECT = /\{\{.*?\}\}/m
    HTML_TAG      = /<\/?[A-Za-z][^>]*>/m
    HTML_ENTITY   = /&(?:#\d+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]*);/
    MD_IMAGE      = /!\[([^\]]*)\]\([^)]*\)/
    MD_LINK       = /\[([^\]]*)\]\([^)]*\)/
    MD_LINK_DEF   = /^[ \t]{0,3}\[[^\]]+\]:[ \t]*\S.*$/
    WORD          = /[[:alnum:]]+(?:['’\-][[:alnum:]]+)*/

    IMAGE_MARKERS = [
      /!\[[^\]]*\]\([^)]*\)/,                 # ![alt](src)
      /<img\b/i,                              # <img …>
      /\{%-?\s*include\s+photo\.html\b/       # {% include photo.html … %}
    ].freeze

    # Word counts of a post body: { 'prose' => n, 'code' => n, 'images' => n }.
    def count(body)
      text = body.to_s.gsub("\r\n", "\n").unicode_normalize(:nfc)

      images = IMAGE_MARKERS.sum { |re| text.scan(re).size }

      code = 0
      text = text.gsub(FENCED_CODE) { |block| code += words(block.lines[1..-2].to_a.join); ' ' }
      text = text.gsub(PRE_BLOCK)   { |block| code += words(strip_markup(block)); ' ' }

      { 'prose' => words(strip_markup(text)), 'code' => code, 'images' => images }
    end

    # Estimated reading time in whole minutes (never below 1).
    def estimate(body, config = nil)
      config = validated_config(config)
      counts = count(body)
      minutes = counts['prose'].to_f / config['words_per_minute'] +
                counts['code'].to_f / config['code_words_per_minute'] +
                counts['images'] * config['seconds_per_image'] / 60.0
      [minutes.ceil, 1].max
    end

    def validated_config(config = nil)
      unless config.nil? || config.is_a?(Hash)
        raise Errors::FatalException, 'Invalid reading_time configuration: expected a mapping'
      end

      merged = DEFAULTS.merge((config || {}).transform_keys(&:to_s))
      {
        'words_per_minute' => 'a positive number',
        'code_words_per_minute' => 'a positive number',
        'seconds_per_image' => 'a non-negative number'
      }.each do |key, requirement|
        value = merged[key]
        valid = value.is_a?(Numeric) && value.real? && value.finite? &&
                (key == 'seconds_per_image' ? value >= 0 : value.positive?)
        next if valid

        raise Errors::FatalException,
              "Invalid reading_time configuration: `reading_time.#{key}` must be #{requirement} (got #{value.inspect})"
      end
      merged
    end

    def words(text)
      text.scan(WORD).size
    end

    def strip_markup(text)
      text.gsub(HTML_COMMENT, ' ')
          .gsub(SCRIPT_STYLE, ' ')
          .gsub(LIQUID_TAG, ' ')
          .gsub(LIQUID_OBJECT, ' ')
          .gsub(MD_LINK_DEF, ' ')
          .gsub(MD_IMAGE, '\1')
          .gsub(MD_LINK, '\1')
          .gsub(HTML_TAG, ' ')
          .gsub(HTML_ENTITY, ' ')
    end
  end

  class ReadingTimeGenerator < Generator
    safe true
    priority :normal

    def generate(site)
      config = ReadingTime.validated_config(site.config['reading_time'])

      site.posts.docs.each do |post|
        next unless post.data['reading_time'].nil? # manual override wins

        post.data['reading_time'] = ReadingTime.estimate(post.content, config)
      end
    end
  end
end
