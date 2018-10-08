# Dutch

## Goal
Tools to help with learning Dutch

## To install
You will need Python 3.7: https://www.python.org/downloads/

Then, install `pipenv`: https://pipenv.readthedocs.io/en/latest/
```shell
#Windows
C:\path\to\python.exe -m pip install pipenv

#Linux / Mac
python -m pip install pipenv
```
Then install the tool's dependencies:
```shell
pipenv install
```

## Usage
```shell
[OPTIONS] [SESSIONS]...

This tool is used to help memorizing irregular verbs in Dutch.

Argument:

    SESSIONS:       A list of session numbers (1, 2, 3, 4).
                    Used to only load some sessions.
                    Default: 1 (only session 1 gets loaded)



Options:
  --help  Show this message and exit.
```

## To run
Just session 1:
```shell
pipenv run python verbs/perfectum_onregelmatig.py
```

With sessions 1 and 2:
```shell
pipenv run python verbs/perfectum_onregelmatig.py 1 2
```