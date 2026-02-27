from enum import Enum


class JobStatus(str, Enum):
    CANCELED = "canceled"
    DEFERRED = "deferred"
    FAILED = "failed"
    FINISHED = "finished"
    QUEUED = "queued"
    SCHEDULED = "scheduled"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
