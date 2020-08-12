from src.battle.Battle import Battle
from src.battle.Battlefield import Battlefield
from util.Position import Position

import src.repository.CharacterRepo as CharacterRepo
"""Sets up instances needed for a battle"""

def setup_battle():
    characters = get_characters()
    enemies = get_enemies()
    turn_order = determine_turn_order(characters, enemies)

    battlefield = Battlefield(height=5, width=5)
    place_characters_in_battlefield(battlefield, characters)
    place_enemies_in_battlefield(battlefield, enemies)

    battle = Battle(battlefield, turn_order)

    return battle

def determine_turn_order(characters, enemies):
    turn_order = characters + enemies
    turn_order.sort(key=lambda x: x.sp, reverse=True)

    return turn_order

def place_characters_in_battlefield(battlefield, characters):
    for i in range(len(characters)):
        battlefield.add_new_character(characters[i], Position(y=3, x=1+i))

def place_enemies_in_battlefield(battlefield, enemies):
    for i in range(len(enemies)):
        battlefield.add_new_character(enemies[i], Position(y=1, x=1+i))

def get_characters():
    characters = CharacterRepo.get_characters_from_file('part_defs/char_defs.json')
    return characters

def get_enemies():
    enemies = CharacterRepo.get_characters_from_file('part_defs/ene_defs.json')
    return enemies
