---
title: Download Corepeak
description: Download the free Corepeak XPS peak-fitting app for macOS and Windows.
---

Corepeak is free and open source (GPLv3). No account, no install of Python required.

## Latest release

Get the signed installers from the **[GitHub Releases page →](https://github.com/contact993/xpsfit/releases)**.

### macOS (Apple Silicon)
1. Download the `.app.zip`, unzip it, and move **Corepeak.app** to Applications.
2. First launch: **right-click → Open → Open** (one-time, because the app isn't from the App Store).
3. If you ever see "damaged, can't be opened": run `xattr -cr "/Applications/Corepeak.app"` in Terminal, then right-click → Open.

### Windows (10 / 11, x64)
1. Download the `.zip`, extract it, and run **Corepeak.exe** from the extracted folder.
2. On the first SmartScreen prompt: **More info → Run anyway** (the reputation prompt clears as more people download).

:::note
Need an Intel-Mac or Linux build? [Open an issue](https://github.com/contact993/xpsfit/issues/new/choose) and let me know.
:::

## Run from source

```bash
git clone https://github.com/contact993/xpsfit && cd xpsfit
python -m venv .venv && . .venv/bin/activate
pip install -e .
python -m xpsfit.app
```
