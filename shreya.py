"""Pages for the CA Shreya Jain version of the site (python3 build.py shreya).

Written in CA Shreya Jain's own voice, as on the LinkedIn profile.  Service
and contact pages are shared with the firm version and come from build.py.
"""

def patch(g):
    # borrow build.py's helpers and settings without overriding this module's pages
    for k, v in g.items():
        if k not in globals():
            globals()[k] = v
    global FAQ
    FAQ = [
      ("Who is CA Shreya Jain?",
       "CA Shreya Jain is a practising Chartered Accountant in Indore and a Partner at Prakash S. Jain & Co. since September 2016. The firm has been in practice for more than 39 years. CA Jain also holds Company Secretary (CS), LL.B. and FAFD qualifications."),
      ("What does CA Shreya Jain specialise in?",
       "Corporate and personal tax compliance, income tax assessments and appeals, tax planning for domestic and foreign clients, company incorporation and secretarial matters, RBI compliances and forensic audit."),
      ("Can CA Shreya Jain represent me in an income tax appeal?",
       "Yes. CA Shreya Jain handles income tax assessments and appeals before the Commissioner of Income Tax (Appeals) and the Income Tax Appellate Tribunal."),
      ("Does CA Shreya Jain advise NRIs and foreign clients?",
       "Yes. The practice covers foreign tax, NRI taxation, DTAA relief, Form 15CA / 15CB and RBI / FEMA compliance for foreign investment into India."),
      ("Where can I meet CA Shreya Jain?",
       f"At the office of Prakash S. Jain & Co., {STREET}, {CITY}, {REGION} {PIN}. Call {PHONE_DISPLAY} to fix a time."),
    ]

MONO = '<svg viewBox="0 0 100 100" aria-hidden="true" style="width:70%;stroke:none"><text x="50" y="63" text-anchor="middle" font-family="Quicksand, sans-serif" font-weight="700" font-size="40" letter-spacing="2" fill="#fff">SJ</text></svg>'

def seal(label, size, title, sub):
    return f'''<div class="seal"><svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="27" fill="none" stroke="#c9bd93" stroke-width="1.5"/><circle cx="30" cy="30" r="22" fill="none" stroke="#c9bd93" stroke-dasharray="2 3"/><text x="30" y="35" text-anchor="middle" font-family="Quicksand" font-weight="700" font-size="{size}" fill="#fff">{label}</text></svg><div><b>{title}</b><small>{sub}</small></div></div>'''


