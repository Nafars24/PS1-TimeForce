# Power Rangers Time Force — Indonesian Translation

Fan-made Indonesian translation project for **Power Rangers Time Force** on PlayStation 1.

This project aims to translate the game's text from English into natural Indonesian while preserving the original gameplay, interface, and overall feel of the game.

> 🇮🇩 **Status: In Development**

---

## 🎮 Project Status

| Component | Status |
|---|---|
| Text extraction | ✅ Complete |
| BIGLUMP identification | ✅ Complete |
| Text editing | ✅ Complete |
| Pointer / string handling | ✅ Working |
| Indonesian translation | 🟡 In Progress |
| Gameplay testing | 🟡 In Progress |
| Full game playthrough | 🟡 In Progress |
| Proofreading | ⬜ Pending |
| Final patch | ⬜ Pending |

The current translation has been successfully tested in-game and has reached at least **Level 1** without breaking gameplay.

---

## 🇮🇩 Translation Philosophy

The goal of this project is **not** to translate every sentence word-for-word.

The Indonesian translation is written to feel natural for Indonesian players while keeping the original meaning and context.

For example:

| English | Indonesian |
|---|---|
| Punch | Pukul |
| Kick | Tndg |
| Jump | Lmpt |
| Grapple & Throw | Banting + Lempar |
| Ground Thump | Hantaman Tanah |
| Electric Thump | Hantaman Listrik |
| Tornado Kick | Tendangan Tornado |

Some gameplay text uses shortened Indonesian terminology where necessary because of the game's original text-space limitations.

---

## 🛠️ Technical Information

The translation currently focuses on the game's text resources stored inside:

```text
BIGLUMP.BIN
```

The project involved:

```text
Original Game
     │
     ▼
Extract BIGLUMP.BIN
     │
     ▼
Locate text resources
     │
     ▼
Extract strings
     │
     ▼
Translate strings
     │
     ▼
Rebuild string resources
     │
     ▼
Create translated BIGLUMP.BIN
     │
     ▼
Replace resource in game image
     │
     ▼
Test in-game
```

---

## 🔧 Tools

Tools used during development include:

- CDMage
- xdelta3
- Delta Patcher
- Python
- Hex editor
- PlayStation 1 emulator

Additional custom scripts and tools may be added to this repository as development continues.

---

## 📁 Repository Structure

```text
power-rangers-time-force-id/
│
├── README.md
│
├── translation/
│   ├── PRTF_TRANSLATION_FINAL.csv
│   └── glossary.md
│
├── patches/
│   └── v1.0.0/
│       ├── PRTF-ID-v1.0.0.xdelta
│       └── README.md
│
├── tools/
│   ├── extract_text.py
│   ├── rebuild_biglump.py
│   └── apply_patch.py
│
├── docs/
│   ├── extraction.md
│   ├── translation.md
│   └── installation.md
│
└── screenshots/
    ├── before/
    └── after/
```

The repository structure may change during development.

---

## 🚀 Installation

### Requirements

You need:

- Your own original copy of the PlayStation 1 game
- A valid dump/image of the game
- CDMage
- Delta Patcher
- The `.xdelta` patch provided by this project

### Applying the Translation

1. Obtain your own legal dump of the game.
2. Extract the required `BIGLUMP.BIN` file from your game image.
3. Open **Delta Patcher**.
4. Select your original `BIGLUMP.BIN` as the **Original File**.
5. Select the project's `.xdelta` file as the **XDelta Patch**.
6. Apply the patch.
7. Replace the resulting `BIGLUMP.BIN` in your game image using CDMage.
8. Save the modified game image.
9. Run the game using an emulator or compatible PlayStation hardware.

> The patch is designed to be applied to the specific game version documented by the release. Make sure your source game matches the required version.

---

## ⚠️ Important

**Always keep a backup of your original game image and original `BIGLUMP.BIN`.**

Do not overwrite your original files.

Recommended:

```text
game/
├── ORIGINAL/
│   └── BIGLUMP.BIN
│
└── MODDED/
    └── BIGLUMP.BIN
```

---

## 🧪 Testing

The translation is being tested through actual gameplay rather than only checking the extracted text.

Testing includes:

- Main menu
- Options
- Controller configuration
- Character selection
- Training
- Gameplay
- Special moves
- Tutorial text
- Mission text
- Pause menu
- Level progression
- Dialogues
- End-of-level screens

The game has currently been successfully tested through **Level 1**.

Full-game testing is still in progress.

---

## 📝 Translation Notes

Some strings in the original game have strict space or formatting limitations.

Because of this, certain Indonesian words may use abbreviations.

Examples:

```text
Kick → Tndg
Jump → Lmpt
```

This is intentional and is done to prevent text overflow and preserve game stability.

The glossary is used to maintain consistent terminology throughout the entire game.

---

## 📖 Glossary

The translation glossary is maintained separately in:

```text
translation/glossary.md
```

It contains standardized translations for:

- Gameplay actions
- Special moves
- Menu terminology
- Character-related terminology
- Items
- Objectives
- System messages

New terminology will be added as the game is tested.

---

## 🐛 Bug Reports

If you encounter a problem while using the translation, please provide:

1. Game version / region
2. Emulator or hardware
3. Exact location in the game
4. Screenshot or video if possible
5. Description of the problem

Examples of useful reports:

```text
[BUG]

Location:
Level 3 — Training Area

Problem:
Text is cut off on the right side.

Expected:
Full sentence should be visible.

Screenshot:
attached
```

---

## 💬 Translation Feedback

Suggestions regarding translation quality are welcome.

In particular, please report:

- Awkward Indonesian
- Incorrect context
- Typographical errors
- Inconsistent terminology
- Text overflow
- Incorrect button descriptions
- Translation that changes the original meaning

The goal is to make the Indonesian version feel like a proper localization rather than a literal machine translation.

---

## 📌 Versioning

Release versions will follow:

```text
vMAJOR.MINOR.PATCH
```

Example:

```text
v1.0.0
```

### Development

```text
v0.x
```

Experimental builds and testing versions.

### Final

```text
v1.0.0
```

First stable full-game Indonesian translation.

---

## 📦 Patches

Translation patches are distributed as **xdelta patches**.

Example:

```text
patches/
└── v1.0.0/
    ├── PRTF-ID-v1.0.0.xdelta
    └── README.md
```

The patch is intended to modify files from the corresponding original game version.

---

## ⚖️ Disclaimer

This is an unofficial, fan-made translation project.

**Power Rangers Time Force** and its related characters, names, trademarks, and game content are property of their respective copyright and trademark holders.

This project is not affiliated with, endorsed by, or sponsored by the original developers, publishers, or rights holders.

This repository does **not** distribute the original game ROM, ISO, or other copyrighted game assets.

Users are responsible for obtaining and using their own copy of the original game.

---

## ❤️ Credits

### Translation
Naufal Alfarisi

### ROMHacking / Technical
Naufal Alfarisi

### Tools

- CDMage
- xdelta3
- Delta Patcher
- Python

---

## ⭐ Support the Project

If you find this project useful:

- ⭐ Star the repository
- 🐛 Report bugs
- 💬 Suggest better translations
- 📝 Help with proofreading
- 📢 Share the project with other Indonesian ROMhacking enthusiasts

---

## 📜 License

The source code, scripts, documentation, and original translation work created for this project are provided under the license specified in this repository.

Game assets and copyrighted material from the original game are **not covered by this license**.
