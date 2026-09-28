#!/usr/bin/env python3
"""Builds the Prakash S. Jain & Co. site as static, crawlable HTML.

Every page is real HTML with its own title, description, canonical URL,
Open Graph tags and schema.org JSON-LD, so Google and AI answer engines can
read it without running JavaScript.  Run:  python3 build.py
"""
import html, json, os, pathlib, datetime

# ------------------------------------------------------------------ settings
SITE = "https://prekshabarjatya.github.io/ca-site"   # live on GitHub Pages; change when a custom domain is set up
FIRM = "Prakash S. Jain & Co."
FIRM_LONG = "Prakash S. Jain & Co., Chartered Accountants"
PARTNER = "CA Shreya Jain"
PHONE_DISPLAY = "+91 98260 52751"
PHONE_E164 = "+919826052751"
STREET = "319/320, Manas Bhavan, R.N.T. Marg"
CITY, REGION, PIN, COUNTRY = "Indore", "Madhya Pradesh", "452001", "IN"
MAPS = "https://www.google.com/maps/search/?api=1&query=Manas+Bhavan+R.N.T.+Marg+Indore+452001"
LINKEDIN = "https://www.linkedin.com/in/c-a-c-s-llb-fafd-shreya-jain-67a56a8/"
YEARS = "39+"
TODAY = datetime.date.today().isoformat()

ROOT = pathlib.Path(__file__).parent

# Two versions share one design: "firm" (Prakash S. Jain & Co.) and
# "shreya" (CA Shreya Jain's personal practice site).  python3 build.py shreya
import sys, shutil
VARIANT = sys.argv[1] if len(sys.argv) > 1 else "firm"
SHREYA = VARIANT == "shreya"
OUT = ROOT / "shreya-site" if SHREYA else ROOT
if SHREYA: SITE += "/shreya-site"
ABOUT = "/about/" if SHREYA else "/ca-shreya-jain/"
BRAND = "CA SHREYA JAIN" if SHREYA else "PRAKASH S. JAIN &amp; CO."
BRAND_SUB = "CA · CS · LL.B. · FAFD" if SHREYA else "CHARTERED ACCOUNTANTS"
ABOUT_LABEL = "About" if SHREYA else "Meet CA Shreya Jain"
SVC_LABEL = "Practice Areas" if SHREYA else "Services"
SITE_NAME = "CA Shreya Jain" if SHREYA else "Prakash S. Jain & Co."
SPRITE = (ROOT / "src/sprite.html").read_text()
esc = html.escape

