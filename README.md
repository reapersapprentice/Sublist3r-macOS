<h1 align="center">Sublist3r <sub>· for macOS</sub></h1>

<p align="center"><b>Discover a domain's subdomains fast — from your Mac.</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS-000000?logo=apple&logoColor=white" alt="macOS">
  <img src="https://img.shields.io/badge/Intel%20%26%20Apple%20Silicon-supported-success" alt="Apple Silicon & Intel">
  <img src="https://img.shields.io/badge/license-GPL--2.0-blue" alt="license">
  <img src="https://img.shields.io/badge/beginner-friendly-ff69b4" alt="beginner friendly">
</p>

<p align="center">
  <img src="demo.png" alt="Sublist3r running natively on macOS" width="640">
</p>

---

## ✨ What is this?

Point it at a domain and it rapidly enumerates the subdomains that are visible across search engines and public sources — a staple of the reconnaissance phase.

This repository is a **macOS-ready conversion** — packaged so it runs on an Apple
Mac (Intel **or** Apple Silicon) without needing a Linux computer or a virtual
machine. This is an independent macOS conversion by **C.Studva**. The underlying program is open-source software distributed under the GNU General Public License; that license is kept in this repository (see `LICENSE`/`COPYING` and `NOTICE`).

## 🚀 Quick start

Open the **Terminal** app (press **Cmd ⌘ + Space**, type *Terminal*, hit Return),
then:

### 1. Get the files onto your Mac

```bash
git clone https://github.com/reapersapprentice/Sublist3r-macOS.git
cd Sublist3r-macOS
```

### 2. Install what it needs (one time)

```bash
pip3 install -r requirements.txt
```

### 3. Run it

```bash
python3 sublist3r.py -d example.com
```

(swap `example.com` for a domain you're authorized to assess)

That's it — you're running **Sublist3r** on your Mac. 🎉

## 🧰 What it can do

- Fast subdomain discovery across many public sources
- Optional brute-force mode for deeper coverage
- Simple, single-command output you can feed into other tools

## 💻 What you need

- A Mac (macOS 12 or newer) — Intel or Apple Silicon
- Python 3 (already on macOS)

## 🆘 New to the Terminal? Read this (30 seconds)

- The **Terminal** is just a window where you type commands. Nothing here can hurt your Mac.
- Run the commands **one line at a time**, pressing **Return** after each.
- To paste, use **Cmd ⌘ + V**.
- ⚠️ **Copy only the command itself** — never the three back-ticks around it, and
  never a line that starts with `#` (those are notes). Pasting those is the #1
  beginner mistake and causes a `parse error`.
- If a command seems stuck, it's usually just working — give it a minute.

## ⚠️ Disclaimer

**For authorized and educational use only.** Only use this against systems,
accounts or data you **own** or have **written permission** to test. You are
responsible for how you use it. See [DISCLAIMER.md](DISCLAIMER.md) for the full
terms. In short: **C.Studva, the author of this macOS conversion, is not liable**
for any damage, loss or misuse.

## 📄 License

This is an independent macOS conversion by **C.Studva**. The underlying program is open-source software distributed under the GNU General Public License; that license is kept in this repository (see `LICENSE`/`COPYING` and `NOTICE`).

## 🍎 More macOS conversions by C.Studva

Same idea — popular Linux tools, packaged to run **natively on your Mac**:

- [**Hash-Buster**](https://github.com/reapersapprentice/Hash-Buster-macOS) — identify & crack hashes in seconds
- [**theHarvester**](https://github.com/reapersapprentice/theHarvester-macOS) — OSINT emails, subdomains & names for a domain
- [**Eagle Eye**](https://github.com/reapersapprentice/EagleEye-macOS) — find someone's social profiles from a photo
- [**httptunnel**](https://github.com/reapersapprentice/httptunnel-macOS) — tunnel a data stream over HTTP

---

<p align="center"><sub>macOS conversion crafted by <b>C.Studva</b>.</sub></p>
