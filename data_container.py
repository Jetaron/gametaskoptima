import json
from character import Character

class DataContainer:
    def __init__(self):
        self.characters = []
        self.items = []
        self.abilities = []

    def restore_character_equipment(self):
        for character in self.characters:
            character.restore_equipped_tool(self.items)

def save_data(characters, items, abilities):
    data = {
        "characters": [vars(c) for c in characters],
        "items": items,
        "abilities": abilities
    }
    with open("GameSave.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    try:
        with open("GameSave.json", "r") as f:
            data = json.load(f)
            characters = [Character(**c) for c in data.get("characters", [])]
            items = data.get("items", [])
            abilities = data.get("abilities", [])
            return characters, items, abilities
    except FileNotFoundError:
        print("Файл не знайдений, створюємо нову гру.")
        return [], [], []
