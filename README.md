# CA Shreya Jain · Prakash S. Jain & Co.

Website for CA Shreya Jain (CA, CS, LL.B., FAFD), Partner at Prakash S. Jain & Co., Chartered Accountants, Indore.

Two versions share one design:

| Version | Folder | Voice |
|---|---|---|
| Prakash S. Jain & Co. (firm) | repo root (`index.html`, `services/`, …) | the firm |
| CA Shreya Jain (personal), **published** | `docs/` | first person |

`downloads/` holds each version as a single HTML file that opens offline with a double-click.

## Build

```bash
python3 build.py          # firm version → repo root
python3 build.py shreya   # personal version → docs/ (published)
python3 export.py         # single-file versions → downloads/
```

Edit content in `build.py` (services, FAQs, contact details) and `shreya.py` (personal home and about pages). Styles and scripts live in `assets/`.

## SEO

Every page is static HTML with its own title, description, canonical URL, Open Graph tags and schema.org JSON-LD (AccountingService, Person, Service, FAQPage, BreadcrumbList). Each version ships `sitemap.xml`, a `robots.txt` that admits search and AI crawlers, and `llms.txt`.

## Live site

GitHub Pages publishes the `docs/` folder on `main`, which is CA Shreya Jain's site:

**https://prekshabarjatya.github.io/ca-site/**

The firm version at the repo root is kept for reference and is not published.

Links inside the pages are relative, so the site works in this sub-folder, at a custom domain, or opened from disk.

## Before going live

- When a custom domain is ready, set `SITE` in `build.py` to it (currently the GitHub Pages address) and rebuild. `robots.txt` and `sitemap.xml` only take effect at a domain root, so this matters for SEO.
- Confirm the phone number and add an email address.
- Add CA Shreya Jain's photo, ICAI membership and firm registration numbers.
- Connect the contact form to an inbox (e.g. Formspree or a hosting provider's form handler).