def home():
    mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    dates = "".join(f'<div class="date" data-date="{d}"><b><time datetime="{d}">{int(d[8:])} {mon[int(d[5:7])-1]}</time></b><small>{mon[int(d[5:7])-1]} {d[:4]}</small><span>{esc(t)}</span></div>' for d, t in DATES)
    car = "".join(f'<a class="svc{" feat" if i==1 else ""}" href="/services/{s["id"]}/"><span class="ring"><svg class="deco" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco-ring"/></svg>{ico(s["icon"])}</span><span>{esc(s["name"])}</span></a>' for i, s in enumerate(SERVICES))
    body = f'''<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <h1 id="h1"><span class="kicker">CA Shreya Jain · Chartered Accountant in Indore</span><span class="line">Tax, Company Law and <em>Appeals</em>, Handled by <em>One Advisor</em></span></h1>
    <div class="mandala" aria-hidden="true"><canvas id="mandala"></canvas><div class="core">{MONO}</div></div>
  </div>
  <span class="scroll" aria-hidden="true"></span>
</section>

<section class="facts" aria-label="At a glance"><div class="wrap"><dl>
  <div><dt>Qualifications</dt><dd>CA · CS · LL.B. · FAFD</dd></div>
  <div><dt>Practice</dt><dd>Partner, {esc(FIRM)} since 2016</dd></div>
  <div><dt>Focus</dt><dd>Income tax, appeals and foreign tax</dd></div>
  <div><dt>Based in</dt><dd>Manas Bhavan, R.N.T. Marg, Indore</dd></div>
</dl></div></section>

<section class="intro">
  <div class="wrap">
    <div>
      <h2>Practising Chartered Accountant in Indore, Madhya Pradesh</h2>
      <p>I am a practising Chartered Accountant and a partner in one of the oldest and most respected firms in Indore, M/s {esc(FIRM)}, which has served clients for more than 39 years.</p>
      <p>My work helps individuals, businesses and companies plan their finances well and stay fully compliant.</p>
    </div>
    <div class="col2">
      <p>I look after corporate and personal tax compliance, including <a href="/services/assessments-appeals/">income tax assessments and appeals</a>, and advise domestic and foreign clients on <a href="/services/tax-planning-foreign-tax/">tax planning</a>. I also handle <a href="/services/company-incorporation-secretarial/">company incorporation and related matters</a>, <a href="/services/rbi-fema-compliance/">RBI compliances</a> and <a href="/services/forensic-audit/">forensic audit</a>.</p>
      <p>Being a Chartered Accountant, a Company Secretary and a law graduate lets me look at a problem from the tax, company-law and legal side at the same time. <a href="{ABOUT}">More about me</a>.</p>
    </div>
  </div>
</section>

<section class="carousel" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 id="svc-h" class="sr">Practice Areas</h2>
    <div class="car">
      <button class="arrow" id="prev" aria-label="Previous practice areas"><svg viewBox="0 0 24 24"><path d="M17 4L5 12l12 8z"/></svg></button>
      <div class="track" id="track">{car}</div>
      <button class="arrow" id="next" aria-label="Next practice areas"><svg viewBox="0 0 24 24"><path d="M7 4l12 8-12 8z"/></svg></button>
    </div>
    <a class="btn" href="/services/">View All Practice Areas</a>
  </div>
</section>

<section class="why" aria-labelledby="why-h">
  <canvas id="lake" aria-hidden="true"></canvas>
  <div class="wrap">
    <div>
      <h2 id="why-h">Why Clients Work With Me</h2>
      <p>Tax questions rarely stay in one lane. A notice can turn into a company-law issue, and a restructuring can raise a foreign-exchange question. With CA, CS and LL.B. qualifications, I can follow a matter through all of these without handing it over.</p>
      <p>Behind me is a firm with almost four decades of practice in Indore, so every engagement has an experienced team and a long track record behind it.</p>
      <a class="btn light" href="/contact/">Book a Consultation</a>
    </div>
    <ul>
      <li><i aria-hidden="true">✓</i><span>Chartered Accountant, Company Secretary, LL.B. and FAFD in one advisor.</span></li>
      <li><i aria-hidden="true">✓</i><span>Income tax assessments and appeals handled from notice to hearing.</span></li>
      <li><i aria-hidden="true">✓</i><span>Tax planning for domestic and foreign clients, with RBI and FEMA compliance.</span></li>
      <li><i aria-hidden="true">✓</i><span>Company incorporation and secretarial work alongside the tax work.</span></li>
      <li><i aria-hidden="true">✓</i><span>Partner at {esc(FIRM)}, in practice in Indore for 39+ years.</span></li>
    </ul>
  </div>
</section>

<section class="who" aria-label="Who I work with">
  <div class="wrap grid">
    <div class="box"><div><h3>Businesses &amp; Companies</h3><ul><li>Corporate tax compliance</li><li>Company incorporation</li><li>Company secretarial work</li><li>RBI compliances</li><li>Forensic audit</li></ul></div></div>
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

{faq_html(FAQ)}

<section class="badges jaali-dark" aria-label="Qualifications">
  <div class="wrap">
    {seal("CA", 16, "Chartered Accountant", "ICAI")}
    {seal("CS", 16, "Company Secretary", "ICSI")}
    {seal("LL.B.", 12, "Bachelor of Laws", "Law graduate")}
    {seal("FAFD", 12, "Forensic Accounting", "ICAI certification")}
  </div>
</section>'''
    graph = [website_schema(), person_schema(), firm_schema(), faq_schema(FAQ),
             {"@type": "ProfilePage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": "CA Shreya Jain | Chartered Accountant in Indore",
              "mainEntity": {"@id": PERSON_ID}, "isPartOf": {"@id": SITE_ID}, "inLanguage": "en-IN", "dateModified": TODAY}]
    return page("CA Shreya Jain | Chartered Accountant in Indore (CA, CS, LL.B.)",
                f"CA Shreya Jain is a Chartered Accountant, Company Secretary and law graduate in Indore, Partner at {FIRM}. Income tax, assessments and appeals, foreign tax, company law, RBI compliance and forensic audit.",
                "/", graph, "home", body, inner=False)


