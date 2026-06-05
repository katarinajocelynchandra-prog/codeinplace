"""
Karel's Potion Shop
===================
A Code in Place Final Project by Katarina Chandra

Karel the robot wants to become a prince.
Pick three ingredients and unlock the potion to make that happen!

HOW TO RUN:
    python karel_potion_tkinter.py

HOW THE CODE WORKS (for beginners):
    1. POTIONS dictionary maps ingredient combos → potion results
    2. We sort the 3 picks so order doesn't matter
    3. tkinter draws the window and buttons
    4. When you click BREW, we look up the combo in the dictionary
"""

import tkinter as tk  # tkinter is built into Python - no install needed!

# ==============================================================
# STEP 1: THE INGREDIENTS
# ==============================================================

INGREDIENTS = [
    "Eye of Newt",
    "Tears of Unicorn",
    "Leprechaun's Hat",
    "Wolfsbane",
    "Mermaid's Core",
]

# Short nicknames used as dictionary keys (easier to type)
NICKNAMES = {
    "Eye of Newt":       "newt",
    "Tears of Unicorn":  "unicorn",
    "Leprechaun's Hat":  "hat",
    "Wolfsbane":         "wolf",
    "Mermaid's Core":    "mermaid",
}

# ==============================================================
# STEP 2: THE POTION DICTIONARY
#
# ==============================================================

