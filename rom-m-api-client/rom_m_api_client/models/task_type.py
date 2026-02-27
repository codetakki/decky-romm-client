from enum import Enum


class TaskType(str, Enum):
    CLEANUP = "cleanup"
    CONVERSION = "conversion"
    GENERIC = "generic"
    SCAN = "scan"
    UPDATE = "update"
    WATCHER = "watcher"

    def __str__(self) -> str:
        return str(self.value)
