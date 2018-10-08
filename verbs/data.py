from typing import Set

from verbs.structures import Verb, Perfectum, Auxilaries

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