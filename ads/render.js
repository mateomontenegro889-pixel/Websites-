// Usage: node render.js — renders each ad HTML to a 3x PNG in ../assets
const { chromium } = require('playwright');
const jobs = [['ravara-ig-feed', 1080, 1080], ['ravara-ig-story', 1080, 1920]];
(async () => {
  const b = await chromium.launch();
  for (const [name, w, h] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 3 });
    await p.goto('file://' + __dirname + '/' + name + '.html', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: __dirname + '/../assets/' + name + '.png' });
    await p.close();
  }
  await b.close();
})();
