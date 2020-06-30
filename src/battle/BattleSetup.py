from src.battle.Battle import Battle
from src.battle.Battlefield import Battlefield

import src.repository.CharacterRepo as CharacterRepo
"""Sets up instances needed for a battle"""

def setup_battle():
    characters = get_characters()
    enemies = get_enemies()
    turn_order = determine_turn_order(characters, enemies)

    battlefield = Battlefield()
    place_characters_in_battlefield(battlefield, characters)
    place_enemies_in_battlefield(battlefield, enemies)

    battle = Battle(battlefield, turn_order)

    return battle

def determine_turn_order(characters, enemies):
    turn_order = characters + enemies
    turn_order.sort(key=lambda x: x.sp, reverse=True)

    return turn_order

def place_characters_in_battlefield(battlefield, characters):
    pass

def place_enemies_in_battlefield(battlefield, enemies):
    pass

def get_characters():
    characters = CharacterRepo.get_characters_from_file('part_defs/char_defs.json')
    return characters

def get_enemies():
    enemies = CharacterRepo.get_characters_from_file('part_defs/ene_defs.json')
    return enemies
