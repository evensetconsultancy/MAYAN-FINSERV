# -*- coding: utf-8 -*-
"""Builds every page of the Mayan Finserv Solutions website.
Change brand/contact details in SITE below and re-run:  python3 build.py
"""
import json, os, html

SITE = {
    "brand": "Mayan Finserv Solutions",
    "short": "Mayan Finserv",
    "tagline": "Your Funding Partner",
    "owner": "Viswanadha Achari",
    "phone_display": "+91 99859 00483",
    "phone_tel": "+919985900483",
    "whatsapp": "919985900483",
    "email": "viswaraj58@gmail.com",
    "address": "2/52, Aspari Road, Adoni – 518301, Kurnool District, Andhra Pradesh",
    "city": "Adoni",
    "domain": "mayanfinserv.com",
    "url": "https://www.mayanfinserv.com",
    "hours": "Mon – Sat, 9:30 AM – 7:00 PM",
    "maps": "https://www.google.com/maps/search/?api=1&query=2%2F52+Aspari+Road+Adoni+518301",
    # Illustrative figures — confirm with client before go-live
    "stats": [("₹120 Cr+", "loans disbursed"), ("3,500+", "happy customers"),
              ("25+", "banks and NBFC partners"), ("48 hrs", "typical in-principle approval")],
}

BANKS = ["State Bank of India", "Bank of Baroda", "Canara Bank", "Union Bank of India",
         "Punjab National Bank", "Indian Bank", "Bank of India", "Central Bank of India",
         "Indian Overseas Bank", "UCO Bank", "HDFC Bank", "ICICI Bank", "Axis Bank",
         "Kotak Mahindra Bank", "IDFC FIRST Bank", "Federal Bank", "Karur Vysya Bank"]
NBFCS = ["Bajaj Finserv", "Tata Capital", "Aditya Birla Capital", "L&T Finance",
         "Piramal Finance", "Shriram Finance", "Cholamandalam Finance", "Poonawalla Fincorp",
         "HDB Financial Services", "IIFL Finance", "Hero FinCorp", "Mahindra Finance"]

# ---------------------------------------------------------------- products
PRODUCTS = [
 {"slug":"home-loan","name":"Home Loan","abbr":"HL","tag":"From 8.35% p.a.",
  "blurb":"Buy, build, extend or renovate your home with tenures up to 30 years.",
  "hero":"Own the home you have been planning for.",
  "intro":"Whether it is a first flat in Kurnool, a plot and construction in Adoni, or a balance transfer from a costly lender, we compare offers from public sector banks, private banks and housing finance companies and hand you the best one. One set of documents, one point of contact, no running between branches.",
  "kv":[("8.35% – 10.5%","Interest rate p.a."),("Up to 30 yrs","Tenure"),("Up to 90%","Of property value")],
  "features":["Purchase, construction, plot plus construction, extension and renovation","Balance transfer with top-up at lower rates","Joint loans with spouse or parents to increase eligibility","PMAY and government subsidy assistance where applicable","Pre-approved sanction so you can negotiate with the builder","Doorstep document pickup across Kurnool district"],
  "eligibility":["Salaried: minimum 2 years of work experience, age 21 to 60 at loan maturity","Self-employed: minimum 3 years in business, age 21 to 65 at maturity","Minimum monthly income of ₹15,000 (salaried) or ₹2 lakh annual profit (self-employed)","CIBIL score of 700 or above for the best rates; lower scores considered with NBFC partners"],
  "docs":["KYC: PAN, Aadhaar, passport size photographs","Income: 3 months salary slips and Form 16, or 2 years ITR with financials","Bank statements for the last 6 months","Property papers: sale agreement, title deed, approved plan, EC, tax receipts"],
  "faq":[("How much home loan can I get?","Lenders usually allow EMIs up to 50 to 60 percent of your net monthly income after existing EMIs. Use our eligibility checker for an indicative figure, then we confirm it with the lender."),("Fixed or floating rate?","Most home loans today are floating and linked to the repo rate. Fixed rates cost more. We explain the trade off for your case before you sign."),("Can I transfer my existing home loan?","Yes. If your current rate is 0.5 percent or more above today's rates, a balance transfer with a top up usually saves a meaningful amount. We do the paperwork.")],
  "preset":{"min":500000,"max":50000000,"step":100000,"amount":3500000,"rmin":8,"rmax":12,"rate":8.6,"tmin":5,"tmax":30,"tenure":20}},
 {"slug":"personal-loan","name":"Personal Loan","abbr":"PL","tag":"Approval in 24 to 72 hours",
  "blurb":"Unsecured funds for weddings, education, medical needs or travel, without collateral.",
  "hero":"Money for what matters, without pledging anything.",
  "intro":"A personal loan is the fastest way to arrange ₹50,000 to ₹40 lakh for a wedding, hospital bill, education fee, home repair or to consolidate credit card dues. We place your file with the lender most likely to approve it at the lowest rate, so you are not hit by multiple credit enquiries.",
  "kv":[("10.5% – 18%","Interest rate p.a."),("1 – 6 yrs","Tenure"),("₹50K – ₹40 L","Loan amount")],
  "features":["No collateral or guarantor","Minimal documentation for salaried applicants","Pre-approved offers for customers of partner banks","Debt consolidation to replace 36 percent card interest with a single EMI","Part prepayment and foreclosure options","Disbursal directly to your bank account"],
  "eligibility":["Salaried employees of private, public and government organisations, age 21 to 58","Self-employed professionals and business owners, age 23 to 65","Minimum net monthly income of ₹15,000 in Adoni and ₹25,000 in metro cities","CIBIL score of 700 and above; new to credit customers considered with select NBFCs"],
  "docs":["PAN and Aadhaar","Last 3 months salary slips or last 2 years ITR","Last 6 months bank statement","Employment proof or business proof (GST, Udyam, shop licence)"],
  "faq":[("How fast is disbursal?","With complete documents, salaried applicants typically receive funds in 24 to 72 hours. Self-employed files take 3 to 7 working days."),("Does applying reduce my credit score?","Every lender enquiry leaves a mark. That is why we assess your profile first and send it to one lender that fits, instead of applying everywhere."),("Can I prepay?","Yes. Most lenders allow part prepayment after 6 to 12 EMIs, with charges of 2 to 4 percent on the prepaid amount. Some offer zero charges; we tell you which.")],
  "preset":{"min":50000,"max":4000000,"step":10000,"amount":500000,"rmin":10,"rmax":24,"rate":12.5,"tmin":1,"tmax":6,"tenure":4}},
 {"slug":"business-loan","name":"Business Loan","abbr":"BL","tag":"MSME and trader friendly",
  "blurb":"Working capital, machinery, expansion and Mudra/CGTMSE backed loans for MSMEs.",
  "hero":"Capital that keeps your business moving.",
  "intro":"From a kirana store needing stock for the season to a rice mill adding a new line, we arrange unsecured business loans, cash credit and overdraft limits, term loans for machinery, and government scheme loans under Mudra, PMEGP and CGTMSE. We understand how Rayalaseema businesses actually keep their books and prepare the file accordingly.",
  "kv":[("11% – 20%","Interest rate p.a."),("1 – 7 yrs","Tenure"),("₹1 L – ₹5 Cr","Loan amount")],
  "features":["Unsecured business loans up to ₹75 lakh on banking and GST turnover","Cash credit and overdraft against stock and receivables","Machinery and equipment term loans, including CLCSS subsidy assistance","Mudra (Shishu, Kishore, Tarun) and PMEGP scheme loans","CGTMSE covered loans with no collateral up to ₹5 crore","Invoice discounting and dealer finance"],
  "eligibility":["Proprietorships, partnerships, LLPs and private limited companies","Minimum 2 years of business vintage (1 year for scheme loans)","Annual turnover of ₹10 lakh and above; GST registration where applicable","Promoter age 23 to 65; CIBIL and commercial CIBIL considered"],
  "docs":["KYC of business and promoters, Udyam certificate","GST returns for 12 months and ITR with audited or CA certified financials for 2 years","Bank statements for 12 months of all business accounts","Business proof: shop licence, partnership deed or incorporation documents"],
  "faq":[("I file returns under presumptive tax. Can I still get a loan?","Yes. Several NBFC partners lend on banking turnover and GST data rather than declared profit. Expect a slightly higher rate."),("What is CGTMSE?","A government guarantee scheme that lets banks lend up to ₹5 crore to MSMEs without collateral. We check whether your business qualifies and route the file to a bank that actively uses the scheme."),("How long does a business loan take?","Unsecured NBFC loans: 3 to 7 days. Bank cash credit and term loans: 3 to 6 weeks depending on valuation and appraisal.")],
  "preset":{"min":100000,"max":50000000,"step":50000,"amount":1500000,"rmin":10,"rmax":24,"rate":14,"tmin":1,"tmax":7,"tenure":3}},
 {"slug":"loan-against-property","name":"Loan Against Property","abbr":"LAP","tag":"Unlock value, keep the property",
  "blurb":"Large ticket funds against residential, commercial or industrial property at low rates.",
  "hero":"Your property can fund your next move.",
  "intro":"Mortgage a self-occupied house, shop, godown or industrial shed and borrow up to 70 percent of its market value for business expansion, education abroad, a wedding, or to consolidate costly debt. You continue to use the property as before. Rates are far lower than unsecured loans because the lender is secured.",
  "kv":[("9% – 12.5%","Interest rate p.a."),("Up to 15 yrs","Tenure"),("Up to 70%","Of market value")],
  "features":["Residential, commercial, industrial and mixed use property accepted","Term loan or dropline overdraft structures","Lease rental discounting against rented commercial property","Balance transfer of existing LAP with top up","Loan to companies and firms with directors and partners as co-applicants","Flexible end use with minimal justification"],
  "eligibility":["Property owner aged 25 to 70 at loan maturity, salaried or self-employed","Clear and marketable title with approved construction","Income to support EMI: salary, business profit or rental income","Properties in municipal limits of Adoni, Kurnool, Nandyal, Bellary and other towns we cover"],
  "docs":["KYC and income documents as for a home loan","Complete chain of title documents, latest EC for 13 years, property tax receipts","Approved building plan and occupancy certificate where available","Rental agreements if rental income is considered"],
  "faq":[("How is the property valued?","The lender appoints an approved valuer who reports market value based on location, construction and comparable sales. The loan is a percentage of that value."),("Can agricultural land be mortgaged?","Generally not for LAP. A few co-operative and regional lenders consider converted or NA land. Ask us for your specific case."),("What if the property is in my father's name?","He can be the co-applicant and mortgagor while you are the main applicant on income. This is common and lenders accept it.")],
  "preset":{"min":500000,"max":100000000,"step":100000,"amount":5000000,"rmin":8.5,"rmax":14,"rate":9.75,"tmin":3,"tmax":15,"tenure":12}},
 {"slug":"car-loan","name":"Car Loan","abbr":"CL","tag":"New and used cars",
  "blurb":"Up to 100 percent on-road funding for new cars and up to 85 percent for used cars.",
  "hero":"Drive it home this week.",
  "intro":"We tie up with the banks and NBFCs that offer the highest funding and lowest rates on the models sold at dealerships in Adoni, Kurnool and Bellary. New car, pre-owned car, or a commercial vehicle for your business, we arrange the loan while you pick the colour.",
  "kv":[("8.75% – 12%","New car rate p.a."),("Up to 7 yrs","Tenure"),("Up to 100%","On-road funding")],
  "features":["New car loans up to 100 percent of on-road price for salaried applicants","Used car loans up to 85 percent of valuation, cars up to 10 years old at maturity","Commercial vehicle and two wheeler loans","Refinance on an owned car to release cash","Tie ups with dealers for same day delivery","No income proof programmes for select profiles"],
  "eligibility":["Salaried: minimum ₹20,000 monthly income, age 21 to 60","Self-employed: 2 years ITR or banking based programmes, age 21 to 65","Farmers with land holding records considered by select banks","CIBIL 700 and above for 100 percent funding; lower scores at reduced LTV"],
  "docs":["PAN, Aadhaar, driving licence","Income proof: salary slips or ITR, or 6 months bank statement","Proforma invoice from the dealer","For used cars: RC copy, insurance and valuation report"],
  "faq":[("Which is better, dealer finance or your loan?","Often the same banks. We negotiate the rate and processing fee separately from the car price, so you know exactly what the finance costs."),("Can I get a loan without ITR?","Yes, for many profiles: salaried with bank credits, farmers with land records, and existing loan customers with good repayment track. Funding may be 80 to 90 percent."),("Is the hypothecation removed automatically?","No. After the last EMI, collect the NOC and Form 35 from the lender and apply at the RTO. We help with this step too.")],
  "preset":{"min":100000,"max":5000000,"step":25000,"amount":800000,"rmin":8,"rmax":16,"rate":9.25,"tmin":1,"tmax":7,"tenure":5}},
 {"slug":"credit-cards","name":"Credit Cards","abbr":"CC","tag":"Lifetime free options",
  "blurb":"Cashback, fuel, travel and premium cards from leading banks, matched to how you spend.",
  "hero":"The right card for the way you spend.",
  "intro":"A credit card used well builds your credit history and earns rewards on money you would spend anyway. We help you choose between cashback, fuel, shopping and travel cards from partner banks, check your eligibility before you apply, and handle the paperwork so the card reaches you without a rejection on your record.",
  "kv":[("0 – ₹2,999","Annual fee"),("Up to 45 days","Interest free credit"),("5% – 10%","Typical cashback categories")],
  "features":["Lifetime free cards for salaried applicants","Fuel cards with surcharge waiver for daily commuters and transporters","Cashback and shopping cards for online spends","Travel cards with lounge access and air miles","Secured cards against fixed deposit for new to credit customers","Business cards with GST invoice and expense tracking"],
  "eligibility":["Age 21 to 65, Indian resident","Salaried with net income of ₹20,000 per month, or self-employed with ITR of ₹3 lakh","CIBIL 720 and above for premium cards; secured cards for any score","Existing card holders can upgrade or add a second bank card"],
  "docs":["PAN and Aadhaar","Latest salary slip or ITR","Address proof if different from Aadhaar","For secured cards: FD receipt or FD opened with the issuing bank"],
  "faq":[("Will a credit card hurt my CIBIL score?","Not if you pay the full statement amount on time and use less than 30 to 40 percent of the limit. Used this way it improves your score."),("What is the interest if I pay the minimum due?","Typically 36 to 42 percent per year. Never pay only the minimum for long; convert large spends to EMI or take a personal loan instead."),("Which card should I take?","Tell us your top three monthly spends. Fuel, groceries and online shopping each have a card that pays back the most on that category.")],
  "preset":None},
]

