class Logger:
    def __init__(self, hp, damage):
        self._hp = hp
        self._damage = damage

    def get_hp(self):
        return self._hp

    def change_hp(self, amount):
        self._hp += amount

    def get_damage(self):
        return self._damage

    def change_damage(self, amount):
        self._damage += amount


class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.logger = Logger(hp, damage)

    def character_info_output(self):
        print(f"{self.name}, здоров'я: {self.logger.get_hp()}, урон: {self.logger.get_damage()}.")

    def take_damage(self, amount):
        self.logger.change_hp(-amount)
        print(f"{self.name} отримав {amount} болю, залишилось {self.logger.get_hp()} HP!")

    def heal(self, amount):
        self.logger.change_hp(amount)
        print(f"{self.name} відновив {amount} здоров'я, тепер в нього {self.logger.get_hp()} HP.")

    def damage_boost(self, amount):
        self.logger.change_damage(amount)


class Abilities:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name
        self.power = power

    def use(self, attacker, target):
        print(f"{attacker.name} використовує {self.name} на {target.name}, наносячи {self.power} урона.")
        target.take_damage(self.power)


class CursedTool:
    def __init__(self, id, name, damage_boost):
        self.id = id
        self.name = name
        self.damage_boost = damage_boost

    def apply_to_game_character(self, character):
        character.damage_boost(self.damage_boost)
        print(f"{character.name} екіпірував {self.name}, збільшивши свій урон на {self.damage_boost}.")

    @staticmethod
    def reversed_spear_of_haven():
        return CursedTool(1, "Обратное Копье Небес", 250)
