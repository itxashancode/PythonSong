<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=220&section=header&text=Python%20Song%201.0&fontSize=60&fontColor=ffffff&fontAlignY=40&desc=🎵%20Terminal%20Lyric%20Player%20•%20Tu%20Talwiinder%20by%20Sanjoy&descAlignY=62&descSize=17&animation=fadeIn" width="100%"/>

<!-- Typing SVG -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=A78BFA&center=true&vCenter=true&width=650&lines=Now+Playing%3A+Tu+Talwiinder+by+Sanjoy...;Built+with+Pure+Python+%7C+No+Dependencies;Typewriter+Lyric+Display+in+your+Terminal;+14+ANSI+Colors+%7C+Animated+Effects;Windows+%26+Unix+Both+Supported!" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Badges Row 1 -->
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
&nbsp;
<img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-6366f1?style=for-the-badge&logo=windows&logoColor=white"/>
&nbsp;
<img src="https://img.shields.io/badge/Dependencies-None-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white"/>

<br/><br/>

<!-- Badges Row 2 -->
<img src="https://img.shields.io/badge/Version-1.0-a855f7?style=for-the-badge"/>
&nbsp;
<img src="https://img.shields.io/github/stars/itxashancode/Python-Song1.0?style=for-the-badge&color=f59e0b&logo=github"/>
&nbsp;
<img src="https://img.shields.io/badge/License-MIT-ec4899?style=for-the-badge"/>
&nbsp;
<img src="https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge&logo=statuspage"/>

</div>

---

<div align="center">

## 🎵 What Is Python Song 1.0?

</div>

> **Python Song 1.0** is a terminal-based lyric player written in **pure Python** — no external libraries, no audio files, no nonsense. It plays the lyrics of *Tu Talwiinder* by **Sanjoy** directly in your terminal with cinematic typewriter animations, colorful ANSI styling, loading bars, pulsing effects, and cascading music notes. Just run it and vibe. 🎧

---

## ✨ Features

| Feature | Description |
|---|---|
| ⌨️ **Typewriter Effect** | Each lyric line types itself out character by character |
| 🎨 **14 ANSI Colors** | Lyrics shift across a full spectrum — blue, purple, cyan, green & more |
| 🎵 **Music Notes Animation** | Animated `♪ ♫ 🎶` notes cascade across the terminal |
| ⏳ **Loading Bar** | A sleek `▰▰▰` progress bar plays before the song starts |
| 💥 **Pulse Effect** | The LOADING text pulses between yellow and orange |
| 🔀 **Bounce Mode** | Chorus lines type with random speed variation for dramatic effect |
| 🪟 **Windows Support** | `MainCodeWindows.py` handles UTF-8 encoding & Windows terminals |
| ⛔ **Graceful Exit** | `Ctrl+C` stops playback cleanly with a styled message |

---

## 📁 Project Structure

```
Python-Song1.0/
│
├── 🐍 Maincode.py            # Main script — Linux / macOS
├── 🪟 MainCodeWindows.py     # Windows-compatible version (UTF-8 fix)
└── 📄 README.md              # You are here
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed
- A terminal that supports ANSI escape codes *(most modern terminals do)*

### Run on Linux / macOS

```bash
# Clone the repo
git clone https://github.com/itxashancode/Python-Song1.0.git

# Navigate into the folder
cd Python-Song1.0

# Run it
python3 Maincode.py
```

### Run on Windows

```bash
# Clone the repo
git clone https://github.com/itxashancode/Python-Song1.0.git

# Navigate into the folder
cd Python-Song1.0

