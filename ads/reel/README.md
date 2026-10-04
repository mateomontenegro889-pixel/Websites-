# Ravara Reel: "Answering your own phone OR letting your line text them back"

Output: `assets/ravara-reel-meme.mp4`. 1080x1920, 30 fps, 12.5 s, no audio (add a trending sound in Instagram).

Rebuild: `node render-reel.js` (writes frames/), then
`ffmpeg -framerate 30 -i frames/f%04d.jpg -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart ../../assets/ravara-reel-meme.mp4`

Photos (`photo-top.png`, `photo-bottom.png`) are cropped from the original Ravara meme post. Swap in
higher-resolution originals with the same names for a sharper result.

## Timeline
- 0.0 s: "ANSWERING YOUR OWN PHONE ON A JOB:" + frustrated photo; incoming call banner shakes
- 2.4 s: banner flips to **Missed call**
- 2.8 s: OR
- 3.1 s: "LETTING YOUR LINE TEXT THEM BACK:" + relaxed photo; customer's reply types in:
  "Furnace quit, house is down to 12. Can someone come today?"
- 6.1 s: JOB SAVED stamp
- 7.6 s: end card: "Missed a call? Still book the job." + Book a free call

## Caption
Answering your own phone on a job vs. letting your line text them back.

Calgary HVAC and plumbing owners: every missed call gets a text back in seconds, from your business,
in your name. They reply while you finish the job. The job waits for you.

No app. No new number. Nothing for you to do.
Book a free call. Link in bio.

#yyc #yychvac #calgaryplumbing #calgaryhvac #hvaclife #plumbinglife #airdrie #okotoks