# ---------------------------------------------------------------- blog
POSTS = [
 {"slug":"home-loan-balance-transfer-guide","title":"When does a home loan balance transfer actually save money?","date":"15 September 2026","cat":"Home Loans",
  "summary":"A lower rate is not the whole story. Here is the simple arithmetic we use before advising any customer to switch lenders.",
  "body":"""<p>Every few months a customer walks in with a flyer promising a home loan at a rate half a percent lower than what they pay today. Sometimes switching is a clear win. Sometimes the costs eat the saving. The arithmetic takes five minutes.</p>
<h2>Step 1: What is the real gap?</h2><p>Compare your current rate with the rate you are actually offered after the lender checks your file, not the headline rate on the flyer. A 0.5 percent gap on a ₹30 lakh loan with 15 years left saves roughly ₹1.4 lakh in interest over the remaining tenure, or about ₹850 a month in EMI.</p>
<h2>Step 2: Add up the switching costs</h2><ul><li>Processing fee of the new lender, usually 0.25 to 0.5 percent plus GST, sometimes waived</li><li>Legal and valuation charges, around ₹5,000 to ₹10,000</li><li>Stamp duty on the new mortgage deed, which varies by state</li><li>Foreclosure charges from your current lender, nil for floating rate home loans to individuals</li></ul>
<h2>Step 3: How many years are left?</h2><p>Interest is front loaded. In the first third of a loan, most of the EMI is interest and a lower rate helps a lot. In the last third, you are mostly repaying principal and the saving is small. If fewer than five years remain, a transfer rarely pays.</p>
<h2>The rule of thumb we use</h2><div class="note">Switch when the rate gap is at least 0.5 percent, at least 8 years of tenure remain, and total switching costs are recovered within 12 to 18 months of the EMI saving.</div>
<p>A top up loan bundled with the transfer often makes the decision easier, since it gives you funds at home loan rates for renovation or to close a costly personal loan. Bring your latest loan statement and we will run the numbers for your loan in ten minutes.</p>"""},
 {"slug":"cibil-score-explained","title":"Your CIBIL score: what moves it and how to fix it before you apply","date":"2 September 2026","cat":"Credit",
  "summary":"Most rejections we see are avoidable. Six things that push a score down and the order in which to repair them.",
  "body":"""<p>Lenders in India rely on your CIBIL score, a three digit number between 300 and 900, to decide whether to lend and at what rate. Above 750 you get the best offers. Between 650 and 750 you will be approved but may pay more. Below 650, options narrow to a few NBFCs.</p>
<h2>What moves the score</h2><ul><li><b>Payment history</b> (largest weight). One EMI or card payment more than 30 days late stays on the report for years.</li><li><b>Credit utilisation.</b> Using more than 40 percent of your card limits every month signals stress.</li><li><b>Enquiries.</b> Every loan application is recorded. Six enquiries in three months looks desperate.</li><li><b>Mix and age.</b> A long history with both secured (home, car) and unsecured (card, personal) credit helps.</li><li><b>Settled accounts.</b> A loan closed for less than the full amount is marked "settled" and hurts badly.</li><li><b>Errors.</b> Loans you never took, wrong dates, duplicate accounts. These are more common than people think.</li></ul>
<h2>Fix in this order</h2><ol><li>Pull your free report from cibil.com and check every line.</li><li>Raise a dispute for any error. Corrections take 30 days.</li><li>Clear any overdue amount and collect the no dues letter.</li><li>Bring card balances under 30 percent of limit before the statement date.</li><li>Stop applying anywhere for three to six months.</li></ol>
<p>If your score is below 650, ask us before applying. We know which partners lend at that level and we avoid adding rejections to your file.</p>"""},
 {"slug":"msme-loan-schemes-2026","title":"Government loan schemes every small business in Andhra Pradesh should know","date":"20 August 2026","cat":"Business Loans",
  "summary":"Mudra, PMEGP, CGTMSE, Stand Up India and the state schemes, explained in plain terms with who qualifies for what.",
  "body":"""<p>Small businesses often pay 18 to 24 percent on private loans when a bank would lend at 9 to 12 percent under a government scheme. The schemes are real and the banks do lend under them. The difficulty is knowing which one fits and preparing the file the way the bank wants it.</p>
<h2>Pradhan Mantri Mudra Yojana</h2><p>Loans up to ₹20 lakh for non-farm micro enterprises: Shishu (up to ₹50,000), Kishore (₹50,000 to ₹5 lakh), Tarun (₹5 lakh to ₹10 lakh) and Tarun Plus (₹10 lakh to ₹20 lakh for those who have repaid a Tarun loan). No collateral. Good for shops, tailoring units, food stalls, auto owners and service providers.</p>
<h2>PMEGP</h2><p>A subsidy linked scheme for new manufacturing units up to ₹50 lakh and service units up to ₹20 lakh. Subsidy of 15 to 35 percent depending on category and location. Applications go through KVIC or the District Industries Centre, then to a bank.</p>
<h2>CGTMSE</h2><p>Not a loan but a guarantee. The trust covers 75 to 85 percent of a bank's loss, so banks lend up to ₹5 crore to MSMEs without collateral. Ask specifically for a CGTMSE covered loan; not every branch offers it unprompted.</p>
<h2>Stand Up India</h2><p>Loans of ₹10 lakh to ₹1 crore for greenfield enterprises promoted by women or SC/ST entrepreneurs. At least one such loan per bank branch is the mandate.</p>
<h2>What the bank will ask for</h2><ul><li>Udyam registration certificate</li><li>A project report with realistic sales and cash flow projections</li><li>Quotations for machinery or stock</li><li>KYC, bank statements, and ITR where the business is running</li></ul>
<p>We prepare the project report and file the application with a branch that is active in the scheme. That alone changes the odds considerably.</p>"""},
 {"slug":"used-car-loan-checklist","title":"Buying a used car on loan: the checklist before you pay the token amount","date":"5 August 2026","cat":"Car Loans",
  "summary":"Funding limits, valuation, RC transfer and the mistakes that delay a used car loan by weeks.",
  "body":"""<p>Used car loans are approved quickly when the car and its papers are clean. Most delays come from the car, not the borrower. Check these before you commit.</p>
<h2>Age and kilometres</h2><p>Lenders fund cars that will be under 10 years old at the end of the loan. A 6 year old car therefore gets at most a 4 year loan. Very high odometer readings reduce valuation.</p>
<h2>Funding limit</h2><p>Expect 70 to 85 percent of the lender's valuation, which is usually below the asking price. Keep 20 to 30 percent ready as down payment plus RC transfer and insurance costs.</p>
<h2>Papers to inspect</h2><ul><li>Original RC with no existing hypothecation, or an NOC and Form 35 if there was a loan</li><li>Valid insurance and PUC</li><li>Service history and the second key</li><li>Seller's ID matching the RC name</li><li>No pending challans or tax dues on the Parivahan portal</li></ul>
<h2>Process with us</h2><ol><li>Share the RC and photos; we get an indicative valuation in a day.</li><li>Loan sanction in 2 to 3 working days.</li><li>Lender pays the seller directly; RC transfer with hypothecation to the lender is filed at the RTO.</li></ol>
<p>One caution: never pay the full amount to a private seller before the RC transfer papers are signed. A token amount with a written agreement is enough to hold the car.</p>"""},
]

