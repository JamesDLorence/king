from src.models.Character import Character
import json


def get_characters_from_file(file_path):
    characters = []
    print(file_path)

    with open(file_path) as reader:
        char_list = json.load(reader)

        for char_dict in char_list:
            character = Character(**char_dict)
            characters.append(character)

    return characters
