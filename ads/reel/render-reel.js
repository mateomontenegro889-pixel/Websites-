// Usage: node render-reel.js — renders reel.html frame-by-frame, then encode with ffmpeg
const { chromium } = require('playwright');
const FPS = 30, DURATION = 12.5;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/reel.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const n = Math.round(FPS * DURATION);
  for (let i = 0; i < n; i++) {
    const t = (i / FPS) * 1000;
    await p.evaluate(t => document.getAnimations().forEach(a => { a.currentTime = t; }), t);
    await p.screenshot({ path: __dirname + '/frames/f' + String(i).padStart(4, '0') + '.jpg', type: 'jpeg', quality: 95 });
  }
  await b.close();
})();