TESTIMONIALS = [
 ("Got my home loan sanctioned from a public sector bank at a rate the branch itself had told me was not possible. The team handled every document pickup at my shop.","Ramesh Naidu","Textile merchant, Adoni"),
 ("My CIBIL was 640 after a missed card payment. Instead of applying everywhere they fixed the report first, then got a personal loan for my daughter's fees in a week.","Lakshmi Devi","School teacher, Kurnool"),
 ("Working capital limit for our rice mill under CGTMSE, without giving any extra property. Explained every clause of the sanction letter before we signed.","Mohammed Irfan","Rice mill owner, Yemmiganur"),
]

# ---------------------------------------------------------------- html helpers
LOGO_SVG = """<svg class="logo" viewBox="0 0 96 100" aria-hidden="true"><g transform="translate(2,0) scale(1.0000)"><path d="M46 2 L90 21 L90 53 C90 76 71 91 46 100 C21 91 2 76 2 53 L2 21 Z" fill="#1F3A93"/><path d="M46 2 L90 21 L90 53 C90 76 71 91 46 100 Z" fill="#162B6E"/><path d="M22 66 L38 48 L52 60 L72 36" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 36 L72 36 L72 48" fill="none" stroke="#F2B233" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g></svg>"""
WA_SVG = """<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9 3 3.3 8.7 3.3 15.7c0 2.5.7 4.9 2 6.9L3 29l6.6-2.1a12.7 12.7 0 0 0 6.4 1.7c7 0 12.7-5.7 12.7-12.7S23 3 16 3zm0 23.3c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1.2 1.2-3.8-.3-.4a10.5 10.5 0 0 1-1.7-5.8C5.2 9.9 10 5.1 16 5.1s10.8 4.8 10.8 10.6S22 26.3 16 26.3zm5.9-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.3-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.3 1.4 3.5c.2.2 2.4 3.6 5.8 5 .8.4 1.4.6 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.6.3-.8.3-1.4.2-1.6-.1-.1-.3-.2-.6-.4z"/></svg>"""

def esc(s): return html.escape(s, quote=True)

def head(title, desc, path, extra=""):
    canonical = SITE["url"] + "/" + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {SITE['brand']}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)} | {SITE['brand']}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#1F3A93">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script>window.SITE={json.dumps({"whatsapp":SITE["whatsapp"],"domain":SITE["domain"]})};</script>
{extra}
</head>
<body>
"""

def header():
    prods = "".join(f'<a href="{p["slug"]}.html">{p["name"]}</a>' for p in PRODUCTS)
    return f"""<div class="topbar"><div class="wrap">
  <span>📍 {SITE['city']}, Andhra Pradesh &nbsp;·&nbsp; {SITE['hours']}</span>
  <span>📞 <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a> &nbsp;·&nbsp; ✉ <a href="mailto:{SITE['email']}">{SITE['email']}</a></span>
</div></div>
<header class="header"><div class="wrap">
  <a class="brand" href="index.html">{LOGO_SVG}<span>{SITE['brand']}<small>{SITE['tagline']}</small></span></a>
  <button class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
  <nav class="nav" aria-label="Main">
    <a href="index.html">Home</a>
    <div class="has-menu"><a href="home-loan.html">Loans</a><div class="menu">{prods}</div></div>
    <a href="emi-calculator.html">EMI Calculator</a>
    <a href="eligibility.html">Eligibility</a>
    <a href="about.html">About</a>
    <a href="blog.html">Blog</a>
    <a href="contact.html">Contact</a>
    <a class="btn btn-primary btn-sm header-cta" href="apply.html">Apply Now</a>
  </nav>
