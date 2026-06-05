# 🧪 Karel's Potion Shop

> *Karel the robot wants to become a prince. You are the witch. Choose wisely.*

A whimsical potion-brewing game built in Python — my final project for [Stanford Code in Place 2026](https://codeinplace.stanford.edu/).

![Python](https://img.shields.io/badge/Python-3.x-blue) ![tkinter](https://img.shields.io/badge/GUI-tkinter-purple) ![No installs](https://img.shields.io/badge/dependencies-none-green)

---

## 🎮 How to Play

1. Pick **3 ingredients** from the shelf (repeats allowed)
2. Press **BREW POTION**
3. Watch what happens to Karel
4. Find the one combo that turns Karel into a prince 👑

---

## ▶️ How to Run

No installs needed. tkinter comes built into Python.

```bash
python karel_potion_tkinter.py
```

That's it.

---

## 🌿 The Ingredients

| # | Ingredient | Key |
|---|---|---|
| 1 | 👁️ Eye of Newt | newt |
| 2 | 🦄 Tears of Unicorn | unicorn |
| 3 | 🎩 Leprechaun's Hat | hat |
| 4 | 🌿 Wolfsbane | wolf |
| 5 | 🔮 Mermaid's Core | mermaid |

---

## 🔢 The Math

- 5 ingredients, pick 3, **repeats allowed**, **order doesn't matter**
- That's **35 unique combinations** (multiset coefficient: C(5+3-1, 3))
- Every single one is defined in the `POTIONS` dictionary
- Only **one** combination makes Karel a prince

---

## 🧠 How the Code Works

The whole game runs on one core trick:

```python
# Sort the picks so order doesn't matter
combo_key = tuple(sorted(picks))

# Look it up in the dictionary
potion_name, effect, karel_state = POTIONS[combo_key]
```

`("newt", "hat", "unicorn")` and `("unicorn", "newt", "hat")` both sort to `("hat", "newt", "unicorn")` — same key, same potion.

### Key concepts used
- **Dictionary** — maps ingredient combos to potion results
- **Sorted tuple** — makes order irrelevant
- **Class** — `PotionGame` holds all game state and UI
- **tkinter** — draws the window, buttons, and labels
- **Event-driven programming** — buttons call functions when clicked (no while loop)

---

## 📁 File Structure

```
karel_potion_tkinter.py   ← the whole game, one file
README.md                 ← you're reading this
```

---

## 👩‍💻 About

Made by **Katarina Jocelyn Chandra**
BBA Strategic Management, Ritsumeikan Asia Pacific University (APU), Japan
Stanford Code in Place 2026 — Final Project

