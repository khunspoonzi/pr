# -------------------------------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------------------------------

from typing import Any, List


# -------------------------------------------------------------------------------------
# GET ALIGNMENT CHARACTER
# -------------------------------------------------------------------------------------


def get_alignment_character(alignment: str) -> str:
    """ Returns an alignment character for string formatting """

    # Determine left alignment character
    if alignment in ["left", "l"]:
        return ""

    # Determine right alignment character
    elif alignment in ["right", "r"]:
        return ">"

    # Determine center alignment character
    elif alignment in ["center", "c"]:
        return "^"

    return ""


# -------------------------------------------------------------------------------------
# TROW
# -------------------------------------------------------------------------------------


def trow(
    row: List[Any],
    padding: int = 10,
    alignment: str = "left",
    header: bool = False,
    horizontal_rule_character: str = "-",
) -> None:
    """ Prints a nicely formatted table row """

    # Get alignment character
    alignment_character = get_alignment_character(alignment)

    # Stringify padding
    padding_str = str(padding)

    # Compute truncation string
    truncation_str = f".{padding - 2}"

    # Define template
    template = [
        "{:" + alignment_character + padding_str + truncation_str + "}" for r in row
    ]
    template = " | ".join(template)

    # Compute row length
    row_length = len(row)

    # Get horizontal rule
    horizontal_rule = horizontal_rule_character * (
        padding * row_length + (row_length * 2)
    )

    # Stringify row
    row = [str(r) for r in row]

    # Print heading
    print(template.format(*row))

    # Print horizontal rule
    if header:
        print(horizontal_rule)