</div></header>
<main>
"""

def footer():
    prods = "".join(f'<a href="{p["slug"]}.html">{p["name"]}</a>' for p in PRODUCTS)
    return f"""</main>
<section class="cta-band"><div class="wrap">
  <div><h2>Ready to talk about your loan?</h2><p>Free consultation. We compare offers from {len(BANKS)+len(NBFCS)}+ lenders and you choose.</p></div>
  <div style="display:flex;gap:.8rem;flex-wrap:wrap"><a class="btn btn-outline" href="apply.html">Apply Online</a><a class="btn btn-wa" href="https://wa.me/{SITE['whatsapp']}?text=Hi%2C%20I%20want%20to%20know%20about%20a%20loan." target="_blank" rel="noopener">{WA_SVG} WhatsApp Us</a></div>
</div></section>
<footer class="footer">
  <div class="wrap">
    <div>
      <a class="brand" href="index.html">{LOGO_SVG}<span>{SITE['brand']}<small>{SITE['tagline']}</small></span></a>
      <p style="margin-top:1rem">Loan distribution and advisory service based in {SITE['city']}, serving Kurnool, Nandyal, Bellary and Raichur districts. We work with nationalised banks, private banks and leading NBFCs to get you the best offer.</p>
      <p><b style="color:#fff">Proprietor:</b> {SITE['owner']}</p>
    </div>
    <div><h4>Loans</h4>{prods}</div>
    <div><h4>Company</h4><a href="about.html">About Us</a><a href="emi-calculator.html">EMI Calculator</a><a href="eligibility.html">Eligibility Check</a><a href="blog.html">Blog</a><a href="careers.html">Careers</a><a href="branches.html">Branches</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a></div>
    <div><h4>Reach us</h4>
      <p>{SITE['address']}</p>
      <a href="tel:{SITE['phone_tel']}">📞 {SITE['phone_display']}</a>
      <a href="mailto:{SITE['email']}">✉ {SITE['email']}</a>
      <a href="https://wa.me/{SITE['whatsapp']}" target="_blank" rel="noopener">💬 WhatsApp</a>
      <p style="margin-top:.6rem">{SITE['hours']}</p>
    </div>
  </div>
  <div class="footer-bottom"><div class="wrap">
    <span>© <span data-year>2026</span> {SITE['brand']}. All rights reserved.</span>
    <span><a href="privacy-policy.html" style="display:inline;margin:0 .6rem 0 0">Privacy Policy</a> <a href="terms.html" style="display:inline;margin:0 .6rem">Terms of Use</a> <a href="disclaimer.html" style="display:inline;margin:0 0 0 .6rem">Disclaimer</a></span>
  </div></div>
  <div class="footer-bottom" style="border-top:0"><div class="wrap"><p class="fineprint" style="color:#8FA5B8;margin:0">{SITE['brand']} is a loan distribution and referral service. We are not a lender. Loan sanction, interest rates and terms are decided solely by the respective bank or NBFC. Bank and NBFC names are trademarks of their respective owners.</p></div></div>
</footer>
<a class="wa-float" href="https://wa.me/{SITE['whatsapp']}?text=Hi%2C%20I%20want%20to%20know%20about%20a%20loan." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<script src="assets/main.js"></script>
</body>
</html>
"""

def page(path, title, desc, body, extra=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(head(title, desc, path, extra) + header() + body + footer())
    print("wrote", path)

def page_head(eyebrow, h1, lead, crumbs):
    c = " › ".join(f'<a href="{h}">{t}</a>' if h else t for t, h in crumbs)
    return f"""<section class="page-head"><div class="wrap"><div class="crumbs">{c}</div><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p class="lead">{lead}</p></div></section>"""

def enquiry_form(subject, product_select=True, compact=False):
    opts = "".join(f'<option>{p["name"]}</option>' for p in PRODUCTS)
    sel = f'<div><label for="f-type">Loan type</label><select id="f-type" name="type">{opts}</select></div>' if product_select else ""
    return f"""<form class="form" data-wa="{esc(subject)}">
  <div class="form-row">
    <div><label for="f-name">Full name</label><input id="f-name" name="name" required autocomplete="name"></div>
    <div><label for="f-phone">Mobile number</label><input id="f-phone" name="phone" type="tel" required pattern="[6-9][0-9]{{9}}" placeholder="10 digit mobile" autocomplete="tel"></div>
  </div>
  <div class="form-row">
    {sel}
    <div><label for="f-amount">Loan amount needed (₹)</label><input id="f-amount" name="amount" type="number" min="10000" step="1000" placeholder="e.g. 500000"></div>
  </div>
  {"" if compact else '<div class="form-row"><div><label for="f-city">City / town</label><input id="f-city" name="city" placeholder="Adoni"></div><div><label for="f-emp">Employment</label><select id="f-emp" name="employment"><option>Salaried</option><option>Self-employed / Business</option><option>Professional</option><option>Farmer</option><option>Other</option></select></div></div><div><label for="f-msg">Anything we should know?</label><textarea id="f-msg" name="message" placeholder="Existing loans, property details, timeline…"></textarea></div>'}
  <label class="consent"><input type="checkbox" name="consent" data-label="Consent to be contacted" required> I agree to be contacted by {SITE['brand']} on call or WhatsApp about my enquiry.</label>
  <button class="btn btn-wa" type="submit">{WA_SVG} Send on WhatsApp</button>
  <p class="hint">Your details open in a WhatsApp chat with us; nothing is stored on this website.</p>
</form>"""

def emi_block(presets, default, tenure_unit="years", show_schedule=True, show_tabs=True):
    tabs = "".join(f'<button type="button" class="tab{" active" if k==default else ""}" data-preset="{k}">{v["label"]}</button>' for k,v in presets.items()) if show_tabs else ""
    data = {k:{kk:vv for kk,vv in v.items() if kk!="label"} for k,v in presets.items()}
    sched = """<div class="table-wrap" style="margin-top:1.5rem"><table><thead><tr><th>Period</th><th>Principal paid</th><th>Interest paid</th><th>Balance</th></tr></thead><tbody data-o="schedule"></tbody></table></div>""" if show_schedule else ""
    return f"""<div class="emi" data-presets='{esc(json.dumps(data))}' data-tenure="{tenure_unit}" data-current="{presets[default]['label']}">
  {f'<div class="tabs">{tabs}</div>' if tabs else ''}
  <div class="calc">
    <div>
      <div class="range-row"><div class="lab"><label for="c-amount">Loan amount (₹)</label><span class="typed"><input type="number" id="c-amount-t" data-sync="c-amount" min="10000" step="1000" aria-label="Type loan amount"><output for="c-amount"></output></span></div><input type="range" id="c-amount" data-f="amount" min="100000" max="10000000" step="10000" value="1000000"><div class="lim" data-lim="amount"></div></div>
      <div class="range-row"><div class="lab"><label for="c-rate">Interest rate (% p.a.)</label><span class="typed"><input type="number" id="c-rate-t" data-sync="c-rate" min="1" max="40" step="0.01" aria-label="Type interest rate"></span></div><input type="range" id="c-rate" data-f="rate" min="6" max="24" step="0.05" value="10"><div class="lim" data-lim="rate"></div></div>
      <div class="range-row"><div class="lab"><label for="c-tenure">Tenure ({tenure_unit})</label><span class="typed"><input type="number" id="c-tenure-t" data-sync="c-tenure" min="1" max="360" step="1" aria-label="Type tenure"></span></div><input type="range" id="c-tenure" data-f="tenure" min="1" max="30" step="1" value="5"><div class="lim" data-lim="tenure"></div></div>
      {sched}
    </div>
    <div class="result">
      <div class="big"><small>Monthly EMI</small><span data-o="emi" class="num">—</span></div>
      <canvas data-o="chart" width="200" height="200"></canvas>
      <dl><dt>Principal</dt><dd data-o="principal" class="num"></dd><dt>Total interest</dt><dd data-o="interest" class="num"></dd><dt>Total payable</dt><dd data-o="total" class="num"></dd></dl>
      <a class="btn btn-wa" data-o="wa" href="#" target="_blank" rel="noopener">{WA_SVG} Apply with these numbers</a>
    </div>
  </div>
</div>"""

def faq_block(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items) + "</div>"

def partners_block():
    b = "".join(f'<span class="partner">{x}</span>' for x in BANKS)
    n = "".join(f'<span class="partner nbfc">{x}</span>' for x in NBFCS)
    return f"""<div class="partners">{b}</div><p class="center fineprint" style="margin:1.2rem 0 .6rem">and leading NBFCs</p><div class="partners">{n}</div>
