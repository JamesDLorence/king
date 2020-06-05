from src.battle.Battle import Battle
from src.battle.Battlefield import Battlefield

"""Sets up instances needed for a battle"""

def setup_battle(self):
    characters = self.get_characters()
    enemies = self.get_enemies()
    turn_order = self.determine_turn_order(characters, enemies)

    battlefield = Battlefield()
    self.place_characters_in_battlefield(battlefield, characters)
    self.place_enemies_in_battlefield(battlefield, enemies)

    battle = Battle(battlefield, turn_order)

    return battle

def determine_turn_order(self, characters, enemies):
    pass

def place_characters_in_battle_field(self, battlefield):
    pass

def place_enemies_in_battlefield(self, battlefield):
    pass

def get_characters(self):


def get_enemies(self):
    pass