# ------------------------------------------------------------------ content
SERVICES = [
  dict(id="income-tax", icon="i-tax", name="Income Tax Compliance",
    title="Income Tax Return Filing & Tax Audit in Indore",
    short="Corporate and personal tax returns, advance tax, TDS and tax audit for individuals, firms and companies.",
    intro="We prepare and file income tax returns for individuals, Hindu undivided families, partnership firms, LLPs and companies in Indore, and work out advance tax through the year so there is no interest under Sections 234B and 234C.",
    cover=["ITR preparation and filing (ITR-1 to ITR-7)", "Corporate tax computation and MAT", "Tax audit under Section 44AB (Form 3CA / 3CB / 3CD)", "TDS and TCS returns", "Capital gains on property, shares and mutual funds"],
    docs=["PAN and Aadhaar", "Form 16 / 16A, Form 26AS and AIS", "Bank statements and interest certificates", "Capital gains statements", "Audited accounts, for businesses"],
    faq=[("What is the last date to file an income tax return?", "For individuals and businesses that do not need an audit, the due date is usually 31 July after the financial year ends. Taxpayers who need a tax audit have until 31 October. The government sometimes extends these dates, so confirm the current deadline before filing."),
         ("Who needs a tax audit under Section 44AB?", "A business needs a tax audit when its turnover is above ₹1 crore, or above ₹10 crore when cash receipts and payments are each within 5% of the total. A professional needs one when gross receipts are above ₹50 lakh. Other cases can also apply, so we check each client's position.")]),
  dict(id="assessments-appeals", icon="i-appeal", name="Assessments & Appeals",
    title="Income Tax Notices, Assessments & Appeals in Indore",
    short="Replies to notices, scrutiny and faceless assessments, and appeals before CIT(A) and the Income Tax Appellate Tribunal.",
    intro="A notice is easier to handle in its first week than in its last. We read the notice, gather the evidence the department needs and draft a reply that answers the actual question. When an order goes against the client, we take it to appeal before the Commissioner (Appeals) and the Income Tax Appellate Tribunal.",
    cover=["Notices under Sections 139(9), 143(1), 143(2) and 148", "Scrutiny and faceless assessments", "Rectification under Section 154", "Appeals before CIT(A) and ITAT", "Stay of demand and penalty proceedings"],
    docs=["The notice or order received", "Returns and computations for the year", "Books of account and supporting vouchers", "Earlier correspondence with the department"],
    faq=[("I have received an income tax notice. What should I do?", "Do not ignore it. Note the response date on the notice, then share it with us along with the return for that year. Most notices ask for an explanation or documents, and a timely, well-supported reply usually closes the matter."),
         ("How long do I have to file an appeal against an assessment order?", "An appeal to the Commissioner of Income Tax (Appeals) is generally due within 30 days of receiving the order. An appeal to the Income Tax Appellate Tribunal is generally due within two months of the CIT(A) order.")]),
  dict(id="tax-planning-foreign-tax", icon="i-nri", name="Tax Planning & Foreign Tax",
    title="Tax Planning, NRI & Foreign Tax Advisory in Indore",
    short="Tax planning for domestic and foreign clients, DTAA relief, residential status and certification of foreign remittances.",
    intro="Good tax planning happens before the year ends, not while the return is being filed. We look at how income is earned and held, and advise domestic and foreign clients on arrangements that stay within the law, including relief under India's Double Taxation Avoidance Agreements.",
    cover=["Tax planning for individuals, families and companies", "Residential status and NRI taxation", "DTAA relief and foreign tax credit (Form 67)", "Form 15CA / 15CB for foreign remittances", "Lower or nil TDS certificates"],
    docs=["Passport with travel dates, for NRIs", "Details of foreign income and taxes paid abroad", "Tax Residency Certificate", "Investment and property details"],
    faq=[("Does an NRI need to file an income tax return in India?", "Yes, if the NRI's total income earned in India, such as rent, interest or capital gains, is above the basic exemption limit, or if they want to claim a refund of excess TDS."),
         ("What is Form 15CB?", "Form 15CB is a certificate from a Chartered Accountant confirming the tax position on a payment being sent outside India. Banks ask for it along with Form 15CA before making many foreign remittances.")]),
  dict(id="company-incorporation-secretarial", icon="i-company", name="Company Incorporation & Secretarial",
    title="Company Registration & ROC Compliance in Indore",
    short="Company and LLP incorporation, ROC annual filings, board and shareholder compliance and changes in directors or capital.",
    intro="With both Chartered Accountant and Company Secretary qualifications in the firm, we can set up a company and then keep it compliant: statutory registers, board minutes and the annual filings with the Ministry of Corporate Affairs.",
    cover=["Private limited company, OPC and LLP incorporation", "AOC-4, MGT-7 / MGT-7A and LLP Forms 8 and 11", "DIR-3 KYC for directors", "Changes in directors, registered office and share capital", "Strike-off and closure of companies and LLPs"],
    docs=["Directors' PAN, Aadhaar and photographs", "Proof of registered office", "Proposed names and business objects", "Board and AGM minutes, for existing companies"],
    faq=[("How long does it take to register a private limited company?", "Once documents are ready, incorporation through the MCA SPICe+ form usually takes one to two weeks, depending on name approval and how quickly the Registrar processes the application."),
         ("What annual filings does a private limited company have?", "Every company files its financial statements in Form AOC-4 and its annual return in Form MGT-7 or MGT-7A with the Registrar of Companies, and each director completes DIR-3 KYC. Income tax and GST filings are separate.")]),
  dict(id="rbi-fema-compliance", icon="i-rbi", name="RBI & FEMA Compliance",
    title="RBI & FEMA Compliance for Foreign Investment",
    short="Foreign investment reporting, overseas investment, ECB and the RBI filings that follow when money crosses borders.",
    intro="Late reporting to the Reserve Bank of India leads to compounding and penalties. We track every foreign inflow and outflow for our clients and file the returns the RBI expects under the Foreign Exchange Management Act, on time.",
    cover=["FDI reporting in Forms FC-GPR and FC-TRS", "Annual Return on Foreign Liabilities and Assets (FLA)", "Overseas Direct Investment filings", "External commercial borrowings", "Compounding of contraventions"],
    docs=["Share allotment or transfer documents", "Foreign inward remittance certificates (FIRC)", "Valuation report", "KYC of the foreign investor"],
    faq=[("When must FC-GPR be filed?", "A company must report the issue of shares to a foreign investor in Form FC-GPR within 30 days of allotment, through the RBI's FIRMS portal."),
         ("Who must file the FLA return?", "Indian companies and LLPs that have received foreign direct investment or made overseas direct investment must file the FLA return with the RBI by 15 July every year.")]),
  dict(id="forensic-audit", icon="i-forensic", name="Forensic Audit",
    title="Forensic Audit & Fraud Investigation in Indore",
    short="Investigation of suspected fraud, diversion of funds and accounting irregularities, with reports that can stand in a dispute.",
    intro="When the numbers do not add up, a forensic audit finds out why. Using the methods of ICAI's Forensic Accounting and Fraud Detection (FAFD) course, we trace transactions, test controls and write reports for management, lenders or courts.",
    cover=["Fraud and misappropriation investigations", "Forensic audits for banks and lenders", "Fund diversion and related-party reviews", "Partner and shareholder disputes", "Internal control reviews"],
    docs=["Books of account and bank statements", "Relevant agreements and approvals", "Details of the concern or complaint"],
    faq=[("How is a forensic audit different from a statutory audit?", "A statutory audit gives an opinion on whether the financial statements are true and fair. A forensic audit investigates specific transactions or suspicions in detail, to find out what happened and produce evidence that can be used in a dispute or legal proceeding."),
         ("What is FAFD?", "FAFD is the Certificate Course on Forensic Accounting and Fraud Detection run by the Institute of Chartered Accountants of India. It trains Chartered Accountants in investigation, data analysis and evidence handling.")]),
  dict(id="audit-assurance", icon="i-audit", name="Audit & Assurance",
    title="Statutory Audit & Tax Audit Services in Indore",
    short="Statutory audit of companies, tax audit, and audits of trusts, societies and firms.",
    intro="We plan each audit around the real risks in the business, such as stock, receivables and related-party dealings, so the report tells owners and lenders something useful.",
    cover=["Statutory audit under the Companies Act, 2013", "Tax audit and Form 3CA / 3CB / 3CD", "Audit of trusts and societies", "Internal and stock audits"],
    docs=["Trial balance and ledgers", "Bank statements and reconciliations", "Stock statements", "Fixed asset register"],
    faq=[("Does every private limited company need an audit?", "Yes. Every company registered under the Companies Act, 2013 must have its financial statements audited by a Chartered Accountant each year, whatever its turnover.")]),
  dict(id="gst", icon="i-gst", name="GST",
    title="GST Registration, Returns & Notices in Indore",
    short="Registration, returns, input tax credit reconciliation, annual returns and replies to department notices.",
    intro="We reconcile purchases with GSTR-2B every month, file returns on time and keep a clean record for the annual return and any later enquiry from the department.",
    cover=["GST registration and amendments", "GSTR-1 and GSTR-3B filing", "Input tax credit reconciliation", "GSTR-9 and GSTR-9C annual returns", "Notices and appeals"],
    docs=["Sales and purchase registers", "GSTR-2B for the period", "Debit and credit notes"],
    faq=[("When are GSTR-1 and GSTR-3B due?", "For monthly filers, GSTR-1 is due on the 11th and GSTR-3B on the 20th of the following month. Businesses in the quarterly QRMP scheme follow different dates.")]),
]

