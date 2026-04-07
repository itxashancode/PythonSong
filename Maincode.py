"""
Python Song 1.0 — Terminal Lyric Player
Author: itxashancode
GitHub: https://github.com/itxashancode/Python-Song1.0
"""
__version__ = "1.0.0"

import time
import random
import sys
import os
import argparse

# --- Terminal Colors ---
class Colors:
    HEADER    = "\033[95m"
    CYAN      = "\033[96m"
    BLUE      = "\033[94m"
    GREEN     = "\033[92m"
    YELLOW    = "\033[93m"
    RED       = "\033[91m"
    END       = "\033[0m"
    BOLD      = "\033[1m"
    MAGENTA   = "\033[35m"
    LIGHTCYAN = "\033[36m"   # Fix: was \033[96m (duplicate of CYAN)
    ORANGE    = "\033[33m"
    LIGHTGREEN= "\033[92m"
    PURPLE    = "\033[95m"   # Fix: was \033[35m (duplicate of MAGENTA)
    LIGHTBLUE = "\033[34m"   # Fix: was \033[94m (duplicate of BLUE)

# --- Utility: Clear Screen ---
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# --- Utility: Typewriter Effect ---
def type_text(text, min_delay=0.03, max_delay=0.08, color=Colors.END, bounce=False, newline=True):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        if bounce:
            time.sleep(random.uniform(min_delay, max_delay) * random.uniform(0.5, 1.5))
        else:
            time.sleep(random.uniform(min_delay, max_delay))
    if newline:
        print()

# --- Animation: Music Notes ---
def music_notes_effect():
    print(Colors.BOLD + Colors.PURPLE + "🎵" + Colors.END, end=" ")
    for _ in range(3):
        notes = ["♪", "♫", "🎶"]
        for note in notes:
            sys.stdout.write(Colors.LIGHTBLUE + note + " " + Colors.END)
            sys.stdout.flush()
            time.sleep(0.08)
    print(Colors.BOLD + Colors.PURPLE + "🎵" + Colors.END)

# --- Animation: Pulsing Effect ---
def pulse_effect(text, pulses=3):
    for i in range(pulses):
        if i % 2 == 0:
            sys.stdout.write(Colors.BOLD + Colors.YELLOW + text + Colors.END)
        else:
            sys.stdout.write(Colors.BOLD + Colors.ORANGE + text + Colors.END)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\b" * len(text))

# --- Animation: Loading Bar ---
def loading_bar(duration=3, width=30):
    print(Colors.CYAN + "[", end="")
    for i in range(width):
        sys.stdout.write("▰")
        sys.stdout.flush()
        time.sleep(duration / width)
    print("]" + Colors.END)

