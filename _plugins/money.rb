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
  # Whole amounts print without decimals; anything else prints two — or pass a
  # fixed number of decimals as the third argument (`money: "EUR", _lang, 2`)
  # for a column where amounts must line up. pt-BR separators are "." and
  # ","; every other language gets "," and ".".
  module MoneyFilters
    SYMBOLS = { 'EUR' => '€', 'BRL' => 'R$', 'GBP' => '£', 'USD' => 'US$', 'ALL' => 'Lek' }.freeze

    def money(input, currency = 'EUR', lang = 'pt-BR', decimals = nil)
      value = input.to_f
      decimals = (value % 1).zero? ? 0 : 2 if decimals.nil?
      decimals = decimals.to_i
      int, frac = format("%.#{decimals}f", value.abs).split('.')
      thousands, decimal = pt?(lang) ? ['.', ','] : [',', '.']
      int = int.reverse.scan(/\d{1,3}/).join(thousands).reverse
      number = frac ? "#{int}#{decimal}#{frac}" : int
      sign = value.negative? ? '−' : ''
      "#{sign}#{SYMBOLS.fetch(currency.to_s, currency)} #{number}"
    end

    # {{ 0.248123 | percent: "en", 1 }} → "24.8%"; without the second argument
    # the value is rounded to four decimals and trailing zeros are dropped.
    def percent(input, lang = 'pt-BR', decimals = nil)
      value = (input.to_f * 100).round(decimals.nil? ? 4 : decimals.to_i)
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
