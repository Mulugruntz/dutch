import textwrap
from random import choice
from typing import Set, Tuple, FrozenSet

import click

from verbs.data import verbs
from verbs.structures import Auxilaries, Perfectum, ScoredVerb, shortcuts


# Monkey-patch to have spaces not striped in the doc/usage.
import inspect
import click.formatting
inspect.cleandoc = lambda s: s.split('\n')[0] + '\n' + textwrap.dedent('\n'.join(s.split('\n')[1:]))
click.formatting.wrap_text = lambda s, *args, **kwargs: s


def main(sessions: FrozenSet[int]):
    verbs_to_be_done: Set[ScoredVerb] = {
        ScoredVerb(verb) for session in sessions for verb in verbs[session - 1]
    }
    verbs_done = set()

    print(
        f"Loaded session{'s' if len(sessions) > 1 else ''} {', '.join(str(s) for s in sorted(sessions))}: "
        f"{len(verbs_to_be_done)} verbs."
    )

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


@click.command('perfectum')
@click.argument('sessions', nargs=-1, type=int)
def cli(sessions: Tuple[int]):
    """This tool is used to help memorizing irregular verbs in Dutch.

    Argument:

        SESSIONS:       A list of session numbers (1, 2, 3, 4).
                        Used to only load some sessions.
                        Default: 1 (only session 1 gets loaded)

    """
    if not sessions:
        sessions = frozenset([1])
    else:
        sessions = frozenset(s for s in sessions if 0 < s <= len(verbs))
    main(sessions)


if __name__ == "__main__":
    cli()
