# Ad #3: 5-slide Instagram carousel (1080x1080 each). Renders via render3.js.
HEAD = '<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>'
CSS = '''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;font-family:"Inter",-apple-system,sans-serif;-webkit-font-smoothing:antialiased;color:#fff}
body{position:relative;overflow:hidden;background:radial-gradient(circle at 85% 90%,rgba(249,115,22,.30) 0%,rgba(249,115,22,0) 45%),
     radial-gradient(circle at 0% 0%,#16305a 0%,rgba(22,48,90,0) 55%),#0a1830}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.06) 1.5px,transparent 1.5px);background-size:28px 28px}
.wrap{position:absolute;inset:60px 76px 120px;display:flex;flex-direction:column;justify-content:center}
.eyebrow{align-self:flex-start;font-size:20px;font-weight:800;letter-spacing:1.4px;color:#fdba74;background:rgba(249,115,22,.16);border:2px solid rgba(249,115,22,.55);padding:10px 20px;border-radius:30px;margin-bottom:30px}
h1{font-size:86px;line-height:1.04;font-weight:900;letter-spacing:-2.6px}
h1 em{font-style:normal;color:#F97316}
.sub{font-size:36px;line-height:1.35;color:#d3dcea;font-weight:500;margin-top:24px}.sub b{color:#fff}
.foot{position:absolute;left:76px;right:76px;bottom:52px;display:flex;justify-content:space-between;align-items:center;font-size:22px;font-weight:700;color:#9fb0c8}
.brand{display:flex;align-items:center;gap:10px;color:#fff}
.mk{width:30px;height:30px;border-radius:8px;background:#F97316;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:19px;color:#fff}
.pg{display:flex;gap:8px}.pg i{width:10px;height:10px;border-radius:50%;background:rgba(255,255,255,.25)}.pg i.on{background:#F97316;width:28px;border-radius:5px}
.swipe{color:#F97316;font-size:26px;font-weight:800}
/* iOS-style cards */
.card{background:#fff;color:#000;border-radius:34px;box-shadow:0 40px 80px rgba(0,0,0,.45)}
.note{display:flex;align-items:center;gap:22px;padding:28px 32px}
.note .ic{flex:none;width:76px;height:76px;border-radius:18px;background:linear-gradient(180deg,#5af575,#14c23a);display:flex;align-items:center;justify-content:center}
.note .t{flex:1}.note .row{display:flex;justify-content:space-between;font-size:30px;color:#6b6b72}
.note .row b{color:#000;font-weight:700}.note .num{font-size:48px;font-weight:600;margin-top:4px;letter-spacing:-.5px}
.recents{padding:10px 0}
.recents h3{font-size:24px;font-weight:700;color:#8e8e93;letter-spacing:.5px;padding:18px 34px 8px;text-transform:uppercase}
.rec{display:flex;align-items:center;justify-content:space-between;padding:22px 34px;border-top:1px solid #e5e5ea}
.rec b{display:block;font-size:34px;font-weight:600;letter-spacing:-.4px}
.rec small{font-size:24px;color:#8e8e93}
.rec .r{text-align:right;font-size:24px;color:#8e8e93}
.tag{display:inline-block;font-size:22px;font-weight:800;padding:6px 14px;border-radius:12px;margin-top:6px}
.tag.no{background:#fee2e2;color:#dc2626}.tag.yes{background:#dcfce7;color:#15803d}
.thread{padding:26px 26px 30px;display:flex;flex-direction:column;gap:14px}
.thead{text-align:center;font-size:22px;color:#8e8e93;padding-bottom:6px}.thead b{display:block;color:#000;font-size:26px;font-weight:600}
.b{max-width:82%;padding:16px 22px;font-size:30px;line-height:1.27;border-radius:30px;letter-spacing:-.2px}
.me{align-self:flex-end;background:linear-gradient(180deg,#1a8cff,#0a7aff);color:#fff;border-bottom-right-radius:8px}
.them{align-self:flex-start;background:#e9e9eb;border-bottom-left-radius:8px}
.list{list-style:none;margin-top:36px}
.list li{display:flex;align-items:center;gap:22px;font-size:42px;font-weight:700;padding:15px 0;border-bottom:1px solid rgba(255,255,255,.1)}
.list li:last-child{border:none}
.list i{flex:none;width:46px;height:46px;border-radius:50%;background:#F97316;display:flex;align-items:center;justify-content:center}
.pull{margin-top:44px;background:rgba(249,115,22,.14);border-left:6px solid #F97316;border-radius:0 18px 18px 0;padding:24px 30px;font-size:36px;font-weight:800;letter-spacing:-.5px}
.cta{align-self:flex-start;display:inline-flex;align-items:center;gap:16px;background:#F97316;color:#fff;font-size:50px;font-weight:800;padding:36px 60px;border-radius:22px;box-shadow:0 18px 40px rgba(249,115,22,.5);margin-top:44px}
.towns{margin-top:48px;font-size:26px;font-weight:600;color:#9fb0c8;line-height:1.5}
'''
PH = '<svg width="40" height="40" viewBox="0 0 24 24" fill="#fff"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>'
CK = '<i><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></i>'