<p class="center fineprint" style="margin-top:1.2rem">Lender names are listed to indicate the institutions whose products we distribute or refer. All trademarks belong to their respective owners. Final sanction rests with the lender.</p>"""

ALL_PRESETS = {p["slug"]:dict(p["preset"], label=p["name"]) for p in PRODUCTS if p["preset"]}

# ================================================================ pages
def build_index():
    stats = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v,l in SITE["stats"])
    prods = "".join(f"""<a class="card product" href="{p['slug']}.html"><div class="icon">{p['abbr']}</div><h3>{p['name']}</h3><p style="margin:0;color:var(--muted)">{p['blurb']}</p><span class="pill">{p['tag']}</span><span class="more">Know more</span></a>""" for p in PRODUCTS)
    quotes = "".join(f'<div class="quote"><div class="stars">★★★★★</div><p>“{t}”</p><div class="who">{w}<small>{r}</small></div></div>' for t,w,r in TESTIMONIALS)
    posts = "".join(f"""<a class="card" href="blog/{x['slug']}.html"><span class="pill">{x['cat']}</span><h3>{x['title']}</h3><p style="color:var(--muted);margin:0">{x['summary']}</p><span class="meta">{x['date']}</span></a>""" for x in POSTS[:3])
    home_faq = [("Do you charge the customer any fee?","Our consultation is free. We are paid by the lender on disbursal. Any lender processing fee is disclosed to you in writing before you accept the sanction."),
                ("Which lender will my loan come from?","We match your profile to the bank or NBFC most likely to approve it at the best rate, and tell you the name before applying. You always sign directly with the lender."),
                ("Do I need to visit your office?","Not necessarily. Share documents on WhatsApp and we do a doorstep pickup of originals in Adoni, Kurnool, Nandyal and nearby towns."),
                ("How long does approval take?","Personal and car loans: 1 to 3 days. Home loans and LAP: 7 to 15 days including legal and valuation. Business loans: 3 days to 6 weeks depending on the product.")]
    quick = emi_block({"quick":{"label":"Quick EMI","min":100000,"max":10000000,"step":50000,"amount":1500000,"rmin":7,"rmax":20,"rate":9.5,"tmin":1,"tmax":30,"tenure":10}}, "quick", show_schedule=False, show_tabs=False)
    # simplify the hero calculator: no chart/canvas visuals crowding; keep result
    body = f"""
<section class="hero"><div class="wrap">
  <div>
    <div class="eyebrow">{SITE['tagline']}</div>
    <h1>Loans from {len(BANKS)+len(NBFCS)}+ banks and NBFCs, one trusted local partner.</h1>
    <p class="lead">{SITE['brand']} compares home, personal, business, property and car loan offers from India's leading lenders and gets your file approved at the best rate. Based in {SITE['city']}, working across Rayalaseema and beyond.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="apply.html">Apply Now</a><a class="btn btn-outline" style="border-color:#fff;color:#fff" href="eligibility.html">Check Eligibility</a></div>
    <div class="hero-points"><span>Free consultation</span><span>Doorstep document pickup</span><span>Lowest rate match</span><span>No hidden charges</span></div>
  </div>
  <div class="hero-card">
    <h3>Quick EMI check</h3>
    <div class="emi" data-presets='{{}}' data-tenure="years" data-current="Loan">
      <div class="range-row"><div class="lab"><label for="h-amount">Loan amount (₹)</label><span class="typed"><input type="number" id="h-amount-t" data-sync="h-amount" min="10000" step="1000" aria-label="Type loan amount"><output for="h-amount"></output></span></div><input type="range" id="h-amount" data-f="amount" min="100000" max="10000000" step="50000" value="1500000"><div class="lim"><span>₹1 L</span><span>₹1 Cr</span></div></div>
      <div class="range-row"><div class="lab"><label for="h-rate">Interest rate</label><output for="h-rate"></output></div><input type="range" id="h-rate" data-f="rate" min="7" max="20" step="0.05" value="9.5"><div class="lim"><span>7%</span><span>20%</span></div></div>
      <div class="range-row"><div class="lab"><label for="h-tenure">Tenure</label><output for="h-tenure"></output></div><input type="range" id="h-tenure" data-f="tenure" min="1" max="30" step="1" value="10"><div class="lim"><span>1 yr</span><span>30 yrs</span></div></div>
      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;border-top:1px solid var(--line);padding-top:1rem">
        <div><div class="fineprint">Monthly EMI</div><div style="font-family:var(--font-display);font-size:1.9rem;font-weight:800;color:var(--navy)" class="num" data-o="emi">—</div><div class="fineprint">Total interest <b data-o="interest" class="num"></b></div></div>
        <a class="btn btn-primary btn-sm" href="emi-calculator.html">Full calculator</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section-tight"><div class="wrap"><div class="stats">{stats}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head center"><div class="eyebrow">What we offer</div><h2>Loans for every stage of life and business</h2><p class="lead">Pick a product to see rates, eligibility, documents and an EMI calculator tuned to it.</p></div>
  <div class="grid grid-3">{prods}</div>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head center"><div class="eyebrow">How it works</div><h2>From enquiry to disbursal in four steps</h2></div>
  <div class="steps">
    <div class="step"><h3>Tell us your need</h3><p>Fill the two minute form or message us on WhatsApp. We call back within a working hour.</p></div>
    <div class="step"><h3>Profile and match</h3><p>We assess income, credit and property, then shortlist the lender with the best fit. No blind applications.</p></div>
    <div class="step"><h3>Documents and sanction</h3><p>Doorstep pickup, file submission, follow up with the branch, and a sanction letter you understand.</p></div>
    <div class="step"><h3>Disbursal and after</h3><p>Money in your account or to the seller. We stay on for EMI queries, statements, NOC and closure.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head center"><div class="eyebrow">Lending partners</div><h2>Associated with nationalised and private banks and leading NBFCs</h2></div>
  {partners_block()}
</div></section>

<section class="section section-navy"><div class="wrap">
  <div class="section-head center"><div class="eyebrow">Why Mayan Finserv</div><h2>A local team that knows the lenders and knows you</h2></div>
  <div class="grid grid-4">
    <div><h3>Best rate, not first rate</h3><p>We negotiate with several lenders on your behalf and show you the comparison.</p></div>
    <div><h3>One file, one contact</h3><p>{SITE['owner']} and team handle your case end to end. No call centre queues.</p></div>
    <div><h3>Credit score protected</h3><p>One well placed application instead of five rejected ones.</p></div>
    <div><h3>Honest advice</h3><p>If a loan is not right for you now, we say so and tell you what to fix first.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head center"><div class="eyebrow">Customer stories</div><h2>What our customers say</h2></div>
  <div class="grid grid-3">{quotes}</div>
</div></section>

<section class="section section-alt"><div class="wrap">
  <div class="two-col">
    <div><div class="eyebrow">Loan FAQ</div><h2>Questions we hear every day</h2>{faq_block(home_faq)}<a class="btn btn-outline" href="faq.html" style="margin-top:1rem">All FAQs</a></div>
    <div class="card"><h3>Get a call back</h3>{enquiry_form("Call back request from website", compact=True)}</div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head" style="display:flex;justify-content:space-between;align-items:end;gap:1rem;flex-wrap:wrap"><div><div class="eyebrow">From the blog</div><h2 style="margin:0">Straight talk about loans</h2></div><a class="btn btn-outline btn-sm" href="blog.html">All articles</a></div>
  <div class="grid grid-3">{posts}</div>
</div></section>
"""
    page("index.html", "Home, Personal, Business and Property Loans in Adoni", f"{SITE['brand']}, {SITE['city']}: loan distribution partner for home loans, personal loans, business loans, loan against property, car loans and credit cards from 25+ banks and NBFCs.", body)

def build_products():
    for p in PRODUCTS:
        feats = "".join(f"<li>{x}</li>" for x in p["features"])
        elig = "".join(f"<li>{x}</li>" for x in p["eligibility"])
        docs = "".join(f"<li>{x}</li>" for x in p["docs"])
        kv = "".join(f"<div><b>{v}</b><span>{l}</span></div>" for v,l in p["kv"])
        calc = ""
        if p["preset"]:
            calc = f"""<section class="section section-alt"><div class="wrap"><div class="section-head"><div class="eyebrow">Plan your EMI</div><h2>{p['name']} EMI calculator</h2><p class="lead">Rates and limits preset for a typical {p['name'].lower()}. Move the sliders to match your case.</p></div>{emi_block({p['slug']:ALL_PRESETS[p['slug']]}, p['slug'], show_tabs=False)}</div></section>"""
        others = "".join(f'<a href="{o["slug"]}.html">{o["name"]}</a>' for o in PRODUCTS if o is not p)
        body = page_head(p["tag"], p["hero"], p["blurb"], [("Home","index.html"),("Loans","home-loan.html"),(p["name"],None)]) + f"""
