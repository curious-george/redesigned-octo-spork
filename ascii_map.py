import blessed
import random
import sys
import time

# Define the elements and their properties
ELEMENTS = {
    "wetness": {
        "blue": "💧",
    },
    "hilliness": {
        "brown": "⛰️",
    },
    "forest": {
        "green": "🌲",
    },
    "light": {
        "yellow": "☀️",
        "night": "🌙",
    },
    "player": {
        "A": "👨",
        "B": "👩",
    },
    "disposition": {
        "sleep": "😴",
        "running": "🏃",
        "sitting": "🧘",
    },
}

# Define the colors for each element
COLORS = {
    "wetness": "blue",
    "hilliness": "brown",
    "forest": "green",
    "light": "yellow",
    "player": "white",
    "disposition": "white",
}

def generate_random_map(size):
    """Generates a random map of a given size."""
    game_map = []
    for _ in range(size):
        row = []
        for _ in range(size):
            cell = {}
            # Randomly add elements to the cell
            if random.choice([True, False]):
                cell["wetness"] = "blue"
            if random.choice([True, False]):
                cell["hilliness"] = "brown"
            if random.choice([True, False]):
                cell["forest"] = "green"
            cell["light"] = random.choice(list(ELEMENTS["light"].keys()))
            if random.choice([True, False]):
                player = random.choice(list(ELEMENTS["player"].keys()))
                units = random.randint(1, 99)
                cell["player"] = (player, units)
            if random.choice([True, False]):
                cell["disposition"] = random.choice(list(ELEMENTS["disposition"].keys()))
            row.append(cell)
        game_map.append(row)
    return game_map

def render_map(term, game_map):
    """Renders the map to the terminal."""
    with term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear)
        # Draw top border
        print(term.move_xy(0, 0) + "┌" + "─" * (len(game_map[0]) * 4) + "┐")
        for i, row in enumerate(game_map):
            # Draw side borders
            print(term.move_xy(0, i + 1) + "│")
            for j, cell in enumerate(row):
                x, y = j * 4 + 1, i + 1
                # Draw cell contents
                elements_in_cell = []
                if "wetness" in cell:
                    elements_in_cell.append(term.color(COLORS["wetness"]) + ELEMENTS["wetness"]["blue"])
                if "hilliness" in cell:
                    elements_in_cell.append(term.color(COLORS["hilliness"]) + ELEMENTS["hilliness"]["brown"])
                if "forest" in cell:
                    elements_in_cell.append(term.color(COLORS["forest"]) + ELEMENTS["forest"]["green"])
                if "light" in cell:
                    elements_in_cell.append(term.color(COLORS["light"]) + ELEMENTS["light"][cell["light"]])
                if "player" in cell:
                    player, units = cell["player"]
                    elements_in_cell.append(term.color(COLORS["player"]) + f"{player}{units}{ELEMENTS['player'][player]}")
                if "disposition" in cell:
                    elements_in_cell.append(term.color(COLORS["disposition"]) + ELEMENTS["disposition"][cell["disposition"]])

                print(term.move_xy(x, y) + "".join(elements_in_cell))
            print(term.move_xy(len(game_map[0]) * 4 + 1, i + 1) + "│")
        # Draw bottom border
        print(term.move_xy(0, len(game_map) + 1) + "└" + "─" * (len(game_map[0]) * 4) + "┘")
        # Draw instruction text
        print(term.move_xy(0, len(game_map) + 2) + "Press 'k' for the key/map, 'q' to quit.")

def show_key(term):
    """Displays the key/map."""
    with term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear)
        print("Key/Map:")
        for element, subtypes in ELEMENTS.items():
            print(f"\n{element.capitalize()}:")
            for subtype, symbol in subtypes.items():
                color = COLORS.get(element, "white")
                print(f"  {term.color(color)}{symbol}{term.normal} - {subtype.capitalize()}")
        print("\nPress any key to return to the map.")
        term.inkey()

def main():
    """Main function."""
    term = blessed.Terminal()
    game_map = generate_random_map(10)
    try:
        while True:
            render_map(term, game_map)
            key = term.inkey()
            if key == "k":
                show_key(term)
            elif key == "q":
                break
    finally:
        # Restore terminal settings
        print(term.normal)

if __name__ == "__main__":
    main()
