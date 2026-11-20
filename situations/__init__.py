"""One module per situation, each defining SITUATION = {...}.

To add a situation: copy a similar file, rename it to <situation>.py (the
file name must equal its "situation" field), and list it in a round file
under rounds/.
"""
import importlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def names():
    """Every situation file, sorted."""
    return sorted(f[:-3] for f in os.listdir(HERE) if f.endswith(".py") and not f.startswith("_"))


def load(name):
    s = importlib.import_module(f"situations.{name}").SITUATION
    if s["situation"] != name:
        raise ValueError(f"situations/{name}.py defines situation {s['situation']!r}; the file name must match")
    return s