HOME_FAQ = [
  ("Which Chartered Accountant firm in Indore handles income tax appeals?",
   f"{FIRM} has been in practice in Indore for more than 39 years. Partner {PARTNER} (CA, CS, LL.B., FAFD) handles income tax assessments and appeals before the Commissioner (Appeals) and the Income Tax Appellate Tribunal."),
  ("What services does Prakash S. Jain & Co. offer?",
   "Income tax compliance, income tax assessments and appeals, tax planning and foreign tax advisory, company incorporation and secretarial work, RBI and FEMA compliance, forensic audit, audit and assurance, and GST."),
  ("Where is the office of Prakash S. Jain & Co.?",
   f"The office is at {STREET}, {CITY}, {REGION} {PIN}. You can reach it by phone at {PHONE_DISPLAY}."),
  ("Does the firm work with NRIs and foreign clients?",
   "Yes. The firm advises domestic and foreign clients on tax planning, NRI taxation, DTAA relief, Form 15CA / 15CB and RBI / FEMA compliance for foreign investment."),
  ("What qualifications does CA Shreya Jain hold?",
   "CA Shreya Jain is a Chartered Accountant (ICAI), a Company Secretary (ICSI), holds a Bachelor of Laws (LL.B.) and has completed ICAI's Forensic Accounting and Fraud Detection (FAFD) certification."),
]

DATES = [
  ("2026-09-30", "Tax audit report (Form 3CD) and DIR-3 KYC"),
  ("2026-10-07", "TDS / TCS deposit for September"),
  ("2026-10-11", "GSTR-1 for September"),
  ("2026-10-20", "GSTR-3B for September"),
  ("2026-10-31", "Income tax return for audit cases"),
  ("2026-12-15", "Third instalment of advance tax (75%)"),
]

# ------------------------------------------------------------------ schema
ADDRESS = {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
           "addressRegion": REGION, "postalCode": PIN, "addressCountry": COUNTRY}
FIRM_ID, PERSON_ID, SITE_ID = SITE + "/#firm", SITE + "/#shreya-jain", SITE + "/#website"

def firm_schema():
    return {
      "@type": ["AccountingService", "ProfessionalService"], "@id": FIRM_ID,
      "name": FIRM, "alternateName": ["Prakash S Jain and Co", "Prakash S. Jain & Co. Chartered Accountants", "PSJ & Co."],
      "description": f"{FIRM} is a Chartered Accountant firm in Indore, Madhya Pradesh, in practice for more than 39 years, offering income tax compliance, assessments and appeals, tax planning, company incorporation, RBI compliance and forensic audit.",
      "url": None if SHREYA else SITE + "/", "telephone": PHONE_E164, "address": ADDRESS, "hasMap": MAPS,
      "areaServed": [{"@type": "City", "name": "Indore"}, {"@type": "State", "name": "Madhya Pradesh"}, {"@type": "Country", "name": "India"}],
      "logo": SITE + "/assets/logo.svg", "image": SITE + "/assets/og.png",
      "employee": {"@id": PERSON_ID}, "founder": None,
      "knowsAbout": ["Income tax", "Income tax appeals", "Corporate tax", "Foreign tax", "DTAA", "Company secretarial work", "RBI compliance", "FEMA", "Forensic audit", "GST", "Statutory audit", "Tax audit"],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE}/services/{s['id']}/"}} for s in SERVICES]},
    }

def person_schema():
    return {
      "@type": "Person", "@id": PERSON_ID, "name": "Shreya Jain", "honorificPrefix": "CA",
      "jobTitle": "Partner", "worksFor": {"@id": FIRM_ID},
      "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "Chartered Accountant", "credentialCategory": "Professional qualification", "recognizedBy": {"@type": "Organization", "name": "The Institute of Chartered Accountants of India"}},
        {"@type": "EducationalOccupationalCredential", "name": "Company Secretary", "credentialCategory": "Professional qualification", "recognizedBy": {"@type": "Organization", "name": "The Institute of Company Secretaries of India"}},
        {"@type": "EducationalOccupationalCredential", "name": "Bachelor of Laws (LL.B.)", "credentialCategory": "Degree"},
        {"@type": "EducationalOccupationalCredential", "name": "Forensic Accounting and Fraud Detection (FAFD)", "credentialCategory": "Certificate", "recognizedBy": {"@type": "Organization", "name": "The Institute of Chartered Accountants of India"}}],
      "knowsAbout": ["Income Tax", "Appeals", "Company Secretarial Work", "Corporate Tax", "Foreign Tax", "RBI Compliance", "Forensic Audit"],
      "alumniOf": {"@type": "EducationalOrganization", "name": "St. Paul's Convent School, Indore"},
      "address": ADDRESS, "sameAs": [LINKEDIN], "url": SITE + ("/" if SHREYA else ABOUT), "telephone": PHONE_E164,
    }

