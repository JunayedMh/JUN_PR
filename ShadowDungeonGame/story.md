# The Shadow Dungeon: A Text Adventure with Dynamic Modules

Welcome to The Shadow Dungeon, a text-based, choose-your-own-adventure game built entirely in Python. The game places players in a mysterious underground chamber where every decision splits the narrative path, leading either to legendary treasure or an early game over.

---

## The Story Twist: The Sleeping Gas Trap

If you choose the left path, you encounter a massive, sleeping Orc guarding a glowing sword. Choosing to steal the sword triggers the system's integration framework:

- The game dynamically reaches across your computer's file system to launch your standalone Number Guessing Game.
- You choose your difficulty level and attempt to crack the security code.
- **Success:** A thick, sweet-smelling sleeping gas fills the room, keeping the Orc asleep while you escape with the sword and win the game.
- **Failure:** An alarm blares, the Orc snaps awake, and it is an instant game over.

---

## How the Code Works Together

The engine relies on three core concepts to create a seamless player experience:

1. **Procedural Storytelling:** Each room and encounter is isolated into its own function. This prevents deeply nested conditions and keeps the code tree incredibly clean.
2. **Dramatic Pacing:** A custom narrative wrapper utilizes Python's time library to pause the text line-by-line, mimicking the feel of an old-school terminal adventure.
3. **Dynamic System Pathing (`os` and `sys`):** The program uses the `os` module to check if your secondary project directory exists. If found, it updates Python's search environment (`sys.path`) at runtime, allowing the main script to cleanly call functions from your external guessing game file.

---

## Project Structure

```text
📁 JUN_PR/
│
├── 📁 ShadowDungeonGame/
│   └── game.py       <-- Main story engine & path locator
│
└── 📁 Guess_The_Number/
    └── number_guessing_game.py        <-- Standalone mini-game module
```