def foot(n, swipe=True):
    pg = ''.join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, 6))
    right = '<span class="swipe">Swipe &rarr;</span>' if swipe else '<span class="swipe">Tap Book Now</span>'
    return f'<div class="foot"><div class="brand"><span class="mk">R</span>Ravara</div><div class="pg">{pg}</div>{right}</div>'

slides = {
1: f'''<div class="wrap">
 <div class="eyebrow">CALGARY HVAC &amp; PLUMBING</div>
 <h1>This missed call was<br>a <em>$9,000 furnace.</em></h1>
 <p class="sub">You were under a sink in Okotoks.<br>You couldn&rsquo;t pick up.</p>
 <div class="card note" style="margin-top:60px"><div class="ic">{PH}</div><div class="t">
   <div class="row"><b>Missed Call</b><span>2:14 PM</span></div><div class="num">(403) 555-0148</div></div></div>
</div>''',
2: '''<div class="wrap">
 <h1>They didn&rsquo;t leave<br>a voicemail.</h1>
 <p class="sub" style="font-size:40px;color:#F97316;font-weight:800;margin-top:14px">They called the next company<br>on the list.</p>
 <div class="card recents" style="margin-top:60px">
  <h3>The homeowner&rsquo;s recent calls</h3>
  <div class="rec"><div><b>Next company on Google</b><small>2:15 PM</small></div><div class="r"><span class="tag yes">Answered &middot; booked</span></div></div>
  <div class="rec"><div><b>Your business</b><small>2:14 PM</small></div><div class="r"><span class="tag no">No answer</span></div></div>
 </div>
</div>''',
3: '''<div class="wrap">
 <h1>Now your line<br>texts them back.</h1>
 <p class="sub" style="margin-top:12px">In seconds. <b>From your business, in your name.</b></p>
 <div class="card thread" style="margin-top:60px">
  <div class="thead"><b>Apex Heating &amp; Air</b>Text Message &middot; 2:14 PM</div>
  <div class="b me">Sorry we missed you. Apex Heating &amp; Air here &mdash; we&rsquo;re on a job. What&rsquo;s going on?</div>
  <div class="b them">Furnace quit. House is down to 12</div>
  <div class="b me">No heat &mdash; got it. Texting you a time for a tech today.</div>
 </div>
</div>''',
4: f'''<div class="wrap">
 <h1>Nothing for <em>you</em> to do.</h1>
 <ul class="list">
  <li>{CK}No app to learn</li>
  <li>{CK}No new number</li>
  <li>{CK}No robot on your phone, no call centre</li>
  <li>{CK}Your customers only ever see your name</li>
 </ul>
 <div class="pull">One recovered call pays for the month.</div>
</div>''',
5: '''<div class="wrap">
 <div class="eyebrow">CALGARY HVAC &amp; PLUMBING</div>
 <h1>Missed a call?<br><em>Still book the job.</em></h1>
 <p class="sub">We&rsquo;ll show you how it works on your own business line.</p>
 <div class="cta">Book a free call <span>&rarr;</span></div>
 <p class="towns">Calgary &middot; Airdrie &middot; Okotoks &middot; High River &middot; Chestermere &middot; Cochrane</p>
</div>''',
}
for n, body in slides.items():
    html = HEAD + CSS + '</style></head><body><div class="dots"></div>' + body + foot(n, swipe=n < 5) + '</body></html>'
    open(f'ravara-ig3-slide{n}.html', 'w').write(html)
