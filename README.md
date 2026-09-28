# Mayan Finserv Solutions website

Static HTML/CSS/JS site for mayanfinserv.com. No backend, no database, no build tools needed for hosting.

## Hosting
Upload everything in this folder (all .html files, `assets/`, `blog/`, `sitemap.xml`, `robots.txt`, `404.html`) to the web root (`public_html`) of any hosting: Hostinger, GoDaddy, cPanel, Netlify, Cloudflare Pages, GitHub Pages. Point mayanfinserv.com to it and enable HTTPS. Done.

## Pages
- index.html (home with quick EMI, products, process, partners, testimonials, FAQ, call back form, blog teasers)
- home-loan, personal-loan, business-loan, loan-against-property, car-loan, credit-cards (each with features, eligibility, documents, FAQ, enquiry form and a preset EMI calculator)
- emi-calculator.html (all loan presets, doughnut chart, year wise amortisation)
- eligibility.html (FOIR based indicative eligibility)
- apply.html, about.html, blog.html + blog/ (4 articles), careers.html, branches.html, faq.html, contact.html
- privacy-policy.html, terms.html, disclaimer.html, 404.html

## How leads reach the client
Every form builds a WhatsApp message and opens wa.me/919985900483. Nothing is stored on the site. The floating green button and all "WhatsApp" buttons go to the same number.

## Changing brand name, number, address, partners, figures
All of it is in the `SITE`, `BANKS`, `NBFCS`, `PRODUCTS`, `POSTS` and `TESTIMONIALS` blocks at the top of `build.py`. Edit, then run `python3 build.py` to regenerate every page. If Python is not available, do a find and replace across the .html files instead.

## Before go-live (client to confirm)
1. Brand name and tagline (currently "Mayan Finserv Solutions", "Your Funding Partner").
2. Trust strip figures on the home page are illustrative (₹120 Cr+, 3,500+, 25+, 48 hrs). Replace with real numbers or remove.
3. Testimonials are sample text. Replace with real customer quotes (with consent) or remove.
4. Partner bank and NBFC names: keep only institutions the client is actually empanelled with.
5. Interest rate ranges on product pages: review against current lender rate cards.
6. Add a logo image if one exists (replace the inline SVG mark in `build.py` LOGO_SVG, or drop a PNG into assets/ and reference it).
7. If a Google Business Profile exists, update the `maps` link in `build.py`.
8. Consider adding Google Analytics or Meta Pixel snippets in `head()` in build.py, and update the privacy policy accordingly.

## Regulatory note
The site describes the business as a loan distribution/referral service and not a lender (footer, About, Terms, Disclaimer). Keep that wording; RBI rules require DSAs to not present themselves as lenders. Confirm whether the client holds any DSA/channel partner agreements that require displaying a registration or partner code.