POTIONS = {
    # === THE ONE TRUE PRINCE POTION ===
    ("hat", "newt", "unicorn"):          ("✨ Royal Elixir",        "Karel transforms into a dashing PRINCE!\nThe prophecy is fulfilled!",                          "prince"),

    # === REGULAR COMBOS (3 different ingredients) ===
    ("mermaid", "newt", "unicorn"):      ("🫧 Bubble Brew",         "Karel floats 3 feet off the ground.\nWon't come down.",                                        "chaos"),
    ("hat", "newt", "wolf"):             ("💨 Smoke Bomb",          "Purple smoke fills the lab.\nKarel vanishes. Briefly.",                                        "ghost"),
    ("mermaid", "newt", "wolf"):         ("😤 Rage Potion",         "Karel screams for exactly 4.7 seconds.\nVery specific.",                                       "chaos"),
    ("hat", "mermaid", "newt"):          ("🛝 Slippery Tonic",      "Karel slides into every wall. Repeatedly.",                                                    "chaos"),
    ("hat", "unicorn", "wolf"):          ("✨ Glitter Explosion",   "EVERYTHING is glitter now.\nEverything.",                                                      "chaos"),
    ("hat", "mermaid", "unicorn"):       ("😴 Sleep Draught",       "Karel falls asleep and dreams\nof sorting algorithms.",                                        "ghost"),
    ("mermaid", "unicorn", "wolf"):      ("🌑 Dark Potion",         "Lights out. Ominous humming.\nLights back on. Karel is fine.",                                 "ghost"),
    ("hat", "mermaid", "wolf"):          ("🌀 Mystery Brew",        "'Did you feel that?' Karel asks.\nNobody answers.",                                            "chaos"),
    ("newt", "unicorn", "wolf"):         ("🫠 Confusion Tonic",     "Karel walks in perfect circles.\nDeeply satisfied.",                                           "chaos"),

    # === TRIPLE INGREDIENT COMBOS (the unhinged ones) ===
    ("newt", "newt", "newt"):            ("👁 Pure Newt Essence",   "Karel now has 6 eyes.\nUses all of them simultaneously.",                                      "chaos"),
    ("unicorn", "unicorn", "unicorn"):   ("🌟 Ascension Brew",      "Karel floats and speaks only in rhyme.\nInsufferable.",                                        "chaos"),
    ("hat", "hat", "hat"):               ("🍀 Triple Luck Potion",  "Karel finds a coin, wins a staring contest,\nand parallel parks on the first try.",            "chaos"),
    ("wolf", "wolf", "wolf"):            ("🐺 Full Moon Draught",   "Karel howls ONCE.\nThen looks embarrassed. We don't talk about it.",                           "frog"),
    ("mermaid", "mermaid", "mermaid"):   ("🧜 Deep Ocean Brew",     "Karel grows gills. Still in the lab.\nDelighted anyway.",                                      "frog"),

    # === DOUBLE INGREDIENT COMBOS ===
    ("newt", "newt", "unicorn"):         ("🔍 Newt-Corn Brew",      "Karel can detect lies.\nUses it immediately on everyone.",                                     "chaos"),
    ("newt", "newt", "wolf"):            ("🏃 Predator Tonic",      "Karel moves 30% faster\nbut only when unobserved.",                                            "chaos"),
    ("mermaid", "newt", "newt"):         ("🐠 Tide Eye Brew",       "Karel can breathe underwater.\nStill in the lab. Still happy.",                                "frog"),
    ("hat", "newt", "newt"):             ("🪄 Trick Tonic",         "Karel pulls objects from hats.\nAll slightly wrong.",                                          "chaos"),
    ("newt", "unicorn", "unicorn"):      ("🔮 Horn Sight",          "Karel sees 3 minutes into the future.\nRefuses to share what they see.",                       "ghost"),
    ("unicorn", "unicorn", "wolf"):      ("🌙 Night Sight",         "Karel's eyes glow in the dark.\nConsidered polite somewhere.",                                 "ghost"),
    ("hat", "unicorn", "unicorn"):       ("🧚 Fairy Fortune",       "Karel grants small wishes.\nAll slightly misinterpreted.",                                     "chaos"),
    ("mermaid", "unicorn", "unicorn"):   ("👻 Mist Potion",         "Karel goes translucent for 1 hour.\nUses the time wisely.",                                    "ghost"),
    ("hat", "hat", "newt"):              ("🎰 Double Luck",         "Karel finds 2 coins.\nConsiders it a sign.",                                                   "chaos"),
    ("hat", "hat", "unicorn"):           ("🤏 Leprechaun Brew",     "Karel shrinks to 4 inches tall.\nCannot stop laughing about it.",                             "frog"),
    ("hat", "hat", "wolf"):              ("📯 Wild Trick",          "Karel makes a foghorn sound.\nOnce. Perfectly timed.",                                         "chaos"),
    ("hat", "hat", "mermaid"):           ("🗺 River Luck",          "Karel solves any maze instantly.\nRefuses to explain how.",                                    "chaos"),
    ("newt", "wolf", "wolf"):            ("🌱 Venom Draught",       "Karel identifies plants by smell.\nThe lab smells 'anxious'.",                                 "frog"),
    ("unicorn", "wolf", "wolf"):         ("🌕 Moonbane",            "Karel speaks only in whispers.\nEveryone leans in.",                                           "ghost"),
    ("hat", "wolf", "wolf"):             ("🧭 Hunt Tonic",          "Karel finds lost objects within 200m.\nCurrently searching for your motivation.",              "chaos"),
    ("mermaid", "wolf", "wolf"):         ("🐋 Tide Fang",           "Karel grows briefly, returns to normal.\nDeeply satisfied.",                                   "frog"),
    ("mermaid", "mermaid", "newt"):      ("📖 Saltwater Tonic",     "Karel narrates everything in third person.\n'Karel picks up the flask. Karel looks confused.'","chaos"),
    ("mermaid", "mermaid", "unicorn"):   ("🫧 Pearl Brew",          "Karel produces one perfect pearl.\nRefuses to explain.",                                       "chaos"),
    ("hat", "mermaid", "mermaid"):       ("🪙 Tidal Fortune",       "Karel wins every coin flip for 24 hours.\nUses this power for good.",                          "chaos"),
    ("mermaid", "mermaid", "wolf"):      ("⭐ Deep Tide",           "Karel could navigate home from anywhere.\nAnywhere.",                                          "ghost"),
}

