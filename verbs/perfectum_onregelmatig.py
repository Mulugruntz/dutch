from random import choice
from typing import Set

from verbs.data import verbs
from verbs.structures import Auxilaries, Perfectum, ScoredVerb, shortcuts


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