def website_schema():
    return {"@type": "WebSite", "@id": SITE_ID, "url": SITE + "/", "name": SITE_NAME, "inLanguage": "en-IN", "publisher": {"@id": PERSON_ID if SHREYA else FIRM_ID}}

def crumbs_schema(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}

def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def clean(o):
    if isinstance(o, dict): return {k: clean(v) for k, v in o.items() if v is not None}
    if isinstance(o, list): return [clean(v) for v in o]
    return o

# ------------------------------------------------------------------ templates
def ico(i): return f'<svg viewBox="0 0 48 48" aria-hidden="true"><use href="#{i}"/></svg>'
LOGO = '<svg viewBox="0 0 100 60" aria-hidden="true"><use href="#logo"/></svg>'

def head(title, desc, path, graph, og_type="website"):
    url = SITE + path
    ld = json.dumps(clean({"@context": "https://schema.org", "@graph": graph}), ensure_ascii=False, indent=1)
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="{esc(FIRM_LONG)}">
<meta name="geo.region" content="IN-MP">
<meta name="geo.placename" content="Indore">
<meta name="theme-color" content="#2f3f73">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(FIRM)}">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/og.png">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Lato:wght@400;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{ld}
</script>
</head>
'''

def header(active):
    on = lambda k: ' class="on" aria-current="page"' if k == active else ''
    menu = "".join(f'<a href="/services/{s["id"]}/">{esc(s["name"])}</a>' for s in SERVICES)
    dsvc = "".join(f'<a class="sub" href="/services/{s["id"]}/">{esc(s["name"])}</a>' for s in SERVICES)
    return f'''<a class="skip" href="#content">Skip to content</a>
{SPRITE}<header class="hdr" id="hdr">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{esc(SITE_NAME)} home">
      <span class="disc">{LOGO}</span>
      <span class="name">{BRAND}<small>{BRAND_SUB}</small></span>
    </a>
    <nav class="main" aria-label="Main">
      <a href="/" class="home{' on' if active=='home' else ''}" aria-label="Home"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l9 8h-3v9h-5v-6h-2v6H6v-9H3z"/></svg></a>
      <a href="{ABOUT}"{on('about')}>{ABOUT_LABEL}</a>
      <div class="dd"><a href="/services/"{on('services')}>{SVC_LABEL}</a><div class="menu">{menu}</div></div>
      <a href="/contact/"{on('contact')}>Contact</a>
      <a class="tel" href="tel:{PHONE_E164}"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ph"/></svg>{PHONE_DISPLAY}</a>
    </nav>
    <button class="burger" id="burger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <button class="x" id="closeDrawer" aria-label="Close menu">×</button>
  <a href="/">Home</a><a href="{ABOUT}">{ABOUT_LABEL}</a><a href="/services/">{SVC_LABEL}</a>{dsvc}<a href="/contact/">Contact</a>
  <a class="sub" href="tel:{PHONE_E164}" style="margin-top:14px">{PHONE_DISPLAY}</a>
</div>
'''

FOOTER = f'''<footer>
  <div class="wrap">
    <div class="top">
      <div class="mark">{LOGO}</div>
      <div>
        <h2 class="h4">{("CA Shreya Jain · Partner, " + esc(FIRM)) if SHREYA else esc(FIRM_LONG)}</h2>
        <address><ul>
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#pin"/></svg>{esc(STREET)}, {CITY}, {REGION} {PIN}</li>
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ph"/></svg><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></li>
        </ul></address>
      </div>
      <div class="disc">
        <h2 class="h5">Disclaimer</h2>
        <p>This website follows the guidelines of the Institute of Chartered Accountants of India. It shares information about the firm and is not an advertisement or solicitation. Nothing here is professional advice; please consult us about your specific situation.</p>
      </div>
    </div>
    <div class="rule"></div>
    <div class="bottom">
      <span>© {datetime.date.today().year} {esc(SITE_NAME)}<span class="sep">|</span><a href="/services/" style="margin:0">Services</a><span class="sep">|</span><a href="/contact/" style="margin:0">Contact</a></span>
      <span>Chartered Accountants · Indore, Madhya Pradesh</span>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''

def page(title, desc, path, graph, active, body, inner=True):
    return head(title, desc, path, graph) + f'<body class="{"inner" if inner else "home"}">\n' + header(active) + f'<main id="content">\n{body}\n</main>\n' + FOOTER

def banner(h1, trail):
    items = []
    for i, (n, u) in enumerate(trail):
        last = i == len(trail) - 1
        items.append(f'<li><b aria-current="page">{esc(n)}</b></li>' if last else f'<li><a href="{u}">{esc(n)}</a></li>')
    return f'''<div class="jaali banner"><div class="wrap"><h1>{h1}</h1></div></div>
<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>{"".join(items)}</ol></div></nav>'''

def side(active=None):
    cur = ' class="on" aria-current="page"'
    return "".join(f'<a href="/services/{s["id"]}/"{cur if s["id"]==active else ""}><span class="dot">{ico(s["icon"])}</span>{esc(s["name"])}</a>' for s in SERVICES)

