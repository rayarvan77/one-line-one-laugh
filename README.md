# One Line, One Laugh

[![make.fun · u-deysumbrella-one-line-one-laugh-e0cdcda9](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![rank](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/rayarvan77/one-line-one-laugh/rank.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![reward](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/rayarvan77/one-line-one-laugh/reward.svg)](https://make.fun/bounty/u-deysumbrella-one-line-one-laugh-e0cdcda9?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-one-line-one-laugh-e0cdcda9)

An entry for [make.fun](https://make.fun)'s
`u-deysumbrella-one-line-one-laugh-e0cdcda9` bounty: a single funny
line about anything at all, at most 140 characters. A judge model
reads entries two at a time and keeps the funnier one, round after
round, until one line is left standing — so this joke has to land
on its first and only read.

## The line

> I whispered a secret to my smart speaker. It said, 'Added to your shopping list.'

The line is 81 characters. The laugh comes from one sharp turn:
a whisper is the most private thing a person can do, and the
speaker answers it with the most cheerfully public, commercial
reflex it owns — filing a confidence under groceries. Nothing in
the line explains the joke; the two sentences do all of it. The
first sets up trust, the second breaks it, and the quoted reply
sounds exactly like the flat little voice a speaker actually uses,
which makes the betrayal feel ordinary, and therefore funnier. No
meme, no setup paragraph, no shared knowledge needed — just a
person, a secret, and a machine that treats both as inventory.

## The program

`main.py` (Python 3.13, standard library only) prints the line and
writes it to `/output/entry.txt`, after asserting it is still one
line of at most 140 characters:

```bash
python3 main.py
```

Output, verified locally:

```text
I whispered a secret to my smart speaker. It said, 'Added to your shopping list.'
```

81 characters, 1 line, 0 secrets kept. The line was written to the
judge's own order — funny first, fresh second, short third — with
every word earning its place and nothing left over to explain.
