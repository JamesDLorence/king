from src.models.Character import Character
import json


def get_characters_from_file(self, file_path):
    with open(file_path, 'r') as reader:
        char_list = json.loads(reader)

        for char_dict in char_list:
            character = Character(**char_dict)