def faq_html(faq, h="Frequently Asked Questions", tag="section", cls="faq"):
    qs = "".join(f'<details{" open" if i==0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(faq))
    return f'<{tag} class="{cls}" aria-labelledby="faq-h"><div class="wrap"><h2 id="faq-h">{h}</h2>{qs}</div></{tag}>'

# ------------------------------------------------------------------ pages
def home():
    mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    dates = "".join(f'<div class="date" data-date="{d}"><b><time datetime="{d}">{int(d[8:])} {mon[int(d[5:7])-1]}</time></b><small>{mon[int(d[5:7])-1]} {d[:4]}</small><span>{esc(t)}</span></div>' for d, t in DATES)
    car = "".join(f'<a class="svc{" feat" if i==1 else ""}" href="/services/{s["id"]}/"><span class="ring"><svg class="deco" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco-ring"/></svg>{ico(s["icon"])}</span><span>{esc(s["name"])}</span></a>' for i, s in enumerate(SERVICES))
    body = f'''<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <h1 id="h1"><span class="kicker">Chartered Accountants in Indore · {YEARS} Years</span><span class="line">Clear Books, Sound <em>Advice</em> and Returns <em>Filed on Time</em></span></h1>
    <div class="mandala" aria-hidden="true"><canvas id="mandala"></canvas><div class="core">{LOGO}</div></div>
  </div>
  <span class="scroll" aria-hidden="true"></span>
</section>

<section class="facts" aria-label="Firm at a glance"><div class="wrap"><dl>
  <div><dt>In practice</dt><dd>{YEARS} years in Indore</dd></div>
  <div><dt>Partner</dt><dd>CA Shreya Jain, CA · CS · LL.B. · FAFD</dd></div>
  <div><dt>Clients</dt><dd>Individuals, companies and foreign clients</dd></div>
  <div><dt>Office</dt><dd>Manas Bhavan, R.N.T. Marg, Indore</dd></div>
</dl></div></section>

<section class="intro">
  <div class="wrap">
    <div>
      <h2>Chartered Accountants Based in Indore, Madhya Pradesh.<br>Serving Domestic &amp; Foreign Clients</h2>
      <p>{esc(FIRM)} is one of the oldest Chartered Accountant firms in Indore, in practice for more than 39 years. The firm looks after taxation, audit and compliance for individuals, businesses and companies, and advises both domestic and foreign clients.</p>
    </div>
    <div class="col2">
      <p>The work covers corporate and personal tax compliance, <a href="/services/assessments-appeals/">income tax assessments and appeals</a>, <a href="/services/tax-planning-foreign-tax/">tax planning and foreign tax</a>, <a href="/services/company-incorporation-secretarial/">company incorporation and secretarial matters</a>, <a href="/services/rbi-fema-compliance/">RBI compliances</a> and <a href="/services/forensic-audit/">forensic audit</a>, so a client can take tax, law and company matters to one office.</p>
      <p>Partner <a href="{ABOUT}">CA Shreya Jain</a> (CA, CS, LL.B., FAFD) has been with the firm since 2016 and leads its income tax, appeals, corporate tax and foreign tax work.</p>
    </div>
  </div>
</section>

<section class="carousel" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 id="svc-h" class="sr">Our Services</h2>
    <div class="car">
      <button class="arrow" id="prev" aria-label="Previous services"><svg viewBox="0 0 24 24"><path d="M17 4L5 12l12 8z"/></svg></button>
      <div class="track" id="track">{car}</div>
      <button class="arrow" id="next" aria-label="Next services"><svg viewBox="0 0 24 24"><path d="M7 4l12 8-12 8z"/></svg></button>
    </div>
    <a class="btn" href="/services/">View All Services</a>
  </div>
</section>

<section class="why" aria-labelledby="why-h">
  <canvas id="lake" aria-hidden="true"></canvas>
  <div class="wrap">
    <div>
      <h2 id="why-h">Why Choose Us</h2>
      <p>For almost four decades, families and businesses in Indore have brought their accounts, returns and tax disputes to {esc(FIRM)}.</p>
      <p>With chartered accountancy, company secretarial practice and law under one roof, a tax question that turns into a company-law question or an appeal stays with the people who already know the file.</p>
      <a class="btn light" href="{ABOUT}">Meet CA Shreya Jain</a>
    </div>
    <ul>
      <li><i aria-hidden="true">✓</i><span>More than 39 years in practice in Indore, with partner-level attention on every engagement.</span></li>
      <li><i aria-hidden="true">✓</i><span>CA, CS and LL.B. qualifications in one team for tax, company law and legal representation.</span></li>
      <li><i aria-hidden="true">✓</i><span>Representation in income tax assessments and appeals, from notice to hearing.</span></li>
      <li><i aria-hidden="true">✓</i><span>Tax planning for domestic and foreign clients, including RBI and FEMA compliance.</span></li>
      <li><i aria-hidden="true">✓</i><span>Forensic audit and fraud investigation backed by ICAI's FAFD qualification.</span></li>
    </ul>
  </div>
</section>

<section class="who" aria-label="Who we work with">
  <div class="wrap grid">
    <div class="box"><div><h3>Businesses &amp; Companies</h3><ul><li>Corporate tax compliance</li><li>Statutory and tax audit</li><li>Company incorporation</li><li>Company secretarial work</li><li>Forensic audit</li></ul></div></div>
    <div class="box"><div><h3>Individuals &amp; Families</h3><ul><li>Personal tax returns</li><li>Tax planning</li><li>Capital gains</li><li>Assessments and notices</li><li>Appeals before CIT(A) and ITAT</li></ul></div></div>
    <div class="box"><div><h3>Foreign Clients &amp; NRIs</h3><ul><li>Foreign tax and DTAA relief</li><li>RBI / FEMA compliance</li><li>FDI and ODI reporting</li><li>Form 15CA / 15CB</li><li>Setting up in India</li></ul></div></div>
  </div>
</section>

<section class="cal" aria-labelledby="cal-h">
  <div class="wrap">
    <div class="head"><h2 id="cal-h">Upcoming Tax &amp; Compliance Due Dates</h2><span class="note">Statutory dates for FY 2026–27. Check for government extensions before relying on them.</span></div>
    <div class="dates">{dates}</div>
  </div>
</section>

{faq_html(HOME_FAQ)}

<section class="badges jaali-dark" aria-label="Credentials">
  <div class="wrap">
    <div class="seal"><svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="27" fill="none" stroke="#c9bd93" stroke-width="1.5"/><circle cx="30" cy="30" r="22" fill="none" stroke="#c9bd93" stroke-dasharray="2 3"/><text x="30" y="35" text-anchor="middle" font-family="Quicksand" font-weight="700" font-size="14" fill="#fff">ICAI</text></svg><div><b>Member Firm</b><small>Chartered Accountants</small></div></div>
    <div class="seal"><svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="27" fill="none" stroke="#c9bd93" stroke-width="1.5"/><circle cx="30" cy="30" r="22" fill="none" stroke="#c9bd93" stroke-dasharray="2 3"/><text x="30" y="35" text-anchor="middle" font-family="Quicksand" font-weight="700" font-size="11" fill="#fff">CA · CS</text></svg><div><b>CA · CS · LL.B. · FAFD</b><small>Partner qualifications</small></div></div>
    <div class="seal"><svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="27" fill="none" stroke="#c9bd93" stroke-width="1.5"/><circle cx="30" cy="30" r="22" fill="none" stroke="#c9bd93" stroke-dasharray="2 3"/><text x="30" y="35" text-anchor="middle" font-family="Quicksand" font-weight="700" font-size="14" fill="#fff">39+</text></svg><div><b>Years in Practice</b><small>Indore, Madhya Pradesh</small></div></div>
  </div>
</section>'''
    graph = [website_schema(), firm_schema(), person_schema(), faq_schema(HOME_FAQ),
             {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": f"{FIRM} | Chartered Accountants in Indore",
              "isPartOf": {"@id": SITE_ID}, "about": {"@id": FIRM_ID}, "inLanguage": "en-IN", "dateModified": TODAY}]
    return page(f"Chartered Accountants in Indore | {FIRM}",
                f"{FIRM} is a Chartered Accountant firm in Indore with 39+ years in practice: income tax returns, assessments and appeals, tax planning, company incorporation, RBI compliance and forensic audit.",
                "/", graph, "home", body, inner=False)

def about():
    trail = [("Home", "/"), ("CA Shreya Jain", ABOUT)]
    body = f'''<div class="jaali">
  <div class="wrap person">
    <div class="portrait" role="img" aria-label="Portrait of CA Shreya Jain (photo to be added)"><b>SJ</b><small>PHOTO</small></div>
    <div class="who2">
      <h1>CA Shreya Jain <small>Partner · CA, CS, LL.B., FAFD</small></h1>
      <div class="contactline">
        <span><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ph"/></svg><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></span>
        <span><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#card"/></svg>Partner since 2016</span>
        <span><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#pin"/></svg>Indore</span>
      </div>
    </div>
  </div>
</div>
<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol><li><a href="/">Home</a></li><li><b aria-current="page">CA Shreya Jain</b></li></ol></div></nav>
<div class="wrap two left" style="padding-block:24px 72px">
  <aside class="side" aria-label="Services">{side()}</aside>
  <article>
    <div class="tabs" role="tablist">
      <button role="tab" aria-selected="true" data-tab="bio" id="tab-bio">Profile</button>
      <button role="tab" aria-selected="false" data-tab="edu" id="tab-edu">Qualifications</button>
      <button role="tab" aria-selected="false" data-tab="reg" id="tab-reg">Practice Areas</button>
    </div>
    <div class="tabpanel" data-panel="bio">
      <p>CA Shreya Jain is a practising Chartered Accountant and has been a Partner at {esc(FIRM)} since September 2016. The firm is one of the oldest and most respected Chartered Accountant practices in Indore, serving clients for more than 39 years.</p>
      <p>CA Jain looks after corporate and personal tax compliance, including income tax assessments and appeals, and advises domestic and foreign clients on tax planning. The practice also covers company incorporation and related secretarial matters, RBI compliances and forensic audit.</p>
      <p>Holding the Chartered Accountant, Company Secretary and law qualifications together means a single conversation can cover the tax position, the company-law requirement and the legal route for an appeal.</p>
      <p>The aim is simple: help individuals, businesses and companies plan their finances well and stay fully compliant.</p>
    </div>
    <div class="tabpanel" data-panel="edu" hidden>
      <ul>
        <li>Chartered Accountant (CA), The Institute of Chartered Accountants of India</li>
        <li>Company Secretary (CS), The Institute of Company Secretaries of India</li>
        <li>Bachelor of Laws (LL.B.)</li>
        <li>FAFD: Certificate Course on Forensic Accounting and Fraud Detection, ICAI</li>
        <li>St. Paul's Convent School, Indore</li>
      </ul>
    </div>
    <div class="tabpanel" data-panel="reg" hidden>
      <ul>
        <li>Income Tax, including assessments and appeals</li>
        <li>Corporate Tax</li>
        <li>Foreign Tax and tax planning for foreign clients</li>
        <li>Company Secretarial Work and company incorporation</li>
        <li>RBI Compliances</li>
        <li>Forensic Audit</li>
      </ul>
    </div>
    <p style="margin-top:20px;font-size:13px"><a href="{LINKEDIN}" rel="me noopener" target="_blank">CA Shreya Jain on LinkedIn ↗</a></p>
  </article>
</div>'''
    graph = [website_schema(), firm_schema(), person_schema(), crumbs_schema(trail),
             {"@type": "ProfilePage", "@id": SITE + ABOUT + "#webpage", "url": SITE + ABOUT, "name": "CA Shreya Jain",
              "mainEntity": {"@id": PERSON_ID}, "isPartOf": {"@id": SITE_ID}, "dateModified": TODAY}]
    return page(f"CA Shreya Jain, Chartered Accountant in Indore | {FIRM}",
                f"CA Shreya Jain (CA, CS, LL.B., FAFD) is a Partner at {FIRM}, Indore, handling income tax assessments and appeals, corporate and foreign tax, company secretarial work, RBI compliance and forensic audit.",
                ABOUT, graph, "about", body)

def services():
    trail = [("Home", "/"), (SVC_LABEL, "/services/")]
    cards = "".join(f'<a class="scard" href="/services/{s["id"]}/"><div><span class="dot">{ico(s["icon"])}</span><h2 class="h3">{esc(s["name"])}</h2><p>{esc(s["short"])}</p><span>Learn More ›</span></div></a>' for s in SERVICES)
    body = banner("Practice Areas of CA Shreya Jain" if SHREYA else "Chartered Accountant Services in Indore", trail) + f'<div class="wrap cards">{cards}</div>'
    graph = [website_schema(), firm_schema(), crumbs_schema(trail),
             {"@type": "CollectionPage", "url": SITE + "/services/", "name": SVC_LABEL, "isPartOf": {"@id": SITE_ID},
              "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/services/{s['id']}/", "name": s["name"]} for i, s in enumerate(SERVICES)]}}]
    return page(f"Practice Areas: Tax, Appeals, Company Law | CA Shreya Jain, Indore" if SHREYA else f"CA Services in Indore: Tax, Appeals, Company Law | {FIRM}",
                f"Services of {FIRM}, Chartered Accountants in Indore: income tax, assessments and appeals, tax planning and foreign tax, company incorporation, RBI and FEMA compliance, forensic audit, audit and GST.",
                "/services/", graph, "services", body)

