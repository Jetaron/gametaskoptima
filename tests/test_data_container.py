import pytest
from data_container import save_data, load_data
from character import Character

def test_save_load_data(tmp_path):
    characters = [Character("Hero", 100, 10)]
    items = []
    abilities = []
    
    save_data(characters, items, abilities)
    
    loaded_characters, loaded_items, loaded_abilities = load_data()
    
    assert len(loaded_characters) == 1
    assert loaded_characters[0].name == "Hero"
    assert loaded_characters[0].logger.get_hp() == 100
    assert loaded_characters[0].logger.get_damage() == 10