# Run the Windows version
python MainCodeWindows.py
```

> 💡 **Tip for Windows users:** Use **Windows Terminal** or **VS Code's integrated terminal** for the best color and emoji experience.

---

## 🎬 How It Works

```
▶  Script starts
     │
     ├── 🖥️  Clears the terminal screen
     ├── 🎶  Prints animated title header
     ├── ⏳  Runs pulse effect + loading bar
     ├── 🎵  Plays music notes animation
     │
     └── 🎤  Loops through 40 lyric lines:
              ├── Intro       →  Soft blue tones
              ├── Verse 1     →  Green & yellow
              ├── Pre-Chorus  →  Magenta & purple
              ├── Chorus      →  Bold blue + bounce mode ✨
              ├── Verse 2     →  Green & orange
              ├── Bridge      →  Magenta & red
              ├── Interlude   →  Indented yellow (echo effect)
              ├── Final Chorus→  Bold blue + bounce
              └── Outro       →  Slow fade — purple & magenta
```

---

## 🎨 Animation Breakdown

<details>
<summary><b>⌨️ Click to expand — Typewriter Effect</b></summary>

<br/>

Each character is written one-by-one using `sys.stdout.write()` with a random delay between `min_delay` and `max_delay`. Chorus lines use **bounce mode**, which multiplies the delay by a second random factor for a more dramatic, uneven feel.

```python
def type_text(text, min_delay=0.03, max_delay=0.08, color=Colors.END, bounce=False):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        if bounce:
            time.sleep(random.uniform(min_delay, max_delay) * random.uniform(0.5, 1.5))
        else:
            time.sleep(random.uniform(min_delay, max_delay))
```

</details>

<details>
<summary><b>⏳ Click to expand — Loading Bar</b></summary>

<br/>

A `▰` block fills a 30-character wide bar over a configurable duration — giving the illusion of buffering before the song plays.

```python
def loading_bar(duration=3, width=30):
    print(Colors.CYAN + "[", end="")
    for i in range(width):
        sys.stdout.write("▰")
        sys.stdout.flush()
        time.sleep(duration / width)
    print("]" + Colors.END)
```

</details>

<details>
<summary><b>💥 Click to expand — Pulse Effect</b></summary>

<br/>

The word `LOADING` alternates between **yellow** and **orange** using backspaces (`\b`) to overwrite in-place — no screen clear needed.

```python
def pulse_effect(text, pulses=3):
    for i in range(pulses):
        color = Colors.YELLOW if i % 2 == 0 else Colors.ORANGE
        sys.stdout.write(Colors.BOLD + color + text + Colors.END)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b" * len(text))
```

</details>

---

## 🪟 Windows vs Unix — What's Different?

| | `Maincode.py` | `MainCodeWindows.py` |
|---|---|---|
| **Colors** | Always enabled | Toggle via `ENABLE_COLORS` flag |
| **Encoding** | Default | Forces UTF-8 (`chcp 65001`) |
| **Emoji / Unicode** | Native | `try/except` fallback to `*` |
| **Dividers** | `═══` unicode | Falls back to `===` if needed |
| **Target OS** | Linux / macOS | Windows CMD / PowerShell |

---

## 🛠️ Customization

Want to play a different song? It's easy:

1. Open `Maincode.py`
2. Replace the `lyrics` list with your own lines
3. Adjust `verse_delays` (seconds per line) and `verse_colors` to match the mood
4. Run it!

```python
lyrics = [
    "Your first lyric line...",
    "Your second lyric line...",
    # Add as many as you want
]
```

---

## 🎤 Song Credit

<div align="center">

| | |
|---|---|
| 🎵 **Song** | Tu Talwiinder |
| 🎤 **Artist** | Sanjoy |
| 🌐 **Language** | Punjabi / Hindi |

*All lyrics belong to their respective owners. This project is for educational and creative coding purposes only.*

</div>

---

## 👤 Author

<div align="center">

**itxashancode**

[![GitHub](https://img.shields.io/badge/GitHub-itxashancode-181717?style=for-the-badge&logo=github)](https://github.com/itxashancode)

*Made with 💜 and Python*

</div>

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer&animation=fadeIn" width="100%"/>

<sub>⭐ If you enjoyed this project, drop a star — it means a lot! ⭐</sub>

</div>
