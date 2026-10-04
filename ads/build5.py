# Ad #5: two more meme formats (1:1). C = homeowner's text thread, D = starter pack.
HEAD = '<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>'
BASE = '''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;font-family:"Inter",-apple-system,"Helvetica Neue",sans-serif;-webkit-font-smoothing:antialiased;color:#0a0a0a}
body{position:relative;overflow:hidden}
.cta{display:inline-flex;align-items:center;gap:14px;background:#0a0a0a;color:#fff;font-weight:800;border-radius:16px;font-size:30px;padding:24px 32px;flex:none}
.cta span{color:#F97316}
.bottom{position:absolute;left:60px;right:60px;bottom:52px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.punch{font-size:38px;font-weight:900;line-height:1.12;letter-spacing:-.8px}
'''

# ---------- C: the homeowner's text thread ----------
C = HEAD + BASE + '''
body{background:#fff}
.top{background:#FACC15;padding:46px 60px 40px}
.top h1{font-size:58px;font-weight:900;line-height:1.05;letter-spacing:-2px}
.top p{font-size:28px;font-weight:600;margin-top:12px}
.chat{padding:34px 60px 0;display:flex;flex-direction:column;gap:12px}
.who{text-align:center;font-size:22px;color:#8e8e93;margin-bottom:6px}.who b{color:#000;font-weight:700}
.b{max-width:76%;padding:16px 24px;font-size:36px;line-height:1.25;border-radius:30px;letter-spacing:-.3px}
.me{align-self:flex-end;background:linear-gradient(180deg,#1a8cff,#0a7aff);color:#fff;border-bottom-right-radius:8px}
.them{align-self:flex-start;background:#e9e9eb;border-bottom-left-radius:8px}
.gap{height:8px}
.b.hit{box-shadow:0 0 0 5px #dc2626}
.bottom{border-top:4px solid #0a0a0a;padding-top:26px;bottom:44px}
</style></head><body>
<div class="top"><h1>Your missed call, from<br>the homeowner&rsquo;s side.</h1><p>Calgary HVAC &amp; plumbing owners, read this one.</p></div>
<div class="chat">
 <div class="who"><b>Jess</b> &middot; Today 2:16 PM</div>
 <div class="b them">furnace still dead??</div>
 <div class="b me">yeah. called the furnace place, nobody picked up</div>
 <div class="gap"></div>
 <div class="b them">it&rsquo;s freezing in here</div>
 <div class="b me hit">called the next one on google. they&rsquo;re coming at 4</div>
 <div class="b them">ok good. book them</div>
</div>
<div class="bottom">
 <div class="punch">Text them back before<br>they call the next one.</div>
 <div class="cta">Book a free call <span>&rarr;</span></div>
</div>
</body></html>'''

# ---------- D: starter pack ----------
def ico(path, extra=''):
    return f'<svg width="74" height="74" viewBox="0 0 24 24" fill="none" stroke="#0a0a0a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" {extra}>{path}</svg>'
ICONS = {
 'phone': ico('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/><path d="M15 3a6 6 0 016 6M15 7a2 2 0 012 2"/>'),
 'snow': ico('<path d="M12 2v20M4.9 6.5l14.2 11M4.9 17.5l14.2-11M9 3.5l3 2 3-2M9 20.5l3-2 3 2"/>'),
 'cup': ico('<path d="M5 8h11v6a5 5 0 01-5 5h-1a5 5 0 01-5-5V8z"/><path d="M16 10h1.5a2.5 2.5 0 010 5H16M8 3c0 1.5 1 1.5 1 3M12 3c0 1.5 1 1.5 1 3"/>'),
 'quote': ico('<path d="M4 5h16v11H9l-5 4V5z"/><path d="M9 9.5v2M15 9.5v2"/>'),
 'vm': ico('<circle cx="6.5" cy="12" r="3.5"/><circle cx="17.5" cy="12" r="3.5"/><path d="M6.5 15.5h11"/>'),
 'gone': ico('<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 10l6 6M15 10l-6 6M9 6h6"/>', ''),
}
tiles = [('phone','Phone rings the second you&rsquo;re under a sink'),('snow','Cold snap. Phone won&rsquo;t stop'),
         ('cup','Coffee gone cold on the dash'),('quote','&ldquo;I called you four times&rdquo;'),
         ('vm','Voicemail: 0 new'),('gone','The job: gone to the next company')]
T = ''.join(f'<div class="t{" last" if i==5 else ""}">{ICONS[k]}<p>{txt}</p></div>' for i,(k,txt) in enumerate(tiles))
D = HEAD + BASE + '''
body{background:#FACC15}
.title{position:absolute;left:60px;top:56px;background:#fff;border:5px solid #0a0a0a;padding:16px 26px;font-size:50px;font-weight:900;letter-spacing:-1.6px;line-height:1.05;box-shadow:10px 10px 0 #0a0a0a}
.grid{position:absolute;left:60px;right:60px;top:240px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.t{background:#fff;border:4px solid #0a0a0a;border-radius:20px;height:290px;padding:26px 22px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:18px}
.t p{font-size:27px;font-weight:800;line-height:1.18;letter-spacing:-.5px}
.t.last{background:#0a0a0a;color:#fff}.t.last svg{stroke:#F97316}.t.last p{color:#fff}
.t.last p{font-size:28px}
</style></head><body>
<div class="title">Calgary furnace guy<br>starter pack</div>
<div class="grid">''' + T + '''</div>
<div class="bottom">
 <div class="punch">Lose the last one.<br>Your line texts back for you.</div>
 <div class="cta">Book a free call <span>&rarr;</span></div>
</div>
</body></html>'''

open('ravara-ig5-meme-c.html','w').write(C)
open('ravara-ig5-meme-d.html','w').write(D)
