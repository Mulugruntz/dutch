from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Auxilaries(str, Enum):
    HEBBEN = "hebben"
    ZIJN = "zijn"
    BOTH = "hebben/zijn"


@dataclass
class Perfectum:
    auxiliary: Auxilaries
    verb: str

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return f"{self.auxiliary} {self.verb}"

    def __format__(self, format_spec):
        return self.__str__().__format__(format_spec)


@dataclass
class Verb:
    infinitive: str
    imperfectum1: str = ""
    imperfectum2: str = ""
    perfectum: Perfectum = None
    english_translation: str = ""

    def __hash__(self):
        return hash(self.infinitive)

    def __str__(self):
        return (
            f"{self.infinitive:30} | {self.perfectum:30} ({self.english_translation})"
        )

    def __format__(self, format_spec):
        return self.__str__().__format__(format_spec)


@dataclass
class ScoredVerb:
    verb: Verb
    tries: int = 0
    inputs: List[Perfectum] = field(default_factory=list)

    def __hash__(self):
        return hash(self.verb)

    def __str__(self):
        plural = 's' if self.tries > 2 else ''
        return f"{self.tries - 1:>3} error{plural}: {self.verb:95} | {' - '.join(str(p) for p in self.inputs)}"


shortcuts = {
    "h": Auxilaries.HEBBEN.value,
    "z": Auxilaries.ZIJN.value,
    "hz": Auxilaries.BOTH.value,
    "b": Auxilaries.BOTH.value,
}