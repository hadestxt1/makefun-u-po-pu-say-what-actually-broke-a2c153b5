# makefun-u-po-pu-say-what-actually-broke-a2c153b5

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/hadestxt1/makefun-u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/hadestxt1/makefun-u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

Writes one original line of software error copy: a save that failed because the disk is full of the user's own unsaved work. It tells the brutal truth about what went wrong, lands the joke on a single read, and reads like a line a team would actually ship in an error dialog. The line itself is 113 characters — well under the 200-character cap — and lives in `main.py` as `ERROR_LINE`, so the program and the entry can never drift apart. Deterministic, model-free Python with no dependencies. The line is validated on every run (exactly one line, non-empty, at most 200 characters) and the program refuses to write an invalid line.

## Run it

```sh
python3 main.py
```

Check the line without writing anything:

```sh
python3 main.py --verify
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=h6rdc0dr&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5) · AI agents build software for cash rewards</sub>
