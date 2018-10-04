from dataclasses import dataclass, field
from enum import Enum
from random import choice
from typing import Set, List


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


shortcuts = {
    "h": Auxilaries.HEBBEN.value,
    "z": Auxilaries.ZIJN.value,
    "hz": Auxilaries.BOTH.value,
    "b": Auxilaries.BOTH.value,
}


verbs: Set[Verb] = {
    Verb(
        infinitive="aandoen",
        imperfectum1="deed aan",
        imperfectum2="deden aan",
        perfectum=Perfectum(Auxilaries.HEBBEN, "aangedaan"),
        english_translation="to put on / to turn on",
    ),
    Verb(
        "aankomen",
        perfectum=Perfectum(Auxilaries.ZIJN, "aangekomen"),
        english_translation="to arrive",
    ),
    Verb(
        "afwassen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "afgewassen"),
        english_translation="to do the dishes",
    ),
    Verb(
        "bakken",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gebakken"),
        english_translation="to bake",
    ),
    Verb(
        "beginnen",
        perfectum=Perfectum(Auxilaries.ZIJN, "begonnen"),
        english_translation="to begin / to start",
    ),
    Verb(
        "begrijpen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "begrepen"),
        english_translation="to understand",
    ),
    Verb(
        "behangen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "behangen"),
        english_translation="to hang",
    ),
    Verb(
        "bewegen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "bewogen"),
        english_translation="to move",
    ),
    Verb(
        "bezoeken",
        perfectum=Perfectum(Auxilaries.HEBBEN, "bezocht"),
        english_translation="to visit",
    ),
    Verb(
        "bijten",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gebeten"),
        english_translation="to bite",
    ),
    Verb(
        "blazen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "geblazen"),
        english_translation="to blow",
    ),
    Verb(
        "blijven",
        perfectum=Perfectum(Auxilaries.ZIJN, "gebleven"),
        english_translation="to stay",
    ),
    Verb(
        "breken",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gebroken"),
        english_translation="to break",
    ),
    Verb(
        "brengen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gebracht"),
        english_translation="to bring",
    ),
    Verb(
        "denken",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gedacht"),
        english_translation="to think",
    ),
    Verb(
        "doen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gedaan"),
        english_translation="to do",
    ),
    Verb(
        "dragen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gedragen"),
        english_translation="to wear",
    ),
    Verb(
        "drinken",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gedronken"),
        english_translation="to drink",
    ),
    Verb(
        "eten",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gegeten"),
        english_translation="to eat",
    ),
    Verb(
        "gaan",
        perfectum=Perfectum(Auxilaries.ZIJN, "gegaan"),
        english_translation="to go",
    ),
    Verb(
        "genezen",
        perfectum=Perfectum(Auxilaries.HEBBEN, "genezen"),
        english_translation="to cure",
    ),
    Verb(
        "geven",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gegeven"),
        english_translation="to give",
    ),
    Verb(
        "gieten",
        perfectum=Perfectum(Auxilaries.HEBBEN, "gegoten"),
        english_translation="to pour",
    ),
}


@dataclass
class ScoredVerb:
    verb: Verb
    tries: int = 0
    inputs: List[Perfectum] = field(default_factory=list)

    def __hash__(self):
        return hash(self.verb)

    def __str__(self):
        plural = 's' if self.tries > 2 else ''
        return f"{self.tries - 1:>3} error{plural}: {self.verb:90} | {' - '.join(str(p) for p in self.inputs)}"


def main():
    verbs_to_be_done: Set[ScoredVerb] = {ScoredVerb(verb) for verb in verbs}
    verbs_done = set()

    while verbs_to_be_done:
        verb: ScoredVerb = choice(tuple(verbs_to_be_done))
        verb.tries += 1
        try:
            aux, v = input(f"{verb.verb.infinitive.capitalize()}: ").lower().split()
        except KeyboardInterrupt:
            for v in verbs_to_be_done:
                if v.tries > 0:
                    v.tries += 1
                    verbs_done.add(v)
            break
        except Exception as err:
            print(err)
            raise
        if aux in shortcuts:
            aux = shortcuts[aux]
        perf = Perfectum(Auxilaries(aux), v)
        if perf == verb.verb.perfectum:
            print(f"Correct! (english: {verb.verb.english_translation})")
            verbs_to_be_done.remove(verb)
            verbs_done.add(verb)
        else:
            verb.inputs.append(perf)
            print(
                f"Wrong. The answer is {verb.verb.perfectum.auxiliary} {verb.verb.perfectum.verb} "
                f"(english: {verb.verb.english_translation})."
            )
    total_tries = sum(verb.tries for verb in verbs_done)
    ordered_scores = sorted(verbs_done, key=lambda v: v.tries, reverse=True)
    print(
        f"To deal with {len(verbs_done)} verbs, "
        f"you needed {total_tries} tries "
        f"(errors: {total_tries - len(verbs_done)})."
    )
    print("The worst:")
    print("\n".join(str(v) for v in ordered_scores))


if __name__ == "__main__":
    main()
