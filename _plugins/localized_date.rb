# frozen_string_literal: true

require 'time'

module Jekyll
  # `%B` in Ruby's strftime always renders the *system* locale's month name
  # — on most CI runners that's English regardless of the format string
  # being "%d de %B de %Y". Rather than depend on the build environment
  # having a pt-BR locale installed, this filter substitutes the month name
  # from a fixed table before handing the format to strftime, so pt-BR
  # dates render correctly no matter where the site is built.
  module LocalizedDateFilter
    MONTH_NAMES = {
      'pt-BR' => %w[janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro],
      'en' => %w[January February March April May June July August September October November December]
    }.freeze

    def localized_date(date, format, lang = nil)
      return '' if date.nil? || format.nil?

      time = date.respond_to?(:strftime) ? date : Time.parse(date.to_s)
      months = MONTH_NAMES[lang.to_s] || MONTH_NAMES['pt-BR']
      patched_format = format.gsub('%B', months[time.month - 1])
      time.strftime(patched_format)
    rescue StandardError
      ''
    end
  end
end

Liquid::Template.register_filter(Jekyll::LocalizedDateFilter)