# ==============================================================
# STEP 3: KAREL DRAWINGS
# I can't figure out how to add the real Karel so I do it like this
# ==============================================================

def get_karel_art(state):
    """Return Karel's ASCII art based on their current state."""

    if state == "robot":
        return (
            "  ┌─────┐  \n"
            "  │ ◉ ◉ │  \n"
            "  │  ▬  │  \n"
            "  └──┬──┘  \n"
            "  ┌──┴──┐  \n"
            "  │KAREL│  \n"
            "  └─────┘  \n"
            "  ◉     ◉  "
        )
    elif state == "prince":
        return (
            "    👑    \n"
            "  ┌─────┐  \n"
            "  │ ★ ★ │  \n"
            "  │  ▲  │  \n"  # smiling
            "  └──┬──┘  \n"
            " ╔═══╧═══╗ \n"
            " ║ PRINCE║ \n"
            " ╚═══════╝ \n"
            "   ◉   ◉   "
        )
    elif state == "ghost":
        return (
            "  ░░░░░░░  \n"
            " ░ ◉   ◉ ░ \n"
            " ░       ░ \n"
            " ░  ___  ░ \n"
            " ░░░░░░░░░ \n"
            "  ░ ░ ░ ░  \n"
            "\n"
            "  spooky... "
        )
    elif state == "frog":
        return (
            " ╭──●──●──╮ \n"
            " │  (ᴗ)   │ \n"
            " │  ___   │ \n"
            " ╰────────╯ \n"
            "  ╱      ╲  \n"
            "\n"
            "  ribbit?   "
        )
    else:  # chaos
        return (
            "  ┌─────┐  \n"
            "  │ ◉ ◉ │  \n"
            "  │  ?  │  \n"
            "  └──┬──┘  \n"
            "  ┌──┴──┐  \n"
            "  │ ??? │  \n"
            "  └─────┘  \n"
            " ? ?   ? ?  "
        )

# ==============================================================
# STEP 4: THE GAME WINDOW
# ==============================================================

