import pytest
from command_interpreter import CommandInterpreter

def test_command_interpreter_initialization():
    interpreter = CommandInterpreter()
    assert interpreter.characters == []
    assert interpreter.items == []
    assert interpreter.abilities == []

def test_create_character():
    interpreter = CommandInterpreter()
    interpreter.create_entity("Hero 100 10")
    assert len(interpreter.characters) == 1
    assert interpreter.characters[0].name == "Hero"
    assert interpreter.characters[0].logger.get_hp() == 100
    assert interpreter.characters[0].logger.get_damage() == 10