<section class="section"><div class="wrap two-col">
  <div class="prose">
    <p class="lead" style="color:var(--ink)">{p['intro']}</p>
    <div class="kv">{kv}</div>
    <h2>Features</h2><ul class="checks">{feats}</ul>
    <h2>Eligibility</h2><ul class="checks">{elig}</ul>
    <h2>Documents required</h2><ul class="checks">{docs}</ul>
    <div class="note">Rates and limits shown are indicative ranges across our lending partners as of this month and change with lender policy. Your exact offer depends on profile, credit score and the lender's assessment.</div>
    <h2>Frequently asked</h2>{faq_block(p['faq'])}
  </div>
  <aside class="sticky">
    <div class="card"><h3>Apply for a {p['name']}</h3>{enquiry_form(p['name'] + ' enquiry', product_select=False, compact=True)}</div>
    <div class="card" style="margin-top:1.2rem"><h3>Other products</h3><div style="display:grid;gap:.4rem">{others}</div></div>
  </aside>
</div></section>
{calc}
"""
        page(f"{p['slug']}.html", f"{p['name']} in Adoni and Kurnool", f"{p['name']} through {SITE['brand']}: {p['blurb']} Compare offers from 25+ banks and NBFCs.", body)

def build_calculator():
    body = page_head("Free tool","EMI calculator for every loan","Pick a loan type, set the amount, rate and tenure, and see the EMI, interest cost and year wise repayment schedule instantly.",[("Home","index.html"),("EMI Calculator",None)]) + f"""
<section class="section"><div class="wrap">{emi_block(ALL_PRESETS, "home-loan")}
<div class="prose" style="max-width:70ch;margin-top:3rem">
<h2>How EMI is calculated</h2>
<p>EMI = P × r × (1 + r)<sup>n</sup> ÷ ((1 + r)<sup>n</sup> − 1), where P is the loan amount, r is the monthly interest rate (annual rate ÷ 12 ÷ 100) and n is the number of monthly instalments. Early EMIs are mostly interest; later EMIs are mostly principal, which is why prepaying in the first years saves the most.</p>
<h2>Three things the calculator will show you</h2>
<ul><li><b>Tenure is expensive.</b> A ₹30 lakh home loan at 8.6 percent costs about ₹22 lakh in interest over 20 years, but about ₹33 lakh over 30 years, for an EMI that is only ₹3,000 lower.</li>
<li><b>Rate matters more on long loans.</b> Half a percent on a personal loan of 3 years changes the EMI by a few hundred rupees. On a 20 year home loan it changes total interest by over a lakh.</li>
<li><b>Prepayment helps early.</b> Look at the schedule: the balance barely moves in the first years. A lump sum then knocks out far more interest than the same amount paid later.</li></ul>
<p>Results are for planning. The lender's exact EMI may differ slightly because of the disbursal date, pre EMI interest and rounding.</p>
</div></div></section>"""
    page("emi-calculator.html", "EMI Calculator for Home, Personal, Business, Car and Property Loans", "Free EMI calculator with per loan presets, interest breakup and amortisation schedule from Mayan Finserv Solutions.", body)

def build_eligibility():
    body = page_head("Two minute check","Are you eligible for a loan?","Enter your income, existing EMIs and age to get an indicative eligible amount. Then send it to us and we confirm it with the lender.",[("Home","index.html"),("Eligibility",None)]) + f"""
<section class="section"><div class="wrap calc">
  <form id="elig-form" class="form card">
    <div><label for="e-type">Loan type</label><select id="e-type"><option value="home">Home Loan</option><option value="personal">Personal Loan</option><option value="business">Business Loan</option><option value="lap">Loan Against Property</option><option value="car">Car Loan</option></select></div>
    <div class="form-row">
      <div><label for="e-income">Net monthly income (₹)</label><input id="e-income" type="number" min="5000" step="500" value="45000" required><p class="hint">Take home salary, or average monthly profit for business.</p></div>
      <div><label for="e-emi">Existing EMIs per month (₹)</label><input id="e-emi" type="number" min="0" step="500" value="5000"></div>
    </div>
    <div class="form-row">
      <div><label for="e-age">Your age</label><input id="e-age" type="number" min="18" max="70" value="32" required></div>
      <div><label for="e-cibil">CIBIL score (if known)</label><select id="e-cibil"><option>Don't know</option><option>750 and above</option><option>700 – 749</option><option>650 – 699</option><option>Below 650</option><option>No credit history</option></select></div>
    </div>
    <button class="btn btn-primary" type="submit">Check eligibility</button>
    <p class="hint">Nothing is stored. The calculation runs in your browser.</p>
  </form>
  <div>
    <div id="elig-result" class="result" hidden></div>
    <a id="elig-wa" class="btn btn-wa" href="#" target="_blank" rel="noopener" hidden style="margin-top:1rem">{WA_SVG} Send to Mayan Finserv for confirmation</a>
    <div class="card" style="margin-top:1.2rem"><h3>How lenders decide</h3><p style="color:var(--muted);margin:0">Most lenders cap total EMIs at 50 to 60 percent of net income (called FOIR). Tenure is limited by your retirement age. A co-applicant adds their income to yours. Credit score decides the rate and, below 650, whether the file is accepted at all. This checker uses those rules with typical rates; the lender's own policy is final.</p></div>
  </div>
</div></section>"""
    page("eligibility.html", "Loan Eligibility Calculator", "Check your indicative home, personal, business, car or property loan eligibility in two minutes.", body)

def build_apply():
    body = page_head("Apply online","Start your loan application","Two minutes. We call you back within a working hour, understand your need and tell you the lender, rate and documents before anything is filed.",[("Home","index.html"),("Apply",None)]) + f"""
<section class="section"><div class="wrap two-col">
  <div class="card">{enquiry_form("New loan application from website")}</div>
  <div>
    <div class="card"><h3>Prefer to talk?</h3><p style="color:var(--muted)">Call or WhatsApp {SITE['owner']} directly.</p><p><b style="font-size:1.3rem;font-family:var(--font-display)" class="num">{SITE['phone_display']}</b> <button class="btn btn-outline btn-sm" type="button" data-copy="{SITE['phone_display']}">Copy</button></p><p>{SITE['hours']}</p><a class="btn btn-wa" href="https://wa.me/{SITE['whatsapp']}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
    <div class="card" style="margin-top:1.2rem"><h3>Keep these ready</h3><ul class="checks" style="margin:0"><li>PAN and Aadhaar</li><li>Salary slips or ITR</li><li>Six months bank statement</li><li>Property or vehicle papers, if applicable</li></ul></div>
  </div>
</div></section>"""
    page("apply.html", "Apply for a Loan Online", "Apply online for a home, personal, business, property or car loan with Mayan Finserv Solutions, Adoni.", body)

def build_about():
    body = page_head("About us", f"{SITE['brand']}", f"A loan distribution partner in {SITE['city']} that puts the borrower first.",[("Home","index.html"),("About",None)]) + f"""
