# Nicer REPL
from contextlib import suppress

with suppress(ImportError):
    from rich import pretty
    pretty.install()
