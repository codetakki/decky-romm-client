from enum import Enum


class RomFileCategory(str, Enum):
    CHEAT = "cheat"
    DEMO = "demo"
    DLC = "dlc"
    GAME = "game"
    HACK = "hack"
    MANUAL = "manual"
    MOD = "mod"
    PATCH = "patch"
    PROTOTYPE = "prototype"
    TRANSLATION = "translation"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