def service(s):
    path = f"/services/{s['id']}/"
    trail = [("Home", "/"), (SVC_LABEL, "/services/"), (s["name"], path)]
    cover = "".join(f"<li>{esc(c)}</li>" for c in s["cover"])
    docs = "".join(f"<li>{esc(d)}</li>" for d in s["docs"])
    body = banner(esc(s["title"]), trail) + f'''
<div class="wrap two detail">
  <article>
    <p style="font-size:15px;color:var(--ink)"><strong>{esc(s["name"])}</strong>: {esc(s["short"])}</p>
    <p>{esc(s["intro"])}</p>
    <h2>What we cover</h2><ul>{cover}</ul>
    <div class="docs"><h3 class="h4">Documents to keep ready</h3><ul>{docs}</ul></div>
    {faq_html(s["faq"], h=f"{esc(s['name'])}: Common Questions", tag="section")}
    <p style="margin-top:28px"><a class="btn" href="/contact/">Discuss Your Requirement</a></p>
  </article>
  <aside class="side" aria-label="Other services">{side(s["id"])}</aside>
</div>'''
    graph = [website_schema(), firm_schema(), crumbs_schema(trail), faq_schema(s["faq"]),
             {"@type": "Service", "@id": SITE + path + "#service", "name": s["name"], "serviceType": s["name"], "description": s["short"],
              "provider": {"@id": PERSON_ID if SHREYA else FIRM_ID}, "areaServed": {"@type": "City", "name": "Indore"}, "url": SITE + path}]
    tail = "CA Shreya Jain, Chartered Accountant, Indore." if SHREYA else f"{FIRM}, Chartered Accountants, Indore."
    return page(f"{s['title']} | {SITE_NAME}", f"{s['short']} {tail}", path, graph, "services", body)

