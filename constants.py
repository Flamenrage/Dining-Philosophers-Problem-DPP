from enum import Enum, auto

class PhilosopherState(Enum):
    EATING = auto()
    HUNGRY = auto()
    THINKING = auto()

class ForkState(Enum):
    DIRTY = auto()
    CLEAN = auto()
