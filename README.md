# CA Shreya Jain · Prakash S. Jain & Co.

Website for CA Shreya Jain (CA, CS, LL.B., FAFD), Partner at Prakash S. Jain & Co., Chartered Accountants, Indore.

Two versions share one design:

| Version | Folder | Voice |
|---|---|---|
| Prakash S. Jain & Co. (firm) | repo root (`index.html`, `services/`, …) | the firm |
| CA Shreya Jain (personal) | `shreya-site/` | first person |

`downloads/` holds each version as a single HTML file that opens offline with a double-click.

## Build

```bash
python3 build.py          # firm version → repo root
python3 build.py shreya   # personal version → shreya-site/
python3 export.py         # single-file versions → downloads/
```

Edit content in `build.py` (services, FAQs, contact details) and `shreya.py` (personal home and about pages). Styles and scripts live in `assets/`.

## SEO

Every page is static HTML with its own title, description, canonical URL, Open Graph tags and schema.org JSON-LD (AccountingService, Person, Service, FAQPage, BreadcrumbList). Each version ships `sitemap.xml`, a `robots.txt` that admits search and AI crawlers, and `llms.txt`.

## Before going live

- Set `SITE` in `build.py` to the real domain (currently `https://www.example.in`) and rebuild.
- Confirm the phone number and add an email address.
- Add CA Shreya Jain's photo, ICAI membership and firm registration numbers.
- Connect the contact form to an inbox (e.g. Formspree or a hosting provider's form handler).
- Host each version at its domain root; pages use root-relative links (`/services/…`).
