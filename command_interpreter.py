import json
from character import Character

class CommandInterpreter:
    def __init__(self):
        self.characters = []
        self.items = []
        self.abilities = []
        self.next_character_id = 1
        self.next_item_id = 1
        self.next_ability_id = 1

    def start(self):
        print("Оберіть режим роботи:\n1 - Text 2 - Game")
        choice = input()
        if choice == "1":
            self.enter_text_mode()
        else:
            self.enter_game_mode()

    def enter_text_mode(self):
        print("Text mode activated.")
        # Implement text mode commands here

    def enter_game_mode(self):
        print("Game mode activated.")
        self.load_data()
        print("Ваші доступні команд: create, add, act, ls, delete, test, save, loadhtml.")
        self.enter_command_loop()

    def enter_command_loop(self):
        while True:
            command = input("> ")
            if command == "exit":
                break
            self.execute_command(command)

    def execute_command(self, command):
        parts = command.split(' ', 1)
        cmd = parts[0]
        parameters = parts[1] if len(parts) > 1 else ""

        if cmd == "create":
            self.create_entity(parameters)
        elif cmd == "add":
            self.add_to_character(parameters)

    def create_entity(self, parameters):
        print("Що бажаєте створити?\n1 - Персонаж\n2 - Предмет\n3 - Здібність")
        choice = int(input())
        if choice == 1:
            name = input("Введіть ім'я вашому персу: ")
            hp = int(input("Введіть HP: "))
            damage = int(input("Введіть силу удару: "))
            character = Character(name, hp, damage)
            self.characters.append(character)
            print(f"Ваш створений перс {name} с ID {self.next_character_id}")
            self.next_character_id += 1
            self.save_data()

    def save_data(self):
        data = {
            "characters": [vars(c) for c in self.characters],
            "items": self.items,
            "abilities": self.abilities
        }
        with open("GameSave.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("GameSave.json", "r") as f:
                data = json.load(f)
                self.characters = [Character(**c) for c in data.get("characters", [])]
                self.items = data.get("items", [])
                self.abilities = data.get("abilities", [])
        except FileNotFoundError:
            print("Файл не знайдений, створюємо нову гру.")
