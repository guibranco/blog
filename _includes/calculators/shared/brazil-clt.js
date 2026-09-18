  // ── Brazil CLT payslip, shared by the Calculators that read shared/brazil-clt.yml (ADR-0017); needs lib.js ──
  function inss(gross, br) { return progressive(Math.min(gross, br.inss.ceiling), br.inss.bands); }
  // IRRF on one month's gross: base is the gross less the larger of the legal deductions (the INSS
  // actually withheld plus dependants) or the simplified discount, then the Lei 15.270 reduction.
  function irrf(gross, inssPaid, dependents, br) {
    var legal = inssPaid + dependents * br.irrf.dependent_deduction;
    var base = Math.max(0, gross - Math.max(legal, br.irrf.simplified_discount));
    var tax = bracket(base, br.irrf.bands);
    var r = br.irrf.reduction, reduction = 0;
    if (gross <= r.full_up_to) reduction = tax;
    else if (gross <= r.partial_up_to) reduction = Math.min(tax, Math.max(0, r.constant - r.factor * gross));
    return { base: base, taxBefore: tax, reduction: reduction, tax: tax - reduction };
  }
  // One CLT payslip.
  function payslip(gross, dependents, br) {
    var i = inss(gross, br), t = irrf(gross, i, dependents, br);
    return { gross: gross, inss: i, irrf: t.tax, irrfBefore: t.taxBefore, reduction: t.reduction, net: gross - i - t.tax };
  }
