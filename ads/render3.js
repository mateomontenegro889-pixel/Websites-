// Usage: node render3.js — renders the 5 carousel slides to 3x PNGs in ../assets
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 3 });
  for (let n = 1; n <= 5; n++) {
    await p.goto('file://' + __dirname + '/ravara-ig3-slide' + n + '.html', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: __dirname + '/../assets/ravara-ig3-slide' + n + '.png' });
  }
  await b.close();
})();
