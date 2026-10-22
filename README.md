# term-colors

A small truecolor swatch book for the terminal. Choose ember or moss, bring your own colors, or export a palette for another tool.

## Install

Requires Python 3.11 or newer. From this directory:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

## Use

```sh
term-colors list
term-colors preview ember
term-colors convert '#ff8800'
term-colors convert 255 136 0
term-colors export moss
```

Custom palettes are nonempty JSON arrays such as `["#112233", "#aabbcc"]`. Load with `term-colors preview --file colors.json`. Previews require a terminal supporting 24-bit ANSI colors. Exports contain no escape sequences.

## Development

```sh
python -m unittest discover -s tests -v
```

Licensed under MIT.
