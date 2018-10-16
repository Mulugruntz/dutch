from typing import Set, List

from verbs.structures import Verb, Perfectum, Auxilaries

verbs: List[Set[Verb]] = [
    {  # Session 1
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
    },
    {  # Session 2
        Verb(
            "hangen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gehangen"),
            english_translation="to hang",
        ),
        Verb(
            "hebben",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gehad"),
            english_translation="to have",
        ),
        Verb(
            "helpen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "geholpen"),
            english_translation="to help",
        ),
        Verb(
            "houden (van)",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gehouden"),
            english_translation="to hold (to love)",
        ),
        Verb(
            "innemen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "ingenomen"),
            english_translation="to take (medicine)",
        ),
        Verb(
            "kiezen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gekozen"),
            english_translation="to choose",
        ),
        Verb(
            "kijken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gekeken"),
            english_translation="to look",
        ),
        Verb(
            "komen",
            perfectum=Perfectum(Auxilaries.ZIJN, "gekomen"),
            english_translation="to come",
        ),
        Verb(
            "kopen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gekocht"),
            english_translation="to buy",
        ),
        Verb(
            "krijgen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gekregen"),
            english_translation="to receive",
        ),
        Verb(
            "kunnen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gekund"),
            english_translation="to can",
        ),
        Verb(
            "laten",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gelaten"),
            english_translation="to leave",
        ),
        Verb(
            "lezen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gelezen"),
            english_translation="to read",
        ),
        Verb(
            "liggen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gelegen"),
            english_translation="to lie (lay)",
        ),
        Verb(
            "lopen",
            perfectum=Perfectum(Auxilaries.BOTH, "gelopen"),
            english_translation="to walk",
        ),
        Verb(
            "meenemen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "meegenomen"),
            english_translation="to take along/with",
        ),
        Verb(
            "moeten",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gemoeten"),
            english_translation="to must",
        ),
        Verb(
            "mogen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gemogen"),
            english_translation="to may",
        ),
        Verb(
            "nakijken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "nagekeken"),
            english_translation="to check / to look at",
        ),
        Verb(
            "nemen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "genomen"),
            english_translation="to take",
        ),
        Verb(
            "onderzoeken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "onderzocht"),
            english_translation="to examine / to investigate",
        ),
        Verb(
            "ontbijten",
            perfectum=Perfectum(Auxilaries.HEBBEN, "ontbeten"),
            english_translation="to have breakfast",
        ),
        Verb(
            "opstaan",
            perfectum=Perfectum(Auxilaries.ZIJN, "opgestaan"),
            english_translation="to get up / to stand up",
        ),
    },
    {
        Verb(
            "oversteken",
            perfectum=Perfectum(Auxilaries.ZIJN, "overgestoken"),
            english_translation="to cross over",
        ),
        Verb(
            "rijden",
            perfectum=Perfectum(Auxilaries.BOTH, "gereden"),
            english_translation="to drive",
        ),
        Verb(
            "roepen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "geroepen"),
            english_translation="to call",
        ),
        Verb(
            "scheiden",
            perfectum=Perfectum(Auxilaries.ZIJN, "gescheiden"),
            english_translation="to divorce",
        ),
        Verb(
            "schijnen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "geschenen"),
            english_translation="to shine",
        ),
        Verb(
            "schrijven",
            perfectum=Perfectum(Auxilaries.HEBBEN, "geschreven"),
            english_translation="to write",
        ),
        Verb(
            "slapen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "geslapen"),
            english_translation="to sleep",
        ),
        Verb(
            "sluiten",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gesloten"),
            english_translation="to close",
        ),
        Verb(
            "snijden",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gesneden"),
            english_translation="to cut",
        ),
        Verb(
            "spreken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gesproken"),
            english_translation="to speak",
        ),
        Verb(
            "springen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gesprongen"),
            english_translation="to jump",
        ),
        Verb(
            "staan",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gestaan"),
            english_translation="to stand",
        ),
        Verb(
            "steken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gestoken"),
            english_translation="to stab",
        ),
        Verb(
            "sterven",
            perfectum=Perfectum(Auxilaries.ZIJN, "gestorven"),
            english_translation="to die",
        ),
        Verb(
            "strijken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gestreken"),
            english_translation="to iron",
        ),
        Verb(
            "treffen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "getroffen"),
            english_translation="to meet",
        ),
        Verb(
            "trekken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "getrokken"),
            english_translation="to pull",
        ),
        Verb(
            "uitdoen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "uitgedaan"),
            english_translation="to turn off",
        ),
        Verb(
            "uitgaan",
            perfectum=Perfectum(Auxilaries.ZIJN, "uitgegaan"),
            english_translation="to go out",
        ),
        Verb(
            "uittrekken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "uitgetrokken"),
            english_translation="to draw / to pull out / to extract",
        ),
        Verb(
            "vallen",
            perfectum=Perfectum(Auxilaries.ZIJN, "gevallen"),
            english_translation="to fall",
        ),
        Verb(
            "varen",
            perfectum=Perfectum(Auxilaries.BOTH, "gevaren"),
            english_translation="to sail",
        ),
        Verb(
            "verbieden",
            perfectum=Perfectum(Auxilaries.HEBBEN, "verboden"),
            english_translation="to forbid",
        ),
        Verb(
            "vergeten",
            perfectum=Perfectum(Auxilaries.BOTH, "vergeten"),
            english_translation="to forget",
        ),
        Verb(
            "verkopen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "verkocht"),
            english_translation="to sell",
        ),
    },
    {
        Verb(
            "verliezen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "verloren"),
            english_translation="to lose",
        ),
        Verb(
            "verstaan",
            perfectum=Perfectum(Auxilaries.HEBBEN, "verstaan"),
            english_translation="to understand",
        ),
        Verb(
            "vertrekken",
            perfectum=Perfectum(Auxilaries.ZIJN, "vertrokken"),
            english_translation="to leave",
        ),
        Verb(
            "vervangen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "vervangen"),
            english_translation="to replace",
        ),
        Verb(
            "vinden",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gevongen"),
            english_translation="to find",
        ),
        Verb(
            "vliegen",
            perfectum=Perfectum(Auxilaries.BOTH, "gevlogen"),
            english_translation="to travel by plane",
        ),
        Verb(
            "voorkomen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "voorkomen"),
            english_translation="to prevent",
        ),
        Verb(
            "vragen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gevraagd"),
            english_translation="to ask",
        ),
        Verb(
            "vriezen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gevroren"),
            english_translation="to freeze",
        ),
        Verb(
            "wassen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gewassen"),
            english_translation="to wash",
        ),
        Verb(
            "wegen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gewogen"),
            english_translation="to weigh",
        ),
        Verb(
            "weten",
            perfectum=Perfectum(Auxilaries.HEBBEN, "geweten"),
            english_translation="to know",
        ),
        Verb(
            "wijzen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gewezen"),
            english_translation="to point / to show",
        ),
        Verb(
            "willen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gewild"),
            english_translation="to want",
        ),
        Verb(
            "winnen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gewonnen"),
            english_translation="to win",
        ),
        Verb(
            "worden",
            perfectum=Perfectum(Auxilaries.ZIJN, "geworden"),
            english_translation="to become",
        ),
        Verb(
            "zeggen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gezegd"),
            english_translation="to say",
        ),
        Verb(
            "zien",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gezien"),
            english_translation="to see",
        ),
        Verb(
            "zijn",
            perfectum=Perfectum(Auxilaries.ZIJN, "geweest"),
            english_translation="to be",
        ),
        Verb(
            "zingen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gezongen"),
            english_translation="to sing",
        ),
        Verb(
            "zitten",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gezeten"),
            english_translation="to sit",
        ),
        Verb(
            "zoeken",
            perfectum=Perfectum(Auxilaries.HEBBEN, "gezocht"),
            english_translation="to search",
        ),
        Verb(
            "zullen",
            perfectum=Perfectum(Auxilaries.HEBBEN, "-"),
            english_translation="to shall",
        ),
        Verb(
            "zwemmen",
            perfectum=Perfectum(Auxilaries.BOTH, "gezwommen"),
            english_translation="to swim",
        ),
    }
]