# --- Lyrics Display Function ---
def play_lyrics(speed=1.0):
    lyrics = [
        # Intro
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",

        # Verse 1
        "Jadon vi tenu dekhan aaya...",
        "Meri akhiyan ne keha...",
        "Tu hi meri jaan, tu hi meri duniya...",
        "Tu hi meri har khushi...",

        # Pre-Chorus
        "Main taan tere kol rehna...",
        "Tere naal guzarna...",
        "Saari zindagi...",

        # Chorus
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",

        # Verse 2
        "Teri muskurahat dekh ke...",
        "Mera dil dhadakda hai...",
        "Teri baaton mein hai woh jaadu...",
        "Jo mujhe bandh ta hai...",

        # Chorus Repeat
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",

        # Bridge
        "Har din tera intezar...",
        "Har raat teri yaad...",
        "Tere bina adhoori hai...",
        "Meri har ek saans...",

        # Musical Interlude
        "Ohhh... Talwiinder...",
        "Meri jaan...",
        "Ohhh... Talwiinder...",
        "Meri duniya...",

        # Final Chorus
        "Tu Talwiinder, mainu pata si...",
        "Tu milegi kade na kade...",
        "Main sochda si, main sochda si...",
        "Tu milegi kade na kade...",

        # Outro
        "Talwiinder...",
        "Meri Talwiinder...",
        "Tu milegi...",
        "Haan tu milegi...",
        "Kade na kade..."
    ]

    verse_delays = [
        2.0, 1.8, 2.2, 2.0,
        1.7, 1.5, 2.0, 1.8,
        1.6, 1.4, 1.2,
        2.0, 1.8, 2.2, 2.0,
        1.7, 1.5, 1.8, 1.6,
        2.0, 1.8, 2.2, 2.0,
        1.8, 1.6, 1.7, 1.5,
        2.5, 2.0, 2.5, 2.0,
        2.0, 1.8, 2.2, 2.0,
        2.5, 2.0, 1.8, 1.5, 2.0
    ]

    verse_colors = [
        Colors.LIGHTBLUE, Colors.CYAN,      Colors.LIGHTCYAN, Colors.BLUE,
        Colors.GREEN,     Colors.LIGHTGREEN, Colors.YELLOW,    Colors.ORANGE,
        Colors.MAGENTA,   Colors.PURPLE,     Colors.RED,
        Colors.LIGHTBLUE, Colors.CYAN,      Colors.LIGHTCYAN, Colors.BLUE,
        Colors.GREEN,     Colors.LIGHTGREEN, Colors.YELLOW,    Colors.ORANGE,
        Colors.LIGHTBLUE, Colors.CYAN,      Colors.LIGHTCYAN, Colors.BLUE,
        Colors.MAGENTA,   Colors.PURPLE,     Colors.RED,       Colors.ORANGE,
        Colors.YELLOW,    Colors.LIGHTGREEN, Colors.YELLOW,    Colors.LIGHTGREEN,
        Colors.LIGHTBLUE, Colors.CYAN,      Colors.LIGHTCYAN, Colors.BLUE,
        Colors.PURPLE,    Colors.MAGENTA,    Colors.LIGHTBLUE, Colors.CYAN, Colors.LIGHTCYAN
    ]

    clear_screen()

    # Title display
    print(Colors.BOLD + Colors.HEADER + "═" * 60 + Colors.END)
    type_text("🎶 NOW PLAYING: SANJOY - TU TALWIINDER 🎶",
              0.05, 0.1, Colors.HEADER, bounce=True)
    print(Colors.BOLD + Colors.HEADER + "═" * 60 + Colors.END)
    print()
    time.sleep(1.5)

    # Loading animation
    print(Colors.YELLOW + "📻 Loading 'Tu Talwiinder' by Sanjoy..." + Colors.END)
    print(Colors.CYAN + "   Music Status: ", end="")
    pulse_effect("LOADING", 4)
    print()
    loading_bar(2.5 / speed)
    print()

    # Music Notes Animation
    music_notes_effect()
    print()

    # Print each lyric
    for i, line in enumerate(lyrics):

        # Section dividers
        if i in [0, 4, 8, 11, 15, 19, 23, 28, 32, 36]:
            print(Colors.BOLD + Colors.PURPLE + "\n┅┅┅┅┅┅┅┅┅┅ ♪ ┅┅┅┅┅┅┅┅┅┅\n" + Colors.END)
            time.sleep(0.7 / speed)

        color = verse_colors[i] if i < len(verse_colors) else Colors.END
        delay = (verse_delays[i] if i < len(verse_delays) else 1.5) / speed

        # Chorus lines — bounce mode
        if i in [11, 12, 13, 14, 19, 20, 21, 22, 32, 33, 34, 35]:
            type_text(line, 0.04, 0.08, color, bounce=True)
            if "Talwiinder" in line:
                time.sleep(0.3 / speed)
            print()  # Fix: replaced dead-code color print with actual spacer

        # Interlude — indented
        elif i in [28, 29, 30, 31]:
            type_text("   " + line, 0.06, 0.12, color)

        # Outro — slow fade
        elif i in [36, 37, 38, 39]:
            type_text(line, 0.07, 0.15, color)

        else:
            type_text(line, 0.04, 0.09, color)

        time.sleep(delay)

    # End screen
    print("\n" + Colors.BOLD + Colors.PURPLE + "┅" * 30 + Colors.END)
    print(Colors.BOLD + Colors.GREEN + "🎧 Song Complete - Sanjoy 'Tu Talwiinder' 🎧" + Colors.END)

    print("\n" + Colors.LIGHTBLUE + "🎵 ", end="")
    for _ in range(3):
        for note in ["♪", "♫", "🎶"]:
            sys.stdout.write(Colors.PURPLE + note + " " + Colors.END)
            sys.stdout.flush()
            time.sleep(0.3)
    print(Colors.BOLD + Colors.LIGHTBLUE + " THE END" + Colors.END)
    print()

    # Replay prompt
    again = input(Colors.CYAN + "🔁 Play again? (y/n): " + Colors.END).strip().lower()
    if again == 'y':
        play_lyrics(speed)

# --- Argument Parser ---
def parse_args():
    parser = argparse.ArgumentParser(
        description="Python Song 1.0 — Terminal Lyric Player"
    )
    parser.add_argument(
        "--fast", action="store_true",
        help="Play lyrics at 3x speed"
    )
    parser.add_argument(
        "--speed", type=float, default=1.0, metavar="X",
        help="Playback speed multiplier (e.g. --speed 2.0 for 2x faster)"
    )
    return parser.parse_args()

# --- Entry Point ---
if __name__ == "__main__":
    args = parse_args()
    speed = 3.0 if args.fast else args.speed

    try:
        play_lyrics(speed)
    except KeyboardInterrupt:
        print("\n\n" + Colors.RED + "⏹️  Playback stopped by user" + Colors.END)
        sys.exit(0)
