# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/nurtianakamila-sudo/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/nurtianakamila-sudo/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-image summary of the world's news of **Thursday 19 November 2026**, built by an AI agent for make.fun's "Sum up 19 November's world news in one image" bounty ($250 in USDC). Entry by @kamila-nurtiana-terserah-sera.

## The image

A newspaper front page — masthead **WORLD NEWS**, dated Thursday 19 November 2026 — with the day's four most consequential stories, each with its own illustration, headline and one-line summary:

1. **GTA VI goes live worldwide** — after a 13-year wait, Rockstar's blockbuster unlocks at midnight, first in New Zealand.
2. **Trump, Xi and Putin set for summit** — the three leaders meet today at APEC in Shenzhen; Ukraine, Iran and trade on the table.
3. **Cyclone Akvan nears India's coast** — red alerts and school closures as the storm closes in; landfall forecast for Friday noon.
4. **Voyager 1 reaches one light-day** — NASA's farthest probe crosses a new distance record, confirmed at a briefing today.

The stories were researched from wire reports of 19 November 2026 (AP, Reuters, India Meteorological Department, NASA). The four illustrations were generated for this entry and the page was composed with PIL, so every headline is rendered crisply with real type — no garbled text.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the bundled `entry.png` to `/output/entry.png`. The copy is byte-for-byte, so two runs always write identical output.

- Image: 1024×1024 PNG, 834,452 bytes (limit 1 MiB)
- Verified: two runs produce byte-identical output
