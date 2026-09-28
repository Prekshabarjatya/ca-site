(() => {
  const $ = s => document.querySelector(s);

  // header turns navy once the home page scrolls; inner pages are always navy
  const hdr = $("#hdr");
  const onScroll = () => hdr.classList.toggle("solid", document.body.classList.contains("inner") || scrollY > 40);
  addEventListener("scroll", onScroll, {passive:true}); onScroll();

  // mobile drawer
  const drawer = $("#drawer");
  const setDrawer = open => { drawer.classList.toggle("open", open); drawer.setAttribute("aria-hidden", String(!open)); };
  $("#burger").onclick = () => setDrawer(true);
  $("#closeDrawer").onclick = () => setDrawer(false);
  addEventListener("keydown", e => { if (e.key === "Escape") setDrawer(false); });

  // service carousel
  const track = $("#track");
  if (track) {
    $("#prev").onclick = () => track.scrollBy({left:-track.clientWidth*.6});
    $("#next").onclick = () => track.scrollBy({left: track.clientWidth*.6});
  }

  // profile tabs
  const tabs = document.querySelectorAll('[role="tab"]');
  tabs.forEach(b => b.onclick = () => {
    tabs.forEach(x => x.setAttribute("aria-selected", String(x === b)));
    document.querySelectorAll("[data-panel]").forEach(p => p.hidden = p.dataset.panel !== b.dataset.tab);
  });

  // due-date labels count down from today
  const today = new Date(); today.setHours(0,0,0,0);
  const mon = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  let first = true;
  document.querySelectorAll(".date[data-date]").forEach(el => {
    const dt = new Date(el.dataset.date + "T00:00:00"), days = Math.round((dt - today) / 864e5);
    el.querySelector("small").textContent = days < 0 ? "Passed" : days === 0 ? "Today" : days <= 14 ? `In ${days} day${days > 1 ? "s" : ""}` : mon[dt.getMonth()] + " " + dt.getFullYear();
    if (first && days >= 0) { if (days <= 14) el.classList.add("soon"); first = false; }
  });

  // enquiry form (connect to the office inbox when the site goes live)
  const form = $("#enq");
  if (form) form.addEventListener("submit", e => {
    e.preventDefault();
    const n = $("#f-name").value.trim(), p = $("#f-phone").value.trim();
    $("#ok").textContent = (!n || !p) ? "Please add your name and phone number." : `Thank you, ${n}. We will call you back on ${p}.`;
  });

  // mandala: drawn once, rotated slowly by CSS
  function drawMandala(){
    const c = $("#mandala"); if (!c) return;
    const r = c.getBoundingClientRect(); if (!r.width) return;
    const dpr = Math.min(devicePixelRatio || 1, 2), S = Math.round(r.width * dpr);
    c.width = c.height = S;
    const g = c.getContext("2d"); g.scale(S/1000, S/1000); g.translate(500, 500);
    g.lineCap = "round"; g.lineJoin = "round";
    const NAVY = "#2f3f73", GOLD = "#8b7d52", SKY = "#5b7bd5";
    const petalRing = (n, r0, r1, w, col, lw, veins, rot = 0) => {
      for (let i = 0; i < n; i++) {
        g.save(); g.rotate(rot + i * 2 * Math.PI / n);
        g.beginPath(); g.moveTo(0, -r0);
        g.bezierCurveTo(w, -r0 - (r1 - r0) * .35, w * .7, -r1 + (r1 - r0) * .12, 0, -r1);
        g.bezierCurveTo(-w * .7, -r1 + (r1 - r0) * .12, -w, -r0 - (r1 - r0) * .35, 0, -r0);
        g.fillStyle = "#fff"; g.fill(); g.strokeStyle = col; g.lineWidth = lw; g.stroke();
        if (veins) {
          g.beginPath(); g.moveTo(0, -r0 - 6); g.lineTo(0, -r1 + 14);
          for (let k = 1; k <= veins; k++) {
            const y = -r0 - (r1 - r0) * (k / (veins + 1)), s = w * .45 * (1 - k / (veins + 2));
            g.moveTo(0, y + 10); g.lineTo(-s, y - 4); g.moveTo(0, y + 10); g.lineTo(s, y - 4);
          }
          g.lineWidth = lw * .6; g.stroke();
        }
        g.restore();
      }
    };
    const circle = (rad, col, lw, dash) => { g.beginPath(); g.setLineDash(dash || []); g.arc(0, 0, rad, 0, Math.PI * 2); g.strokeStyle = col; g.lineWidth = lw; g.stroke(); g.setLineDash([]); };
    for (let i = 0; i < 48; i++) {
      g.save(); g.rotate(i * Math.PI / 24);
      g.beginPath(); g.moveTo(0, -400); g.bezierCurveTo(14, -430, -12, -450, 4, -478);
      g.strokeStyle = i % 2 ? GOLD : NAVY; g.lineWidth = 1.6; g.stroke();
      g.beginPath(); g.arc(4, -484, 5, 0, Math.PI * 2); g.stroke();
      g.restore();
    }
    petalRing(24, 330, 470, 44, NAVY, 2, 4, Math.PI / 24);
    petalRing(24, 300, 420, 36, GOLD, 1.6, 3);
    circle(300, NAVY, 2);
    g.beginPath();
    for (let a = 0; a <= Math.PI * 2 + .01; a += .01) { const rr = 284 + 7 * Math.sin(a * 36); g.lineTo(Math.cos(a) * rr, Math.sin(a) * rr); }
    g.strokeStyle = GOLD; g.lineWidth = 1.5; g.stroke();
    circle(268, NAVY, 1.5);
    petalRing(32, 190, 268, 20, NAVY, 1.6, 2);
    petalRing(16, 186, 250, 26, GOLD, 1.4, 0, Math.PI / 16);
    circle(186, NAVY, 2);
    for (let i = 0; i < 60; i++) { const a = i * Math.PI / 30; g.beginPath(); g.arc(Math.cos(a) * 176, Math.sin(a) * 176, 4, 0, Math.PI * 2); g.fillStyle = i % 3 ? NAVY : SKY; g.fill(); }
    circle(166, GOLD, 1.2, [3, 4]);
    circle(160, NAVY, 3);
  }

  // misty lake behind "Why choose us"
  function drawLake(){
    const c = $("#lake"); if (!c) return;
    const r = c.getBoundingClientRect(); if (!r.width) return;
    const dpr = Math.min(devicePixelRatio || 1, 2), W = c.width = Math.round(r.width * dpr), H = c.height = Math.round(r.height * dpr);
    const g = c.getContext("2d"), horizon = H * .36;
    const sky = g.createLinearGradient(0, 0, 0, horizon);
    sky.addColorStop(0, "#dfe3ea"); sky.addColorStop(1, "#f4f5f7");
    g.fillStyle = sky; g.fillRect(0, 0, W, horizon);
    let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    const ridge = (amp, col, jag) => {
      const pts = [], ph = [rnd() * 6, rnd() * 6, rnd() * 6];
      for (let x = 0; x <= W; x += 3 * dpr) {
        const u = x / W;
        let y = horizon - amp * (.55 + .3 * Math.sin(u * 3.1 + ph[0]) + .15 * Math.sin(u * 9 + ph[1]));
        y -= jag * (rnd() * .9 + Math.abs(Math.sin(u * 140 + ph[2])) * .6);
        pts.push([x, y]);
      }
      g.beginPath(); g.moveTo(0, horizon); pts.forEach(p => g.lineTo(p[0], p[1])); g.lineTo(W, horizon); g.closePath();
      g.fillStyle = col; g.fill();
      g.save(); g.globalAlpha = .55;
      g.beginPath(); g.moveTo(0, horizon); pts.forEach(p => g.lineTo(p[0], horizon + (horizon - p[1]) * .85)); g.lineTo(W, horizon); g.closePath();
      g.fill(); g.restore();
    };
    const fog = (y, h, a) => { const f = g.createLinearGradient(0, y - h, 0, y + h); f.addColorStop(0, "rgba(240,242,246,0)"); f.addColorStop(.5, `rgba(240,242,246,${a})`); f.addColorStop(1, "rgba(240,242,246,0)"); g.fillStyle = f; g.fillRect(0, y - h, W, h * 2); };
    g.fillStyle = "#e9ecf1"; g.fillRect(0, horizon, W, H - horizon);
    ridge(H * .14, "#b9c3c4", 10 * dpr); fog(horizon - H * .07, H * .07, .8);
    ridge(H * .10, "#8b9c99", 14 * dpr); fog(horizon - H * .03, H * .05, .7);
    ridge(H * .06, "#4f6660", 16 * dpr); fog(horizon + H * .02, H * .05, .65);
    for (let i = 0; i < 140; i++) { const y = horizon + rnd() * (H - horizon), x = rnd() * W; g.fillStyle = `rgba(255,255,255,${.08 + rnd() * .12})`; g.fillRect(x, y, (20 + rnd() * 80) * dpr, dpr); }
  }

  const paint = () => { drawMandala(); drawLake(); };
  let rt; addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(paint, 150); });
  paint();
})();
