#!/usr/bin/env python3
"""
Generate a HTML file with what the user is working on. Open the file in a browser.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path
from time import localtime, strftime
from webbrowser import open as open_html


def parse_args() -> Namespace:
    """Parse inputted arguments"""
    parser = ArgumentParser()
    parser.add_argument("input_string", nargs="+")
    return parser.parse_args()


def generate_html(input_string: str) -> str:
    """
    Open `template.html`. Fill in template variables with computed strings.'
    """
    with open("template.html", "r", encoding="utf-8") as file:
        template = file.read()
    return template.replace("{{ input_string }}", input_string)


def main() -> None:
    """
    Entry point for What Am I Working On
    """
    input_string = " ".join(parse_args().input_string)
    filename = strftime("%Y-%m-%d_%H%M%S.html", localtime())
    filepath = Path(f"html/{filename}")
    with filepath.open("w", encoding="utf-8") as file:
        file.write(generate_html(input_string))
    open_html(f"file://{filepath.resolve()}")


if __name__ == "__main__":
    main()