def about():
    trail = [("Home", "/"), ("About", ABOUT)]
    body = f'''<div class="jaali">
  <div class="wrap person">
    <div class="portrait" role="img" aria-label="Portrait of CA Shreya Jain (photo to be added)"><b>SJ</b><small>PHOTO</small></div>
    <div class="who2">
      <h1>About CA Shreya Jain <small>CA, CS, LL.B., FAFD</small></h1>
      <div class="contactline">
        <span><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ph"/></svg><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></span>
        <span><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#card"/></svg>Partner, {esc(FIRM)}</span>
        <span><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#pin"/></svg>Indore</span>
      </div>
    </div>
  </div>
</div>
<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol><li><a href="/">Home</a></li><li><b aria-current="page">About</b></li></ol></div></nav>
<div class="wrap two left" style="padding-block:24px 72px">
  <aside class="side" aria-label="Practice areas">{side()}</aside>
  <article>
    <div class="tabs" role="tablist">
      <button role="tab" aria-selected="true" data-tab="bio" id="tab-bio">Profile</button>
      <button role="tab" aria-selected="false" data-tab="edu" id="tab-edu">Qualifications</button>
      <button role="tab" aria-selected="false" data-tab="reg" id="tab-reg">Experience</button>
    </div>
    <div class="tabpanel" data-panel="bio">
      <p>I am a practising Chartered Accountant, working as a partner in one of the oldest and most respected firms in Indore, M/s {esc(FIRM)}, which has been providing services for more than 39 years.</p>
      <p>I look after corporate and personal tax compliance, including income tax assessments and appeals, and provide advisory services on tax planning to domestic and foreign clients. My practice also covers company incorporation and related matters, RBI compliances and forensic audit.</p>
      <p>I am dedicated to optimising financial strategies and ensuring compliance for individuals, businesses and companies. If you are working towards a financial or compliance goal, I would be glad to talk about how I can help.</p>
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
        <li><strong>Partner, {esc(FIRM)}</strong>, Indore · September 2016 to present</li>
        <li>Skills: Income Tax, Appeals, Company Secretarial Work, Corporate Tax, Foreign Tax</li>
      </ul>
    </div>
    <p style="margin-top:20px;font-size:15px"><a href="{LINKEDIN}" rel="me noopener" target="_blank">Connect on LinkedIn ↗</a></p>
  </article>
</div>'''
    graph = [website_schema(), person_schema(), firm_schema(), crumbs_schema(trail),
             {"@type": "AboutPage", "@id": SITE + ABOUT + "#webpage", "url": SITE + ABOUT, "name": "About CA Shreya Jain",
              "mainEntity": {"@id": PERSON_ID}, "isPartOf": {"@id": SITE_ID}, "dateModified": TODAY}]
    return page("About CA Shreya Jain | CA, CS, LL.B., FAFD, Indore",
                f"CA Shreya Jain is a practising Chartered Accountant and Company Secretary with an LL.B. and FAFD, Partner at {FIRM}, Indore, since 2016.",
                ABOUT, graph, "about", body)


def llms_txt():
    lines = ["# CA Shreya Jain", "",
      f"> CA Shreya Jain is a practising Chartered Accountant in Indore, Madhya Pradesh, India, and a Partner at {FIRM} (in practice for more than 39 years) since September 2016. Qualifications: CA (ICAI), CS (ICSI), LL.B., FAFD (ICAI). Practice: corporate and personal tax compliance, income tax assessments and appeals, tax planning for domestic and foreign clients, company incorporation, RBI compliances and forensic audit.", "",
      "## Key facts",
      "- Name: CA Shreya Jain (C.A., C.S., LL.B., FAFD)",
      f"- Role: Partner, {FIRM_LONG}, since September 2016",
      f"- Office: {STREET}, {CITY}, {REGION} {PIN}, India",
      f"- Phone: {PHONE_DISPLAY}",
      f"- LinkedIn: {LINKEDIN}",
      "- Top skills: Income Tax, Appeals, Company Secretarial Work, Corporate Tax, Foreign Tax", "",
      "## Pages",
      f"- [Home]({SITE}/): overview",
      f"- [About]({SITE}{ABOUT}): profile, qualifications and experience",
      f"- [Practice areas]({SITE}/services/): all practice areas",
    ] + [f"- [{s['name']}]({SITE}/services/{s['id']}/): {s['short']}" for s in SERVICES] + [
      f"- [Contact]({SITE}/contact/): office address, phone and enquiry form", "",
      "## Frequently asked questions"] + [f"- Q: {q}\n  A: {a}" for q, a in FAQ]
    return "\n".join(lines) + "\n"