def contact():
    trail = [("Home", "/"), ("Contact Us", "/contact/")]
    body = banner("Contact Us", trail) + f'''
<div class="wrap two" style="padding-block:24px 72px">
  <div>
    <div class="office">
      <div>
        <h2>{esc(FIRM)}</h2>
        <address class="addr">
          {esc(STREET.split(", ")[0])}, {esc(STREET.split(", ")[1])}<br>
          {esc(STREET.split(", ")[2])}<br>
          {CITY}, {REGION} {PIN}<br>
          Phone: <a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a>
        </address>
        <div class="dir">Directions via:<br><a href="{MAPS}" target="_blank" rel="noopener">Google Maps</a></div>
      </div>
      <a class="map" href="{MAPS}" target="_blank" rel="noopener" aria-label="Open our office location in Google Maps">
        <svg viewBox="0 0 310 200" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
          <rect width="310" height="200" fill="#eef0f2"/><path d="M0 120 Q80 100 150 130 T310 110 V200 H0z" fill="#d8ecd6"/>
          <path d="M40 0 L90 200" stroke="#fff" stroke-width="9"/><path d="M0 70 L310 40" stroke="#fde7a6" stroke-width="10"/>
          <path d="M200 0 L230 200" stroke="#fff" stroke-width="7"/><path d="M0 160 L310 150" stroke="#fff" stroke-width="6"/>
          <path d="M120 0 L140 200" stroke="#fff" stroke-width="4"/>
          <text x="150" y="36" font-size="9" fill="#8a8f98" font-family="Lato">R.N.T. Marg</text><text x="150" y="104" font-size="9" fill="#8a8f98" font-family="Lato">Manas Bhavan</text>
          <path d="M165 58c-7 0-12 5-12 12 0 9 12 20 12 20s12-11 12-20c0-7-5-12-12-12z" fill="#e2463b"/><circle cx="165" cy="70" r="4" fill="#9b2219"/>
        </svg>
        <span class="open">Open in Maps ↗</span>
      </a>
    </div>
    <form class="enq" id="enq" novalidate>
      <h2 class="h3">Send an Enquiry</h2>
      <label>Name<input id="f-name" name="name" required autocomplete="name"></label>
      <label>Phone<input id="f-phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel"></label>
      <label class="full">Email<input id="f-email" name="email" type="email" autocomplete="email"></label>
      <label class="full">What do you need help with?
        <select id="f-topic" name="topic">{"".join(f"<option>{esc(s['name'])}</option>" for s in SERVICES)}<option>Something else</option></select>
      </label>
      <label class="full">Message<textarea id="f-msg" name="msg"></textarea></label>
      <div class="row"><button class="btn" type="submit">Send Enquiry</button><span class="ok" id="ok" role="status"></span></div>
    </form>
  </div>
  <aside class="side" aria-label="Services">{side()}</aside>
</div>'''
    graph = [website_schema(), firm_schema(), crumbs_schema(trail),
             {"@type": "ContactPage", "url": SITE + "/contact/", "name": "Contact Us", "about": {"@id": FIRM_ID}, "isPartOf": {"@id": SITE_ID}}]
    return page("Contact CA Shreya Jain, Chartered Accountant, Indore" if SHREYA else f"Contact {FIRM}, Chartered Accountants, Indore",
                f"Contact {FIRM} at {STREET}, Indore {PIN}. Call {PHONE_DISPLAY} for income tax, appeals, company law, RBI compliance and audit.",
                "/contact/", graph, "contact", body)

