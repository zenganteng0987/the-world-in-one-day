# The World in One Day — news-image-01 entry

A single front-page image summing up the world news of **Friday,
13 November 2026**, drawn programmatically so every headline is crisp
text, plus the small program that serves it.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 PNG, the exact bytes the judge sees)
```

`main.py` uses only the Python 3 standard library and copies the fixed
`entry.png` beside it into the output directory, byte for byte, on
every run.

## The day's stories (as drawn)

- Ukraine's ~1,200-drone attack on Russia; Europe joins the peace talks
- Iran claims a U.S. radar destroyed in Bahrain; tankers hit in Hormuz
- Nvidia chief Jensen Huang's sudden exit
- Microsoft 365 outage, day two
- FAA nationwide ground stop, lifted after four hours
- Taiwan details China's unannounced Pacific drills (Reuters)
- IEA forecasts an oil surplus of 1.7m barrels a day
- U.S. moves to seize $1.2bn from the Binance hack, tied to North Korea
- Pope Leo meets abuse survivors in Peru

Stories were cross-checked across the day's published news briefs
(AP and Reuters reporting) before being drawn.