<section class="section"><div class="wrap two-col">
  <div class="prose">
    <p class="lead" style="color:var(--ink)">{SITE['brand']} was founded by {SITE['owner']} to give families and small businesses in Adoni and the surrounding districts what customers in big cities take for granted: a knowledgeable, independent advisor who compares lenders and stands with the borrower through the whole process.</p>
    <h2>What we do</h2><p>We are a channel partner and referral agent for nationalised banks, private banks, housing finance companies and NBFCs. We assess your profile, pick the lender whose policy fits it, prepare the file the way that lender's credit team expects, follow it through sanction and disbursal, and stay available for everything after: statements, part payments, NOC, closure.</p>
    <h2>What we do not do</h2><ul><li>We do not lend money ourselves or take deposits.</li><li>We do not charge the customer a fee for consultation or file processing. Our income is the payout from the lender on disbursal.</li><li>We do not send your file to multiple lenders at once. One well placed application protects your credit score.</li><li>We do not promise approvals. We tell you the realistic chance and what would improve it.</li></ul>
    <h2>Where we work</h2><p>Our office is on Aspari Road in Adoni. We serve customers across Kurnool, Nandyal, Bellary and Raichur districts with doorstep document collection, and handle files from anywhere in Andhra Pradesh, Telangana and Karnataka over WhatsApp and email.</p>
    <h2>Our commitments</h2><ul class="checks"><li>Written disclosure of the lender's processing fee and all charges before you accept</li><li>Reply to every enquiry within one working hour</li><li>Your documents are shared only with the lender you approve</li><li>Plain language explanation of every clause in the sanction letter</li></ul>
  </div>
  <aside>
    <div class="card"><h3>{SITE['owner']}</h3><p style="color:var(--muted)">Proprietor</p><p>Works directly with branch managers and NBFC credit teams across the region, and personally reviews every file before submission.</p><a class="btn btn-wa" href="https://wa.me/{SITE['whatsapp']}" target="_blank" rel="noopener">{WA_SVG} Message {SITE['owner'].split()[0]}</a></div>
    <div class="card" style="margin-top:1.2rem"><h3>At a glance</h3><dl style="display:grid;grid-template-columns:auto 1fr;gap:.4rem 1rem;margin:0"><dt style="color:var(--muted)">Based in</dt><dd style="margin:0"><b>{SITE['city']}, AP</b></dd><dt style="color:var(--muted)">Partners</dt><dd style="margin:0"><b>{len(BANKS)} banks, {len(NBFCS)} NBFCs</b></dd><dt style="color:var(--muted)">Hours</dt><dd style="margin:0"><b>{SITE['hours']}</b></dd></dl></div>
  </aside>
</div></section>
<section class="section section-alt"><div class="wrap"><div class="section-head center"><div class="eyebrow">Lending partners</div><h2>Who we work with</h2></div>{partners_block()}</div></section>"""
    page("about.html", "About Us", f"About {SITE['brand']}, a loan distribution and advisory partner in Adoni founded by {SITE['owner']}.", body)

def build_blog():
    os.makedirs("blog", exist_ok=True)
    cards = "".join(f"""<a class="card" href="blog/{x['slug']}.html"><span class="pill">{x['cat']}</span><h3>{x['title']}</h3><p style="color:var(--muted);margin:0">{x['summary']}</p><span class="meta">{x['date']}</span></a>""" for x in POSTS)
    body = page_head("Blog","Straight talk about loans and credit","Practical guides written from what we see across hundreds of files every year. No jargon, no sales pitch.",[("Home","index.html"),("Blog",None)]) + f"""<section class="section"><div class="wrap grid grid-2">{cards}</div></section>"""
    page("blog.html", "Blog", "Guides on home loans, credit scores, MSME schemes and car loans from Mayan Finserv Solutions.", body)
    for x in POSTS:
        more = "".join(f'<a href="{y["slug"]}.html">{y["title"]}</a>' for y in POSTS if y is not x)
        body = page_head(x["cat"], x["title"], x["summary"], [("Home","../index.html"),("Blog","../blog.html"),(x["cat"],None)]) + f"""
<section class="section"><div class="wrap two-col">
  <article class="prose" style="max-width:70ch"><p class="article-meta">Published {x['date']} · {SITE['brand']}</p>{x['body']}
  <div class="note" style="margin-top:2rem">Have a question about your own case? <a href="../contact.html">Talk to us</a>, the consultation is free.</div></article>
  <aside><div class="card"><h3>More articles</h3><div style="display:grid;gap:.6rem">{more}</div></div><div class="card" style="margin-top:1.2rem"><h3>Quick enquiry</h3>{enquiry_form("Enquiry from blog: " + x['title'], compact=True)}</div></aside>
</div></section>"""
        # blog pages live one level down: fix relative asset paths
        html_out = head(x["title"], x["summary"], f"blog/{x['slug']}.html") + header() + body + footer()
        html_out = html_out.replace('href="assets/', 'href="../assets/').replace('src="assets/', 'src="../assets/')
        for p in PRODUCTS: html_out = html_out.replace(f'href="{p["slug"]}.html"', f'href="../{p["slug"]}.html"')
        for f_ in ["index","about","emi-calculator","eligibility","blog","careers","branches","faq","contact","apply","privacy-policy","terms","disclaimer"]:
            html_out = html_out.replace(f'href="{f_}.html"', f'href="../{f_}.html"')
        html_out = html_out.replace('href="../../', 'href="../')
        with open(f"blog/{x['slug']}.html", "w", encoding="utf-8") as f: f.write(html_out)
        print("wrote blog/", x["slug"])

def build_careers():
    roles = [("Loan Sales Executive","Adoni / Kurnool","Meet customers, collect documents, coordinate with bank branches. Two wheeler and basic English or Telugu communication required. Freshers with a graduate degree welcome. Fixed salary plus incentives per disbursal."),
             ("Tele Caller and Back Office","Adoni","Handle enquiries on phone and WhatsApp, maintain the lead sheet, prepare document checklists. Comfortable with Excel and Google Sheets. Women candidates encouraged."),
             ("Channel Partner (freelance)","Any town","CAs, tax practitioners, insurance agents and real estate brokers who come across loan requirements. Refer the lead, we do the processing, you earn a payout on every disbursal.")]
    cards = "".join(f'<div class="card"><h3>{t}</h3><span class="pill">{loc}</span><p style="color:var(--muted)">{d}</p><a class="btn btn-wa btn-sm" href="https://wa.me/{SITE["whatsapp"]}?text={html.escape("Hi, I want to apply for the role: " + t).replace(" ", "%20")}" target="_blank" rel="noopener">{WA_SVG} Apply on WhatsApp</a></div>' for t,loc,d in roles)
    body = page_head("Careers","Grow with a growing team","We are hiring in Adoni and the surrounding districts. Send your CV on WhatsApp or email and we will get back within two working days.",[("Home","index.html"),("Careers",None)]) + f"""<section class="section"><div class="wrap"><div class="grid grid-3">{cards}</div><p class="center fineprint" style="margin-top:2rem">Email CVs to <a href="mailto:{SITE['email']}">{SITE['email']}</a> with the role in the subject line.</p></div></section>"""
    page("careers.html", "Careers", f"Job openings at {SITE['brand']}, Adoni: loan sales executive, tele caller and channel partners.", body)

def build_branches():
    areas = ["Adoni","Yemmiganur","Kurnool","Nandyal","Mantralayam","Alur","Aspari","Pattikonda","Bellary","Raichur","Guntakal","Anantapur"]
    chips = "".join(f'<span class="partner">{a}</span>' for a in areas)
    body = page_head("Branches and service areas","Head office in Adoni, service across the region","Visit us on Aspari Road, or ask for doorstep document pickup in any of the towns below.",[("Home","index.html"),("Branches",None)]) + f"""
<section class="section"><div class="wrap two-col">
  <div class="card"><span class="pill">Head office</span><h3>{SITE['city']}</h3><p>{SITE['address']}</p><p><b>Phone:</b> <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a><br><b>Email:</b> <a href="mailto:{SITE['email']}">{SITE['email']}</a><br><b>Hours:</b> {SITE['hours']}</p><div style="display:flex;gap:.7rem;flex-wrap:wrap"><a class="btn btn-outline btn-sm" href="{SITE['maps']}" target="_blank" rel="noopener">Open in Google Maps</a><a class="btn btn-wa btn-sm" href="https://wa.me/{SITE['whatsapp']}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div></div>
  <div><h3>Doorstep service areas</h3><p style="color:var(--muted)">Our executives collect documents and complete verification at your home or business in these towns, usually within 24 hours of your call.</p><div class="partners" style="justify-content:flex-start">{chips}</div><p class="fineprint" style="margin-top:1rem">Outside these towns we process files over WhatsApp, email and courier, across Andhra Pradesh, Telangana and Karnataka.</p></div>
