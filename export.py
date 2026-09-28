#!/usr/bin/env python3
"""Packs a built site into ONE downloadable HTML file that works offline.

All pages go into the file as hidden sections; links become #anchors and a
tiny router shows the right section.  CSS and JS are inlined.
Run after build.py:   python3 export.py
"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
EXPORT = ROOT / "downloads"

def absolute_links(html, page_rel):
    # undo build.py's relative links so every page shares one link space
    import posixpath
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"(https?:|mailto:|tel:|#|data:|/)", url): return m.group(0)
        path = posixpath.normpath(posixpath.join(page_rel, url))
        if url.endswith("/") or url in (".", "./", "..", "../"): path = path.rstrip("/") + "/"
        return f'{attr}="{path}"'
    return re.sub(r'(href|src)="([^"]*)"', fix, html)

def key(path):
    p = path.strip("/")
    return p.replace("/", "-") if p else "home"

def pack(site_dir, out_name):
    site = pathlib.Path(site_dir)
    skip = {"docs", "downloads", "src"} if site == ROOT else set()
    pages = sorted(p for p in site.rglob("index.html") if not skip & set(p.relative_to(site).parts))
    shell = absolute_links((site / "index.html").read_text(), "/")
    sections, titles = [], {}
    for p in pages:
        rel = "/" + str(p.parent.relative_to(site)).replace(".", "") + "/"
        rel = "/" if rel == "//" else rel
        s = absolute_links(p.read_text(), rel)
        k = key(rel)
        titles[k] = __import__("html").unescape(re.search(r"<title>(.*?)</title>", s).group(1))
        inner = "inner" if 'class="inner"' in s else "home"
        main = re.search(r'<main id="content">\n(.*?)\n</main>', s, re.S).group(1)
        sections.append(f'<section class="pg" data-page="{k}" data-body="{inner}"{"" if k == "home" else " hidden"}>\n{main}\n</section>')

    out = re.sub(r'(<main id="content">\n).*?(\n</main>)', lambda m: m.group(1) + "\n".join(sections) + m.group(2), shell, flags=re.S)
    # internal links -> #anchors (external, tel: and mailto: links are left alone)
    out = re.sub(r'href="(/[^"#]*)"', lambda m: f'href="#{key(m.group(1))}"' if not m.group(1).startswith("/assets/") else m.group(0), out)
    out = out.replace('<link rel="icon" href="#assets-logo.svg" type="image/svg+xml">', "")
    out = re.sub(r'<link rel="icon"[^>]*>\n', "", out)
    out = re.sub(r'<link rel="canonical"[^>]*>\n', "", out)
    css = (site / "assets/site.css").read_text()
    js = (site / "assets/site.js").read_text()
    out = out.replace('<link rel="stylesheet" href="/assets/site.css">', f"<style>\n{css}\n</style>")
    router = """
// offline single-file router: #page-key shows that section
(() => {
  const titles = %s;
  const show = () => {
    const k = (location.hash || "#home").slice(1);
    const sec = document.querySelector(`.pg[data-page="${k}"]`);
    if (!sec) return;               // e.g. #content skip link
    document.querySelectorAll(".pg").forEach(s => s.hidden = s !== sec);
    document.body.className = sec.dataset.body;
    document.title = titles[k] || document.title;
    document.getElementById("drawer").classList.remove("open");
    scrollTo({top: 0, behavior: "instant"});
    dispatchEvent(new Event("scroll"));
    dispatchEvent(new Event("resize"));   // repaint the canvases now visible
  };
  addEventListener("hashchange", show);
  show();
})();
""" % __import__("json").dumps(titles)
    out = out.replace('<script src="/assets/site.js" defer></script>', f"<script>\n{js}\n{router}\n</script>")
    EXPORT.mkdir(exist_ok=True)
    (EXPORT / out_name).write_text(out)
    print(out_name, len(pages), "pages,", round(len(out) / 1024), "KB")

pack(ROOT, "prakash-s-jain-co-website.html")
pack(ROOT / "docs", "ca-shreya-jain-website.html")
