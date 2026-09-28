/* Mayan Finserv Solutions — shared scripts */
(function () {
  "use strict";
  var SITE = window.SITE || {};
  var WA = SITE.whatsapp || "919985900483";

  /* ---------- helpers ---------- */
  function inr(n) {
    n = Math.round(n);
    var s = String(Math.abs(n));
    var last3 = s.slice(-3), rest = s.slice(0, -3);
    if (rest) last3 = "," + last3;
    rest = rest.replace(/\B(?=(\d{2})+(?!\d))/g, ",");
    return (n < 0 ? "-" : "") + "₹" + rest + last3;
  }
  function inrShort(n) {
    if (n >= 1e7) return "₹" + (n / 1e7).toFixed(n % 1e7 ? 2 : 0) + " Cr";
    if (n >= 1e5) return "₹" + (n / 1e5).toFixed(n % 1e5 ? 2 : 0) + " L";
    return inr(n);
  }
  function emi(P, annualRate, months) {
    var r = annualRate / 12 / 100;
    if (r === 0) return P / months;
    var f = Math.pow(1 + r, months);
    return P * r * f / (f - 1);
  }
  function toast(msg) {
    var t = document.createElement("div");
    t.className = "toast"; t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, 2600);
  }
  function waLink(text) {
    return "https://wa.me/" + WA + "?text=" + encodeURIComponent(text);
  }
  window.MF = { inr: inr, inrShort: inrShort, emi: emi, toast: toast, waLink: waLink };

  /* ---------- nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav a").forEach(function (a) {
    if (a.getAttribute("href") === here) a.classList.add("active");
  });

  /* ---------- WhatsApp forms ----------
     Any <form data-wa="Subject line"> collects its fields into a message
     and opens WhatsApp. Field labels come from data-label or the label text. */
  document.querySelectorAll("form[data-wa]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var lines = ["*" + form.getAttribute("data-wa") + "*", ""];
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === "submit" || el.type === "button") return;
        if (el.type === "checkbox" && !el.checked) return;
        var lab = el.getAttribute("data-label");
        if (!lab) {
          var l = form.querySelector('label[for="' + el.id + '"]');
          lab = l ? l.textContent.replace(/\*$/, "").trim() : el.name;
        }
        var val = el.type === "checkbox" ? "Yes" : el.value.trim();
        if (val) lines.push(lab + ": " + val);
      });
      lines.push("", "Sent from " + (SITE.domain || location.hostname));
      window.open(waLink(lines.join("\n")), "_blank", "noopener");
      toast("Opening WhatsApp…");
    });
  });

  /* ---------- copy buttons ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var txt = b.getAttribute("data-copy");
      if (navigator.clipboard) navigator.clipboard.writeText(txt).then(function () { toast("Copied"); }, function () { toast(txt); });
      else toast(txt);
    });
  });

  /* ---------- EMI calculators ----------
     <div class="emi" data-presets='{"home":{...}}'> with inputs:
     [data-f=amount] [data-f=rate] [data-f=tenure] (years), outputs
     [data-o=emi] [data-o=interest] [data-o=total] [data-o=principal], canvas[data-o=chart],
     optional tbody[data-o=schedule] */
  document.querySelectorAll(".emi").forEach(function (box) {
    var presets = {};
    try { presets = JSON.parse(box.getAttribute("data-presets") || "{}"); } catch (err) {}
    var f = function (k) { return box.querySelector("[data-f=" + k + "]"); };
    var o = function (k) { return box.querySelector("[data-o=" + k + "]"); };
    var amount = f("amount"), rate = f("rate"), tenure = f("tenure");
    var tenureUnit = box.getAttribute("data-tenure") || "years";

    function syncOut(input) {
      var out = box.querySelector('output[for="' + input.id + '"]');
      if (!out) return;
      if (input === amount) out.textContent = inrShort(+input.value);
      else if (input === rate) out.textContent = (+input.value).toFixed(2) + "% p.a.";
      else out.textContent = input.value + (tenureUnit === "years" ? (input.value == 1 ? " year" : " years") : " months");
    }
    function draw(P, I) {
      var c = o("chart"); if (!c) return;
      var ctx = c.getContext("2d"), w = c.width, h = c.height, cx = w / 2, cy = h / 2, R = Math.min(w, h) / 2 - 6;
      ctx.clearRect(0, 0, w, h);
      var total = P + I, a0 = -Math.PI / 2, a1 = a0 + 2 * Math.PI * (P / total);
      function arc(from, to, color) {
        ctx.beginPath(); ctx.arc(cx, cy, R, from, to); ctx.arc(cx, cy, R * 0.62, to, from, true); ctx.closePath();
        ctx.fillStyle = color; ctx.fill();
      }
      arc(a0, a1, "#F2B233"); arc(a1, a0 + 2 * Math.PI, "#7C93E0");
      ctx.fillStyle = "#fff"; ctx.font = "700 14px Manrope, sans-serif"; ctx.textAlign = "center";
      ctx.fillText(Math.round(P / total * 100) + "% principal", cx, cy - 4);
      ctx.fillStyle = "#BFD2E1"; ctx.font = "500 12px Public Sans, sans-serif";
      ctx.fillText(Math.round(I / total * 100) + "% interest", cx, cy + 14);
    }
    function schedule(P, r, n, monthly) {
      var tb = o("schedule"); if (!tb) return;
      var bal = P, rows = [], yr = 1, yp = 0, yi = 0;
      var monthlyRate = r / 12 / 100;
      for (var m = 1; m <= n; m++) {
        var i = bal * monthlyRate, p = monthly - i; bal -= p; yp += p; yi += i;
        if (m % 12 === 0 || m === n) {
          rows.push("<tr><td>Year " + yr + "</td><td>" + inr(yp) + "</td><td>" + inr(yi) + "</td><td>" + inr(Math.max(bal, 0)) + "</td></tr>");
          yr++; yp = 0; yi = 0;
        }
      }
      tb.innerHTML = rows.join("");
    }
    function calc() {
      var P = +amount.value, r = +rate.value, n = tenureUnit === "years" ? +tenure.value * 12 : +tenure.value;
      var m = emi(P, r, n), total = m * n, I = total - P;
      if (o("emi")) o("emi").textContent = inr(m);
      if (o("principal")) o("principal").textContent = inr(P);
      if (o("interest")) o("interest").textContent = inr(I);
      if (o("total")) o("total").textContent = inr(total);
      [amount, rate, tenure].forEach(syncOut);
      draw(P, I); schedule(P, r, n, m);
      var wa = o("wa");
      if (wa) wa.href = waLink("Hi, I checked the EMI calculator on " + (SITE.domain || "your website") + ".\nLoan type: " + (box.getAttribute("data-current") || "Loan") + "\nAmount: " + inr(P) + "\nRate: " + r + "% p.a.\nTenure: " + n + " months\nEMI: " + inr(m) + "\n\nPlease help me apply.");
    }
    // typed inputs mirror the sliders both ways
    var typed = {};
    box.querySelectorAll("input[data-sync]").forEach(function (t) {
      var slider = document.getElementById(t.getAttribute("data-sync"));
      if (!slider) return;
      typed[slider.id] = t;
      t.addEventListener("input", function () {
        var v = parseFloat(t.value);
        if (isNaN(v) || v <= 0) return;
        if (v > +slider.max) slider.max = v;      // typed amount beyond the slider extends it
        if (v < +slider.min) slider.min = v;
        slider.step = "any";                     // keep the exact typed figure, no snapping
        slider.value = v;
        calc(true);
      });
      t.addEventListener("blur", function () { calc(); });
    });
    function pushTyped(skip) {
      if (skip) return;
      [amount, rate, tenure].forEach(function (i) { if (typed[i.id]) typed[i.id].value = i.value; });
    }
    var calcInner = calc;
    calc = function (fromTyped) { calcInner(); pushTyped(fromTyped); };
    [amount, rate, tenure].forEach(function (i) { i.addEventListener("input", function () { calc(); }); });

    // presets (tabs)
    box.querySelectorAll(".tab[data-preset]").forEach(function (t) {
      t.addEventListener("click", function () {
        var p = presets[t.getAttribute("data-preset")]; if (!p) return;
        box.querySelectorAll(".tab").forEach(function (x) { x.classList.remove("active"); });
        t.classList.add("active");
        box.setAttribute("data-current", t.textContent.trim());
        amount.min = p.min; amount.max = p.max; amount.step = p.step; amount.value = p.amount;
        rate.min = p.rmin; rate.max = p.rmax; rate.value = p.rate;
        tenure.max = p.tmax; tenure.min = p.tmin || 1; tenure.value = p.tenure;
        var lim = box.querySelector("[data-lim=amount]"); if (lim) lim.innerHTML = "<span>" + inrShort(p.min) + "</span><span>" + inrShort(p.max) + "</span>";
        var lr = box.querySelector("[data-lim=rate]"); if (lr) lr.innerHTML = "<span>" + p.rmin + "%</span><span>" + p.rmax + "%</span>";
        var lt = box.querySelector("[data-lim=tenure]"); if (lt) lt.innerHTML = "<span>" + (p.tmin || 1) + "</span><span>" + p.tmax + " " + tenureUnit + "</span>";
        calc();
      });
    });
    var first = box.querySelector(".tab.active[data-preset]") || box.querySelector(".tab[data-preset]");
    if (first) first.click(); else calc();
  });

  /* ---------- Eligibility checker ---------- */
  var elig = document.getElementById("elig-form");
  if (elig) {
    elig.addEventListener("submit", function (e) {
      e.preventDefault();
      var g = function (id) { return +document.getElementById(id).value || 0; };
      var type = document.getElementById("e-type").value;
      var income = g("e-income"), obligations = g("e-emi"), age = g("e-age");
      var rates = { home: 8.5, lap: 9.5, personal: 11.5, business: 14, car: 9.2 };
      var foir = { home: 0.55, lap: 0.55, personal: 0.5, business: 0.5, car: 0.5 }[type];
      var maxTenureYrs = { home: 30, lap: 15, personal: 5, business: 5, car: 7 }[type];
      var retire = type === "business" ? 65 : 60;
      var tenure = Math.max(1, Math.min(maxTenureYrs, retire - age));
      var capacity = income * foir - obligations;
      var r = rates[type], n = tenure * 12, mr = r / 12 / 100;
      var amt = capacity > 0 ? capacity * (Math.pow(1 + mr, n) - 1) / (mr * Math.pow(1 + mr, n)) : 0;
      var out = document.getElementById("elig-result");
      out.hidden = false;
      if (amt <= 0) {
        out.innerHTML = '<p><b>Current obligations are using most of your income.</b> A co-applicant or closing a small loan usually changes the picture. Talk to us and we will work it out with you.</p>';
      } else {
        out.innerHTML =
          '<div class="big"><small>Indicative eligibility</small>' + inrShort(Math.round(amt / 10000) * 10000) + '</div>' +
          '<dl><dt>Loan type</dt><dd>' + document.getElementById("e-type").selectedOptions[0].text + '</dd>' +
          '<dt>Tenure considered</dt><dd>' + tenure + ' years</dd>' +
          '<dt>Rate assumed</dt><dd>' + r + '% p.a.</dd>' +
          '<dt>EMI capacity</dt><dd>' + inr(capacity) + ' / month</dd></dl>' +
          '<p style="font-size:.85rem;color:#BFD2E1;margin:0">Indicative only. Final eligibility depends on the lender’s policy, credit score and documents.</p>';
      }
      var wa = document.getElementById("elig-wa");
      wa.href = waLink("Hi, I checked my eligibility on " + (SITE.domain || "your website") + ".\nLoan type: " + document.getElementById("e-type").selectedOptions[0].text + "\nMonthly income: " + inr(income) + "\nExisting EMIs: " + inr(obligations) + "\nAge: " + age + "\nIndicative eligibility: " + (amt > 0 ? inrShort(amt) : "to discuss") + "\n\nPlease call me back.");
      wa.hidden = false;
      out.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
  }

  /* ---------- footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
