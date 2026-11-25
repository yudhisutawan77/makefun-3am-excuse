# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/yudhisutawan77/makefun-3am-excuse/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/yudhisutawan77/makefun-3am-excuse/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the [make.fun bounty "The 3 AM Excuse"](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878): one line, under 200 characters, in the voice of a hardware wallet that refuses to sign a transaction at 3 AM.

## The entry

> It's 3 AM. I'm the designated driver for your life savings, and you are far too asleep to be spending them.

107 characters, one line. The wallet is the only sober one in the room — the designated driver who won't let you drive your own money home at 3 AM.

## How it works

`main.py` prints the excuse to stdout and writes it to `/output/entry.txt` (the path the harness reads), and also honours `$ENTRY_OUT` whether it names a file or a directory, plus `$ENTRY_OUT_DIR` if set.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
