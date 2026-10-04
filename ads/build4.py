# Ad #4: meme-style single images (1:1). A = text-post meme, B = POV without/with panels.
HEAD = '<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>'
BASE = '''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;font-family:"Inter",-apple-system,"Helvetica Neue",sans-serif;-webkit-font-smoothing:antialiased;color:#0a0a0a}
body{position:relative;overflow:hidden;background:#FACC15}
.stripes{position:absolute;left:0;right:0;height:26px;background:repeating-linear-gradient(-45deg,#0a0a0a 0 26px,#FACC15 26px 52px)}
.cta{display:inline-flex;align-items:center;gap:14px;background:#0a0a0a;color:#fff;font-weight:800;border-radius:16px}
.cta span{color:#F97316}
.mk{width:30px;height:30px;border-radius:8px;background:#F97316;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:19px;color:#fff}
'''
PH = '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="#fff"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>'
MSG = '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="#fff"><path d="M12 3C6.5 3 2 6.6 2 11c0 2.4 1.3 4.6 3.4 6.1-.2 1.3-.9 2.6-1.9 3.6 2 0 3.8-.8 5.1-1.8 1.1.3 2.2.4 3.4.4 5.5 0 10-3.6 10-8S17.5 3 12 3z"/></svg>'
VM = '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4"><circle cx="6.5" cy="12" r="3.5"/><circle cx="17.5" cy="12" r="3.5"/><path d="M6.5 15.5h11"/></svg>'

# ---------- A: text-post meme ----------
A = HEAD + BASE + '''
.stripes.t{top:0}.stripes.b{bottom:0}
.post{position:absolute;left:60px;right:60px;top:70px;background:#fff;border-radius:28px;padding:48px 46px 50px;box-shadow:0 22px 0 #0a0a0a}
.who{display:flex;align-items:center;gap:16px;margin-bottom:40px}
.av{width:64px;height:64px;border-radius:50%;background:#F97316;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:900;font-size:30px}
.who b{display:block;font-size:26px;font-weight:800}.who span{font-size:22px;color:#6b7280;font-weight:500}
.line{font-size:56px;line-height:1.16;font-weight:600;letter-spacing:-1px;margin-bottom:46px}
.line b{font-weight:800}
.line i{font-style:normal;color:#6b7280;font-weight:500}
.line.hit i{color:#dc2626;font-weight:700}
.bottom{position:absolute;left:60px;right:60px;bottom:66px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.punch{font-size:38px;font-weight:900;line-height:1.15;letter-spacing:-.6px}
.cta{font-size:30px;padding:24px 32px;flex:none}
</style></head><body>
<div class="stripes t"></div>
<div class="post">
 <div class="who"><div class="av">R</div><div><b>Ravara</b><span>Calgary HVAC &amp; plumbing</span></div></div>
 <p class="line"><b>Homeowner at &minus;30:</b> <i>*calls your business*</i></p>
 <p class="line"><b>You:</b> <i>*under a sink in Okotoks*</i></p>
 <p class="line"><b>Your phone:</b> <i>*rings out*</i></p>
 <p class="line hit" style="margin-bottom:0"><b>Homeowner, immediately:</b> <i>*calls the next company on the list*</i></p>
</div>
<div class="bottom">
 <div class="punch">Unless your line texts<br>them back first.</div>
 <div class="cta">Book a free call <span>&rarr;</span></div>
</div>
<div class="stripes b"></div>
</body></html>'''

