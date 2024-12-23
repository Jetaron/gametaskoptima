import pytest
from character import Character

def test_character_initialization():
    character = Character("Hero", 100, 10)
    assert character.name == "Hero"
    assert character.logger.get_hp() == 100
    assert character.logger.get_damage() == 10

def test_character_take_damage():
    character = Character("Hero", 100, 10)
    character.take_damage(20)
    assert character.logger.get_hp() == 80

def test_character_heal():
    character = Character("Hero", 100, 10)
    character.take_damage(20)
    character.heal(10)
    assert character.logger.get_hp() == 90

def test_character_damage_boost():
    character = Character("Hero", 100, 10)
    character.damage_boost(5)
    assert character.logger.get_damage() == 15
