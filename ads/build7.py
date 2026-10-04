# Ad #7: "Fun fact" card (1:1), cream background, owner-focused.
html = '''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet"><style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;font-family:"Inter",sans-serif;-webkit-font-smoothing:antialiased;color:#0a1830}
body{position:relative;overflow:hidden;background:#FBF6EC}
.lines{position:absolute;inset:0;background-image:linear-gradient(#e9e1cf 1.5px,transparent 1.5px);background-size:100% 44px;opacity:.6}
.wrap{position:absolute;left:64px;right:64px;top:0;bottom:178px;display:flex;flex-direction:column;justify-content:center;align-items:flex-start}
.tag{display:inline-flex;align-items:center;gap:12px;background:#F97316;color:#fff;font-weight:900;font-size:24px;letter-spacing:1.6px;padding:12px 22px 12px 16px;border-radius:40px}
.tag small{font-weight:700;opacity:.9;letter-spacing:1px}
h1{font-size:84px;line-height:1.02;font-weight:900;letter-spacing:-3px;margin-top:30px}
h1 u{text-decoration:none;background:linear-gradient(transparent 62%,rgba(249,115,22,.45) 62%)}
.ledger{margin-top:44px;background:#fff;border:3px solid #0a1830;border-radius:18px;padding:26px 34px;font-family:"JetBrains Mono",monospace;box-shadow:12px 12px 0 #0a1830;width:940px}
.ledger h3{font-size:22px;font-weight:800;letter-spacing:2px;color:#6b7280;margin-bottom:10px}
.row{display:flex;align-items:baseline;font-size:31px;font-weight:700;padding:12px 0}
.row .dots{flex:1;border-bottom:3px dotted #c4c4c4;margin:0 14px;transform:translateY(-6px)}
.ok{color:#16a34a}
.row.miss{color:#dc2626}.row.miss .v{background:#fee2e2;padding:2px 10px;border-radius:8px}
.sub{font-size:44px;font-weight:900;letter-spacing:-1.2px;margin-top:44px}
.sub span{color:#dc2626}
.band{position:absolute;left:0;right:0;bottom:0;height:178px;background:#0a1830;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px;gap:28px}
.band p{font-size:30px;font-weight:800;line-height:1.2;letter-spacing:-.5px}.band p em{font-style:normal;color:#F97316}
.cta{flex:none;background:#F97316;color:#fff;font-size:32px;font-weight:900;padding:26px 36px;border-radius:16px}
</style></head><body><div class="lines"></div>
<div class="wrap">
 <div class="tag"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 00-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0012 3z"/></svg>FUN FACT <small>&middot; CALGARY HVAC &amp; PLUMBING</small></div>
 <h1>The jobs you lose <u>never<br>show up</u> on your books.</h1>
 <div class="ledger">
  <h3>THIS WEEK&rsquo;S BOOKS</h3>
  <div class="row"><span>Jobs booked</span><span class="dots"></span><span class="ok">tracked</span></div>
  <div class="row"><span>Invoices sent</span><span class="dots"></span><span class="ok">tracked</span></div>
  <div class="row miss"><span>Jobs lost to missed calls</span><span class="dots"></span><span class="v">???</span></div>
 </div>
 <p class="sub">They just look like a <span>missed call.</span></p>
</div>
<div class="band">
 <p>Now every missed call gets a text back<br><em>in your name</em>, so it stays your job.</p>
 <div class="cta">Book a free call &rarr;</div>
</div>
</body></html>'''
open('ravara-ig7-funfact.html','w').write(html)
