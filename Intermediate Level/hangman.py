#!/usr/bin/env python3
import random
import string
from dataclasses import dataclass

# ---------- WORD BANK (word, category, hint) ----------
# Add more tuples or swap in your own!
WORD_BANK = [
    ("python", "Programming", "A popular snake… and a language."),
    ("algorithm", "Computer Science", "A step-by-step procedure to solve a problem."),
    ("binary", "Computer Science", "A way of representing data using 0 and 1."),
    ("keyboard", "Hardware", "You’re tapping it right now."),
    ("umbrella", "Everyday", "Opens when it pours."),
    ("astronomy", "Science", "Study of celestial objects."),
    ("photosynthesis", "Biology", "Plants’ trick to turn light into food."),
    ("mountain", "Geography", "High elevation landform."),
    ("ocean", "Geography", "Covers ~70% of Earth."),
    ("notebook", "Stationery", "You write in it; laptops are also called this."),
    ("hangman", "Game", "You’re playing it!"),
]

# ---------- VISUALS ----------
HANGMAN_PICS = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]

@dataclass
class GameConfig:
    max_wrong: int = len(HANGMAN_PICS) - 1
    max_hints: int = 2
    reveal_on_hint: bool = True  # also reveal one random hidden letter on hint

def pick_word():
    return random.choice(WORD_BANK)

def masked_word(word: str, guessed: set[str]) -> str:
    return " ".join(ch if ch in guessed else "_" for ch in word)

def get_hidden_indices(word: str, guessed: set[str]) -> list[int]:
    return [i for i, ch in enumerate(word) if ch not in guessed]

def show_state(wrong: int, cfg: GameConfig, word: str, guessed: set[str], bad: set[str], category: str, hints_left: int):
    print(HANGMAN_PICS[wrong])
    print(f"\nCategory: {category}")
    print(f"Hints left: {hints_left}")
    print(f"\nWord:  {masked_word(word, guessed)}")
    if bad:
        print("Wrong letters:", " ".join(sorted(bad)))
    print()

def use_hint(word: str, hint: str, guessed: set[str], cfg: GameConfig) -> str | None:
    # Reveal one random hidden letter if enabled
    reveal_letter = None
    if cfg.reveal_on_hint:
        hidden = [c for c in set(word) if c not in guessed and c in string.ascii_lowercase]
        if hidden:
            reveal_letter = random.choice(hidden)
            guessed.add(reveal_letter)
    print("\n💡 HINT:", hint)
    if reveal_letter:
        print(f"➡️ Auto-revealed a letter: '{reveal_letter}'")
    print()
    return reveal_letter

def get_input(valid_letters: set[str]) -> str:
    raw = input("Guess a letter (or type 'hint'): ").strip().lower()
    if raw == "hint":
        return "hint"
    if len(raw) != 1 or raw not in valid_letters:
        print("Please enter a single letter (a–z) or 'hint'.\n")
        return ""
    return raw

def play_one_game(cfg: GameConfig):
    word, category, hint = pick_word()
    word = word.lower()

    guessed: set[str] = set()
    bad: set[str] = set()
    wrong = 0
    hints_left = cfg.max_hints
    alphabet = set(string.ascii_lowercase)

    # Pre-reveal spaces/hyphens etc. (if you add such words)
    for ch in word:
        if ch not in string.ascii_lowercase:
            guessed.add(ch)

    print("\n=== HANGMAN ===")
    print("Type letters to guess. Type 'hint' to get a clue.")
    print(f"You can make up to {cfg.max_wrong} wrong guesses.\n")

    while True:
        show_state(wrong, cfg, word, guessed, bad, category, hints_left)

        # Check win
        if all(ch in guessed or ch not in string.ascii_lowercase for ch in word):
            print("🎉 You guessed it!")
            print(f"The word was: {word}\n")
            break

        # Check lose
        if wrong >= cfg.max_wrong:
            print("💀 Game over!")
            print(f"The word was: {word}\n")
            break

        # Read input
        move = get_input(alphabet)
        if not move:
            continue

        if move == "hint":
            if hints_left > 0:
                hints_left -= 1
                use_hint(word, hint, guessed, cfg)
            else:
                print("No hints left!\n")
            continue

        if move in guessed or move in bad:
            print("You already tried that letter.\n")
            continue

        # Apply guess
        if move in word:
            guessed.add(move)
            # Reveal all occurrences; guessed set is sufficient
            print(f"✅ Nice! '{move}' is in the word.\n")
        else:
            bad.add(move)
            wrong += 1
            print(f"❌ Sorry, '{move}' is not in the word.\n")

def main():
    cfg = GameConfig()
    while True:
        play_one_game(cfg)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
