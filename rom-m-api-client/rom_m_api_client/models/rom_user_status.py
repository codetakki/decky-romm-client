from enum import Enum


class RomUserStatus(str, Enum):
    COMPLETED_100 = "completed_100"
    FINISHED = "finished"
    INCOMPLETE = "incomplete"
    NEVER_PLAYING = "never_playing"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