# ---------- B: POV without / with ----------
B = HEAD + BASE + '''
.stripes{top:0}
.pov{position:absolute;left:60px;right:60px;top:62px;font-size:58px;font-weight:900;line-height:1.06;letter-spacing:-2px}
.pov em{font-style:normal;background:#0a0a0a;color:#FACC15;padding:0 12px;border-radius:8px}
.panels{position:absolute;left:60px;right:60px;top:290px;display:flex;gap:24px}
.pn{flex:1;height:560px;border-radius:36px;overflow:hidden;position:relative;border:6px solid #0a0a0a;color:#fff;
    background:radial-gradient(circle at 30% 100%,#c2410c 0%,rgba(194,65,12,0) 55%),linear-gradient(180deg,#0b1430,#16224a)}
.lab{position:absolute;top:18px;left:50%;transform:translateX(-50%);font-size:21px;font-weight:900;letter-spacing:1.2px;padding:9px 18px;border-radius:30px;white-space:nowrap}
.lab.no{background:#dc2626}.lab.yes{background:#16a34a}
.clk{text-align:center;margin-top:76px;font-size:76px;font-weight:700;letter-spacing:-2px;line-height:1}
.dt{text-align:center;font-size:17px;font-weight:600;opacity:.85;margin-top:6px}
.ns{position:absolute;left:14px;right:14px;top:220px}
.n{background:rgba(245,245,250,.92);color:#000;border-radius:20px;padding:13px 14px;display:flex;gap:11px;margin-bottom:9px}
.ic{flex:none;width:38px;height:38px;border-radius:10px;background:linear-gradient(180deg,#5af575,#14c23a);display:flex;align-items:center;justify-content:center}
.ic.vm{background:linear-gradient(180deg,#9ca3af,#6b7280)}
.n .h{display:flex;justify-content:space-between;font-size:17px}.n .h b{font-weight:700}.n .h span{color:#6b6b72}
.n p{font-size:21px;line-height:1.25;margin-top:2px}
.n.dim p{color:#6b7280}
.verdict{position:absolute;left:14px;right:14px;bottom:26px;text-align:center;font-size:28px;font-weight:900}
.verdict.no{color:#fca5a5}.verdict.yes{color:#86efac}
.bottom{position:absolute;left:60px;right:60px;bottom:52px;display:flex;align-items:center;justify-content:space-between;gap:20px}
.line{font-size:34px;font-weight:900;line-height:1.12;letter-spacing:-.8px}
.cta{font-size:30px;padding:24px 32px;flex:none}
</style></head><body>
<div class="stripes"></div>
<div class="pov">POV: you finally crawl out<br>from under the sink and<br><em>check your phone</em></div>
<div class="panels">
 <div class="pn"><div class="lab no">WITHOUT TEXT-BACK</div>
  <div class="clk">2:47</div><div class="dt">Tuesday &middot; &minus;28&deg;</div>
  <div class="ns">
   <div class="n"><div class="ic">@PH@</div><div style="flex:1"><div class="h"><b>Missed Call</b><span>33m ago</span></div><p>(403) 555-0148</p></div></div>
   <div class="n dim"><div class="ic vm">@VM@</div><div style="flex:1"><div class="h"><b>Voicemail</b><span></span></div><p>No new voicemail</p></div></div>
  </div>
  <div class="verdict no">Job: gone to the next guy</div>
 </div>
 <div class="pn"><div class="lab yes">WITH TEXT-BACK</div>
  <div class="clk">2:47</div><div class="dt">Tuesday &middot; &minus;28&deg;</div>
  <div class="ns">
   <div class="n"><div class="ic">@MSG@</div><div style="flex:1"><div class="h"><b>(403) 555-0148</b><span>now</span></div><p>Furnace quit, house is down to 12. Can someone come today?</p></div></div>
   <div class="n dim"><div class="ic">@PH@</div><div style="flex:1"><div class="h"><b>Missed Call</b><span>33m ago</span></div><p>(403) 555-0148</p></div></div>
  </div>
  <div class="verdict yes">Job: waiting for you</div>
 </div>
</div>
<div class="bottom">
 <div class="line">Same missed call.<br>Only one is still a job.</div>
 <div class="cta">Book a free call <span>&rarr;</span></div>
</div>
</body></html>'''.replace('@PH@', PH % (22,22)).replace('@VM@', VM % (24,24)).replace('@MSG@', MSG % (22,22))

open('ravara-ig4-meme-a.html','w').write(A)
open('ravara-ig4-meme-b.html','w').write(B)