</div></section>"""
    page("branches.html", "Branches and Service Areas", f"{SITE['brand']} head office in Adoni and doorstep loan service across Kurnool, Nandyal, Bellary and Raichur districts.", body)

def build_faq():
    groups = [("General",[("Is Mayan Finserv a bank?","No. We are a loan distribution and referral partner. Loans are sanctioned and disbursed by the bank or NBFC you sign with. We arrange, compare and process."),("What does it cost me?","Nothing. Consultation and processing support are free. Lenders pay us on disbursal. The lender's own processing fee, if any, is disclosed to you before acceptance."),("Is my data safe?","Documents are shared only with the lender you approve, over their official channels. We do not sell or share your data with anyone else. See our privacy policy."),("Do you handle loans outside Adoni?","Yes. Doorstep service in Kurnool, Nandyal, Bellary and Raichur districts, and remote processing anywhere in AP, Telangana and Karnataka.")]),
              ("Eligibility and credit",[("What CIBIL score do I need?","750 and above for the best rates. 700 to 750 is comfortable. 650 to 700 is possible with some NBFCs. Below 650, let us look at the report before applying anywhere."),("I am new to credit. Can I get a loan?","Yes, through secured products (car, home, LAP) or a secured credit card first. Some NBFCs also lend small personal loans on salary credits alone."),("Can I add a co-applicant?","Yes, a spouse, parent or sibling with income increases eligibility. For property loans, all owners must be co-applicants.")]),
              ("Process",[("How long does a loan take?","Personal and car: 1 to 3 days. Home and LAP: 7 to 15 days. Business loans: 3 days to 6 weeks depending on product."),("Do I have to visit the bank?","Usually once, to sign the agreement and for a video or physical KYC. Everything else we handle."),("Can I prepay or close early?","Floating rate loans to individuals have no foreclosure charge on home loans and LAP. Personal and business loans carry 2 to 4 percent. We tell you the exact number before you sign.")])]
    body = page_head("FAQ","Frequently asked questions","Everything customers ask before their first loan, answered plainly.",[("Home","index.html"),("FAQ",None)]) + "<section class='section'><div class='wrap' style='max-width:820px'>" + "".join(f"<h2>{g}</h2>{faq_block(items)}<br>" for g,items in groups) + "</div></section>"
    page("faq.html", "Loan FAQ", "Answers to common questions about loan eligibility, CIBIL, charges and process from Mayan Finserv Solutions.", body)

def build_contact():
    body = page_head("Contact","Talk to us","Call, WhatsApp, email or walk in. We reply to every enquiry within one working hour.",[("Home","index.html"),("Contact",None)]) + f"""
<section class="section"><div class="wrap two-col">
  <div class="card"><h3>Send us a message</h3>{enquiry_form("Contact form message")}</div>
  <div style="display:grid;gap:1.2rem">
    <div class="card"><h3>Phone and WhatsApp</h3><p style="font-family:var(--font-display);font-size:1.4rem;font-weight:800;color:var(--navy);margin:0" class="num">{SITE['phone_display']}</p><p class="fineprint">{SITE['hours']}</p><div style="display:flex;gap:.6rem;flex-wrap:wrap"><a class="btn btn-outline btn-sm" href="tel:{SITE['phone_tel']}">Call</a><a class="btn btn-wa btn-sm" href="https://wa.me/{SITE['whatsapp']}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a><button class="btn btn-outline btn-sm" type="button" data-copy="{SITE['phone_display']}">Copy number</button></div></div>
    <div class="card"><h3>Email</h3><p><a href="mailto:{SITE['email']}">{SITE['email']}</a> <button class="btn btn-outline btn-sm" type="button" data-copy="{SITE['email']}">Copy</button></p></div>
    <div class="card"><h3>Office</h3><p>{SITE['address']}</p><a class="btn btn-outline btn-sm" href="{SITE['maps']}" target="_blank" rel="noopener">Open in Google Maps</a></div>
  </div>
</div></section>"""
    page("contact.html", "Contact Us", f"Contact {SITE['brand']} in Adoni: {SITE['phone_display']}, {SITE['email']}, {SITE['address']}.", body)

def build_legal():
    privacy = f"""<h2>Who we are</h2><p>{SITE['brand']} ("we"), {SITE['address']}, operates {SITE['domain']} and provides loan distribution and referral services.</p>
<h2>What this website collects</h2><p>The website itself does not store form submissions. When you use our enquiry forms, the details you enter are composed into a WhatsApp message on your device and sent to our business number only when you press send. Calculators run in your browser and send nothing.</p><p>Our hosting provider may log standard technical information (IP address, browser, pages visited) for security. If we add analytics, this policy will be updated.</p>
<h2>Information you share with us directly</h2><p>To process a loan we collect identity, income, bank, property or vehicle documents from you on WhatsApp, email or in person. We use them only to assess your requirement and submit your application to the lender you approve.</p>
<h2>Sharing</h2><p>Your documents are shared with the specific bank or NBFC you agree to apply with, through their official channels, and with credit bureaus as required by the lender for your application. We do not sell or rent your information. We do not share it with other lenders without your consent.</p>
<h2>Retention</h2><p>We retain application documents for as long as needed to complete the transaction and to meet the lender's or regulator's requirements, after which they are deleted or returned on request.</p>
<h2>Your rights</h2><p>You may ask us at any time what information we hold about you, request corrections, or ask us to delete records not required by law. Write to {SITE['email']}.</p>
<h2>Contact</h2><p>{SITE['owner']}, {SITE['brand']}, {SITE['address']}. Phone {SITE['phone_display']}.</p>"""
    terms = f"""<h2>Nature of service</h2><p>{SITE['brand']} is a loan distribution, referral and facilitation service. We are not a bank, NBFC or lender, and we do not accept deposits or disburse loans. All loans are provided by the respective lending institution under its own terms.</p>
<h2>No guarantee of approval</h2><p>Eligibility, sanction, interest rate, tenure and fees are determined solely by the lender. Any figure shown on this website, including calculator results and rate ranges, is indicative and not an offer.</p>
<h2>Fees</h2><p>We do not charge borrowers a fee for consultation or processing support unless agreed in writing in advance. Lender charges such as processing fees, legal and valuation charges and stamp duty are payable to the lender or the relevant authority and are disclosed before you accept a sanction.</p>
<h2>Your responsibilities</h2><p>You agree that documents and information you provide are true and complete. Furnishing false information to a lender is an offence and may result in rejection or recall of the loan.</p>
<h2>Website content</h2><p>Content is for general information and may change without notice. Bank and NBFC names and marks belong to their respective owners and are used only to identify the institutions whose products we distribute.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, we are not liable for any loss arising from reliance on website content, lender decisions, or delays outside our control.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of India. Courts at Kurnool, Andhra Pradesh have jurisdiction.</p>"""
    disc = f"""<p>{SITE['brand']} acts as a channel partner, direct selling agent or referral agent for banks, housing finance companies and NBFCs. We do not lend. Loan products described on this website are offered by the respective lenders and are subject to their credit policy, documentation and approval.</p>
<p>Interest rates, loan amounts, tenures and fees mentioned are indicative ranges observed across our partner lenders at the time of publishing and may change without notice. Calculator outputs are estimates for planning only.</p>
<p>Customer testimonials reflect individual experiences and do not guarantee similar outcomes. Figures such as amounts disbursed and customers served are approximate and updated periodically.</p>
<p>Never pay any advance fee in cash to anyone claiming to represent {SITE['brand']} or a lender for guaranteed approval. Our official contact numbers are listed on this website. Report suspicious calls to {SITE['phone_display']}.</p>"""
    for slug, title, lead, content in [("privacy-policy","Privacy Policy","How we handle your information.",privacy),("terms","Terms of Use","The basis on which we provide our service and this website.",terms),("disclaimer","Disclaimer","Please read before relying on any information on this website.",disc)]:
        body = page_head("Legal", title, lead, [("Home","index.html"),(title,None)]) + f"<section class='section'><div class='wrap prose' style='max-width:76ch'><p class='article-meta'>Last updated: September 2026</p>{content}</div></section>"
        page(f"{slug}.html", title, lead, body)

def build_misc():
    import shutil; shutil.copy("/home/claude/logo/kit/favicon.svg","assets/favicon.svg")
    pages = ["index","home-loan","personal-loan","business-loan","loan-against-property","car-loan","credit-cards","emi-calculator","eligibility","apply","about","blog","careers","branches","faq","contact","privacy-policy","terms","disclaimer"] + [f"blog/{x['slug']}" for x in POSTS]
    urls = "".join(f"<url><loc>{SITE['url']}/{'' if p=='index' else p+'.html'}</loc></url>" for p in pages)
    with open("sitemap.xml","w") as f: f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    with open("robots.txt","w") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n")
    with open("404.html","w",encoding="utf-8") as f:
        f.write(head("Page not found","Page not found","404.html") + header() + "<section class='section center'><div class='wrap'><h1>Page not found</h1><p class='lead'>The link may be old. Try the home page or the loan products menu.</p><a class='btn btn-primary' href='index.html'>Go home</a></div></section>" + footer())

if __name__ == "__main__":
    build_index(); build_products(); build_calculator(); build_eligibility(); build_apply()
    build_about(); build_blog(); build_careers(); build_branches(); build_faq(); build_contact(); build_legal(); build_misc()
