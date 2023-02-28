import os

from sutts.utils.path import so_vits_svc_path


class CharacterModel:
    def __init__(self, model_path, config_path, speaker):
        self.model_path = model_path
        self.config_path = config_path
        self.speaker = speaker

    def __str__(self):
        return "model_path: " + self.model_path + "\n" + \
            "config_path: " + self.config_path + "\n" + \
            "speaker: " + self.speaker + "\n"


    mikisayaka = "mikisayaka"
    sakurakyouko = "sakurakyouko"


character_model_map = {
    CharacterModel.mikisayaka: CharacterModel(
        model_path=os.path.join(so_vits_svc_path, "_models/mikisayaka-G_50000-infer.pth"),
        config_path=os.path.join(so_vits_svc_path, "_models/mikisayaka-config.json"),
        speaker=CharacterModel.mikisayaka
    ),
    CharacterModel.sakurakyouko: CharacterModel(
        model_path=os.path.join(so_vits_svc_path, "_models/sakurakyouko-G_100000-infer.pth"),
        config_path=os.path.join(so_vits_svc_path, "_models/sakurakyouko-config.json"),
        speaker=CharacterModel.sakurakyouko
    )
}
