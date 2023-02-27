import os

from sutts.inference.character_model import CharacterModel, character_model_map
from sutts.inference.so_vits_svc import SoVitsSvcTTS
from sutts.utils.path import so_vits_svc_path


# @dataclass


def newSoVitsSvcTTS(character):
    character_model = character_model_map[character]
    # model_path = character_model.model_path
    # config_path = character_model.config_path
    # print("model_path", model_path)
    # print("config_path", config_path)
    print(character_model)
    return SoVitsSvcTTS(character_model)