class PotionGame:
    def __init__(self):
        # --- Create the main window ---
        self.window = tk.Tk()
        self.window.title("🧪 Karel's Potion Shop")
        self.window.configure(bg="#1a0e2e")
        self.window.resizable(False, False)

        # --- Game state variables ---
        self.picks = []          # list of ingredient nicknames picked so far

        # --- Build all the UI pieces ---
        self.build_title()
        self.build_ingredient_buttons()
        self.build_middle_section()
        self.build_brew_reset_buttons()
        self.build_result_section()

    # ----------------------------------------------------------
    # BUILD FUNCTIONS — each one creates one part of the screen
    # ----------------------------------------------------------

    def build_title(self):
        """Top title text"""
        title = tk.Label(
            self.window,
            text="⚗️  KAREL'S POTION SHOP  ⚗️",
            font=("Courier", 20, "bold"),
            bg="#1a0e2e", fg="#c9a84c"
        )
        title.pack(pady=(15, 2))

        subtitle = tk.Label(
            self.window,
            text="~ transform the robot, if you dare ~",
            font=("Courier", 10, "italic"),
            bg="#1a0e2e", fg="#7a6650"
        )
        subtitle.pack(pady=(0, 15))

    def build_ingredient_buttons(self):
        """5 ingredient buttons across the top"""
        frame = tk.Frame(self.window, bg="#1a0e2e")
        frame.pack(pady=5)

        label = tk.Label(
            frame,
            text="CHOOSE 3 INGREDIENTS  (repeats allowed)",
            font=("Courier", 10),
            bg="#1a0e2e", fg="#7a6650"
        )
        label.pack(pady=(0, 8))

        
        emojis = ["👁️", "🦄", "🎩", "🌿", "🔮"]
        button_frame = tk.Frame(frame, bg="#1a0e2e")
        button_frame.pack()

        for i, ingredient in enumerate(INGREDIENTS):
            btn = tk.Button(
                button_frame,
                text=f"{emojis[i]}\n{ingredient}",
                font=("Courier", 9),
                bg="#2a1a3e", fg="#e8d5b7",
                activebackground="#c9a84c", activeforeground="#1a0e2e",
                width=13, height=3,
                relief="flat", bd=0,
                cursor="hand2",
                # When clicked, call add_ingredient with this ingredient's name
                command=lambda name=ingredient: self.add_ingredient(name)
            )
            btn.grid(row=0, column=i, padx=5)

    def build_middle_section(self):
        """Middle area: cauldron on left, Karel on right"""
        middle = tk.Frame(self.window, bg="#1a0e2e")
        middle.pack(pady=10, padx=20)

        # --- LEFT: Cauldron area ---
        cauldron_frame = tk.Frame(middle, bg="#1a0e2e")
        cauldron_frame.grid(row=0, column=0, padx=20)

        tk.Label(
            cauldron_frame,
            text="CAULDRON",
            font=("Courier", 9), bg="#1a0e2e", fg="#7a6650"
        ).pack()

        # The big cauldron emoji
        tk.Label(
            cauldron_frame,
            text="🫕",
            font=("Courier", 60),
            bg="#1a0e2e"
        ).pack()

        # Shows what's been picked so far
        self.picks_label = tk.Label(
            cauldron_frame,
            text="( empty )",
            font=("Courier", 9),
            bg="#1a0e2e", fg="#c9a84c",
            width=28, height=3,
            wraplength=220
        )
        self.picks_label.pack(pady=5)

        # Pick counter: "0 / 3"
        self.counter_label = tk.Label(
            cauldron_frame,
            text="0 / 3 ingredients",
            font=("Courier", 10, "bold"),
            bg="#1a0e2e", fg="#7a6650"
        )
        self.counter_label.pack()

        # --- RIGHT: Karel area ---
        karel_frame = tk.Frame(middle, bg="#1a0e2e")
        karel_frame.grid(row=0, column=1, padx=20)

        tk.Label(
            karel_frame,
            text="KAREL",
            font=("Courier", 9), bg="#1a0e2e", fg="#7a6650"
        ).pack()

        # Karel's ASCII art — updates when you brew
        self.karel_label = tk.Label(
            karel_frame,
            text=get_karel_art("robot"),
            font=("Courier", 12),
            bg="#1a0e2e", fg="#c8d8e8",
            justify="center",
            width=14, height=10
        )
        self.karel_label.pack()

    def build_brew_reset_buttons(self):
        """BREW and RESET buttons"""
        btn_frame = tk.Frame(self.window, bg="#1a0e2e")
        btn_frame.pack(pady=10)

        self.brew_btn = tk.Button(
            btn_frame,
            text="🔥  BREW POTION  🔥",
            font=("Courier", 13, "bold"),
            bg="#3a1f08", fg="#c9a84c",
            activebackground="#c9a84c", activeforeground="#1a0e2e",
            relief="flat", padx=20, pady=8,
            cursor="hand2",
            state="disabled",  # starts disabled until 3 picks
            command=self.brew_potion
        )
        self.brew_btn.pack(side="left", padx=10)

        reset_btn = tk.Button(
            btn_frame,
            text="↺  RESET",
            font=("Courier", 10),
            bg="#1a0e2e", fg="#7a6650",
            activebackground="#2a1a3e", activeforeground="#c9a84c",
            relief="flat", padx=10, pady=8,
            cursor="hand2",
            command=self.reset_game
        )
        reset_btn.pack(side="left", padx=10)

    def build_result_section(self):
        """Bottom area showing potion name and effect"""
        result_frame = tk.Frame(self.window, bg="#2a1a3e", pady=15, padx=20)
        result_frame.pack(fill="x", padx=20, pady=(5, 20))

        self.potion_name_label = tk.Label(
            result_frame,
            text="Add 3 ingredients and press BREW",
            font=("Courier", 13, "bold"),
            bg="#2a1a3e", fg="#c9a84c",
            wraplength=500
        )
        self.potion_name_label.pack(pady=(5, 3))

        self.effect_label = tk.Label(
            result_frame,
            text="",
            font=("Courier", 10, "italic"),
            bg="#2a1a3e", fg="#e8d5b7",
            wraplength=500, justify="center"
        )
        self.effect_label.pack(pady=(0, 5))

    # ----------------------------------------------------------
    # GAME LOGIC FUNCTIONS
    # ----------------------------------------------------------

    def add_ingredient(self, ingredient_name):
        """Called when player clicks an ingredient button."""

        # Only allow adding if we have fewer than 3 picks
        if len(self.picks) >= 3:
            return

        # Add the nickname (e.g. "newt") to our picks list
        nickname = NICKNAMES[ingredient_name]
        self.picks.append(nickname)

        # Update the display
        self.update_picks_display()

        # Enable BREW button once we have 3 picks
        if len(self.picks) == 3:
            self.brew_btn.config(state="normal", bg="#c9a84c", fg="#1a0e2e")
            self.potion_name_label.config(text="✨ Ready to brew! Press BREW POTION ✨")

    def brew_potion(self):
        """Called when player clicks BREW. Looks up the combo in POTIONS dict."""

        # SORT the picks so order doesn't matter
        # e.g. ["unicorn", "newt", "hat"] → ("hat", "newt", "unicorn")
        combo_key = tuple(sorted(self.picks))

        # Look up in the dictionary
        if combo_key in POTIONS:
            potion_name, effect, karel_state = POTIONS[combo_key]
        else:
            # Fallback for any combo not defined (shouldn't happen with 35 combos)
            potion_name = "🌀 Mystery Brew"
            effect = "Something shifts in reality.\nKarel blinks. Nobody speaks."
            karel_state = "chaos"

        # Update Karel's appearance
        karel_art = get_karel_art(karel_state)
        self.karel_label.config(text=karel_art)

        # Update Karel's color based on state
        colors = {
            "prince": "#FFD700",
            "ghost":  "#aaccff",
            "frog":   "#2d8a2d",
            "chaos":  "#ff9900",
            "robot":  "#c8d8e8",
        }
        self.karel_label.config(fg=colors.get(karel_state, "#c8d8e8"))

        # Show the potion result
        self.potion_name_label.config(text=potion_name)
        self.effect_label.config(text=effect)

        # Special gold flash for the PRINCE potion
        if karel_state == "prince":
            self.window.configure(bg="#3a2a00")
            self.window.after(300, lambda: self.window.configure(bg="#1a0e2e"))

    def update_picks_display(self):
        """Update the cauldron label to show current picks."""
        if not self.picks:
            self.picks_label.config(text="( empty )")
        else:
            # Show ingredient names with arrows between them
            display = " → ".join(self.picks)
            self.picks_label.config(text=display)

        self.counter_label.config(text=f"{len(self.picks)} / 3 ingredients")

    def reset_game(self):
        """Clear everything and start over."""
        self.picks = []
        self.update_picks_display()
        self.karel_label.config(text=get_karel_art("robot"), fg="#c8d8e8")
        self.brew_btn.config(state="disabled", bg="#3a1f08", fg="#c9a84c")
        self.potion_name_label.config(text="Add 3 ingredients and press BREW")
        self.effect_label.config(text="")

    def run(self):
        """Start the game loop."""
        self.window.mainloop()


# ==============================================================
# STEP 5: RUN THE GAME
# This is the entry point — 
# ==============================================================

if __name__ == "__main__":
    game = PotionGame()
    game.run()
