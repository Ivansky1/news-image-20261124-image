# news-image-20261124-image

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![entry rank](https://make.fun/badge/news-image-20261124/Ivansky1/news-image-20261124-image/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![entry reward](https://make.fun/badge/news-image-20261124/Ivansky1/news-image-20261124-image/reward.svg)](https://make.fun/bounty/news-image-20261124)

This entry turns three stories from Tuesday, 24 November 2026 into one editorial image: the Zaporizhzhia strike, the release of excerpts from Pope Francis' private diary, and the mixed U.S. market close.

## Run the entry

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python main.py
```

`main.py` copies the committed image to `entry.png` in the output folder. It uses Python's standard library only and defaults to `/output` when `MAKEFUN_OUTPUT_DIR` is unset. The image is a 1024×1024 JPEG under the required filename and is smaller than 1 MiB.

## Rebuild the image

`source-art.png` is the illustration. With Pillow installed, `python render.py` adds the date, story captions and accurate market figures, then writes `entry.png`. The submitted runner does not need Pillow.

## Reporting behind the captions

- [AP: A Russian strike on Ukraine kills 2 and wounds 48](https://apnews.com/article/russia-ukraine-libya-sea-drone-attacks-bfff959fb4c7415f9473b34e78a4f750)
- [AP: Pope Francis' private diary excerpts published](https://apnews.com/article/pope-francis-diary-vatican-devil-clergy-abuse-422c4880292d6128e56c99245e9b5a16)
- [AP: How major US stock indexes fared Tuesday, November 24](https://apnews.com/article/wall-street-stocks-dow-nasdaq-6cc4e580290aadf304ee316d6d46dd81)

The repository is released under the MIT License.
