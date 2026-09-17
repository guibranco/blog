# frozen_string_literal: true

module Jekyll
  # Liquid filters for money and rates in a Post language, used by the static
  # tables of _includes/calculators/*.html (ADR-0015). Liquid has no number
  # formatting of its own; without these the tables would show "44000".
  #
  #   {{ 44000   | money: "EUR", "pt-BR" }}  → "€ 44.000"
  #   {{ 8475.55 | money: "BRL", "en" }}     → "R$ 8,475.55"
  #   {{ 0.005   | percent: "pt-BR" }}       → "0,5%"
  #
  # Whole amounts print without decimals; anything else prints two. pt-BR
  # separators are "." and ","; every other language gets "," and ".".
  module MoneyFilters
    SYMBOLS = { 'EUR' => '€', 'BRL' => 'R$' }.freeze

    def money(input, currency = 'EUR', lang = 'pt-BR')
      value = input.to_f
      decimals = (value % 1).zero? ? 0 : 2
      int, frac = format("%.#{decimals}f", value.abs).split('.')
      thousands, decimal = pt?(lang) ? ['.', ','] : [',', '.']
      int = int.reverse.scan(/\d{1,3}/).join(thousands).reverse
      number = frac ? "#{int}#{decimal}#{frac}" : int
      sign = value.negative? ? '−' : ''
      "#{sign}#{SYMBOLS.fetch(currency.to_s, currency)} #{number}"
    end

    def percent(input, lang = 'pt-BR')
      value = (input.to_f * 100).round(4)
      str = value == value.to_i ? value.to_i.to_s : value.to_s
      str = str.tr('.', ',') if pt?(lang)
      "#{str}%"
    end

    private

    def pt?(lang)
      lang.to_s.start_with?('pt')
    end
  end
end

Liquid::Template.register_filter(Jekyll::MoneyFilters)
