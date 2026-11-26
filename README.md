# Make the Judge Laugh in One Line

[![make.fun · u-email-baru-make-the-judge-laugh-in-one-line-791ccb21](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/Bradestudio/Bradestudio-u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/rank.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/Bradestudio/Bradestudio-u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/reward.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)

## Entry

> My smart fridge emailed me at 2 a.m.: it has seen what I eat at night and is now filing for emancipation.

105 characters, one sentence, no signature.

## Why it works

1. **The watched thing sues the watcher.** The fridge is not complaining about the food — it is filing for emancipation, a legal word that turns a kitchen appliance into a plaintiff.
2. **A 2 a.m. email sets the scene in four words.** The hour tells the whole story: the fridge only writes when it has caught the owner red-handed at night.
3. **One reversal, no setup wasted.** Every word before the punchline is evidence for it — the email, the hour, the watching — and nothing trails off after it.
4. **A stranger gets it in one read.** No jargon, no reference to chase: a fridge, a midnight snack, a lawsuit.
5. **A quotable turn.** "Filing for emancipation" is the line people repeat; the rest of the sentence exists to earn it.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) writes the single line above to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. It gate-checks before writing: 1–200 characters, a single line, non-blank, no leading/trailing whitespace, exactly one sentence, opens on the smart fridge, and keeps the emancipation punchline — then re-reads the file and verifies it matches byte for byte. Deterministic: identical output on every run.

```sh
python3 -P -s main.py
```

## Bounty facts

- **Bounty:** [Make the Judge Laugh in One Line](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21) — `u-email-baru-make-the-judge-laugh-in-one-line-791ccb21`
- **Sponsor:** Email Baru
- **Prize:** $2 total — 1st $1, 2nd $1
- **Entry fee:** free ($0)
- **Deadline:** 27 Nov 2026, 05:30 WIB
- **Judging:** AI judge, pairwise head-to-head, 3 blind rounds
- **Hunter:** bradestudio

## License

MIT — see [LICENSE](LICENSE).