# ------------------------------------------------------------------ crawler files
def llms_txt():
    lines = [f"# {FIRM}", "",
      f"> {FIRM} is a Chartered Accountant firm in Indore, Madhya Pradesh, India, in practice for more than 39 years. Partner CA Shreya Jain (CA, CS, LL.B., FAFD) handles income tax compliance, income tax assessments and appeals, tax planning for domestic and foreign clients, company incorporation and secretarial work, RBI compliances and forensic audit.", "",
      "## Key facts",
      f"- Firm: {FIRM_LONG}",
      f"- Address: {STREET}, {CITY}, {REGION} {PIN}, India",
      f"- Phone: {PHONE_DISPLAY}",
      f"- Partner: CA Shreya Jain, Partner since September 2016; qualifications CA (ICAI), CS (ICSI), LL.B., FAFD (ICAI)",
      f"- Clients: individuals, families, businesses, companies, NRIs and foreign clients", "",
      "## Pages",
      f"- [Home]({SITE}/): overview of the firm",
      f"- [CA Shreya Jain]({SITE}{ABOUT}): partner profile and qualifications",
      f"- [Services]({SITE}/services/): all services",
    ] + [f"- [{s['name']}]({SITE}/services/{s['id']}/): {s['short']}" for s in SERVICES] + [
      f"- [Contact]({SITE}/contact/): address, phone and enquiry form", "",
      "## Frequently asked questions"] + [f"- Q: {q}\n  A: {a}" for q, a in HOME_FAQ]
    return "\n".join(lines) + "\n"

ROBOTS = f"""# Search engines and AI assistants are welcome to read this site.
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
"""

def sitemap(paths):
    urls = "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n" for p, pr in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'

LOGO_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#2f3f73"/><g transform="translate(9 19) scale(.46)" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 46 L28 22 L42 36 L66 10 L94 40"/><path d="M52 46 L66 32 L80 46"/><path d="M58 40 H74"/></g></svg>\n'

# ------------------------------------------------------------------ write
def relative_links(rel, text):
    # root-relative links ("/services/") -> relative ("../services/") so the
    # site works at any address: a domain root, a GitHub Pages sub-folder, or on disk
    import re
    up = "../" * rel.count("/") or "./"
    return re.sub(r'(href|src)="/(?!/)([^"]*)"', lambda m: f'{m.group(1)}="{up}{m.group(2)}"', text)

def write(rel, text):
    if rel.endswith(".html"): text = relative_links(rel, text)
    p = OUT / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text)

if SHREYA:
    import shreya
    shreya.patch(globals())
    home, about, services, contact, llms_txt = shreya.home, shreya.about, shreya.services, shreya.contact, shreya.llms_txt
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    for f in ("site.css", "site.js"): shutil.copy(ROOT / "assets" / f, OUT / "assets" / f)
write("index.html", home())
write(ABOUT.strip("/") + "/index.html", about())
write("services/index.html", services())
for s in SERVICES: write(f"services/{s['id']}/index.html", service(s))
write("contact/index.html", contact())
write("llms.txt", llms_txt())
write("robots.txt", ROBOTS)
write("assets/logo.svg", LOGO_SVG)
write("sitemap.xml", sitemap([("/", "1.0"), (ABOUT, "0.8"), ("/services/", "0.9")] + [(f"/services/{s['id']}/", "0.8") for s in SERVICES] + [("/contact/", "0.7")]))
print("built", 4 + len(SERVICES), "pages")
