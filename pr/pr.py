# -------------------------------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------------------------------

from pprint import pprint
from .tabulate import trow

# -------------------------------------------------------------------------------------
# COLORS
# -------------------------------------------------------------------------------------

# Define ANSI codes
BLACK = "\u001b[30m"
BLUE = "\u001b[34m"
CYAN = "\u001b[36m"
GREEN = "\u001b[32m"
MAGENTA = "\u001b[35m"
RED = "\u001b[31m"
WHITE = "\u001b[37m"
YELLOW = "\u001b[33m"
RESET = "\u001b[0m"

# Map ANSI codes
colors = {
    "ba": BLACK,
    "black": BLACK,
    "bu": BLUE,
    "blue": BLUE,
    "c": CYAN,
    "cyan": CYAN,
    "g": GREEN,
    "green": GREEN,
    "m": MAGENTA,
    "magenta": MAGENTA,
    "r": RED,
    "red": RED,
    "w": WHITE,
    "white": WHITE,
    "y": YELLOW,
    "yellow": YELLOW,
}
# See http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html


# -------------------------------------------------------------------------------------
# PR
# -------------------------------------------------------------------------------------


def pr(
    # Ordered arguments
    content: str = "",
    t: int = 0,  # tabs
    la: int = 0,  # lines after
    lb: int = 0,  # lines before
    # Unordered arguments
    c: str = None,  # color
    ip: bool = False,  # in place
    h: bool = False,  # heading
    hr: bool = False,  # horizontal rule
    hrc: str = "-",  # horizontal rule character
    hrl: int = 72,  # horizontal rule length
    dhrl: bool = False,  # dynamic horizontal rule length
    r: bool = False,  # row
    p: int = 20,  # padding
    a: str = "left",  # alignment
) -> None:
    """ Extends the existing python print function """

    # Construct lines before
    lines_before = "\n" * lb

    # Print lines before
    if lines_before:
        print(lines_before)

    # Construct lines after
    lines_after = "\n" * la

    # Initialize ANSI color
    color = None

    # Check if color argument exists
    if c is not None:

        # Lowercase color argument
        c = c.lower()

        # Get ANSI color
        color = colors.get(c)

    # Handle case of horizontal rule
    if hr is True:

        # Construct horizontal rule
        horizontal_rule = hrc * hrl

        # Check if ANSI color exists
        if color:

            # Add color to horizontal rule
            horizontal_rule = color + horizontal_rule + RESET

        # Print horizontal rule
        print(horizontal_rule)

        # Print lines after and return
        print(lines_after)
        return

    # Handle case of lists and dictionaries
    elif type(content) in [dict, list, tuple]:

        # Handle case of table row
        if type(content) in [list, tuple] and r is True:

            # Check if ANSI color exists
            if color:

                # Add color to each row item
                content = [f"{color}{item}{RESET}" for item in content]

            # Initialize table row dict
            trow_dict = {
                "row": content,
                "padding": p,
                "alignment": a,
            }

            # Handle case of table heading
            if h is True:

                # Add header boolean to table row dict
                trow_dict["header"] = True

                # Add horizontal rule character to table row dict
                trow_dict["horizontal_rule_character"] = hrc

            # Print table row and return
            trow(**trow_dict)

            # Print lines after and return
            if lines_after:
                print(lines_after)
            return

        # Pretty print the content
        pprint(content)

        # Print lines after and return
        if lines_after:
            print(lines_after)
        return

    # Check if ANSI color exists
    if color:

        # Add color to string
        content = color + content + RESET

    # Construct tabs
    tabs = "\t" * t

    # Append tabs to string
    content = tabs + content

    # Case of heading
    if h is True:

        # Determine if horizontal rule length should be dynamic
        if dhrl:

            # Set horizontal rule length to the length of the content + 1
            hrl = len(content) + 1

        # Construct horizontal rule
        horizontal_rule = hrc * hrl

        # Check if ANSI color exists
        if color:

            # Add color to horizontal rule
            horizontal_rule = color + horizontal_rule + RESET

        # Add tabs to horizontal rule
        horizontal_rule = tabs + horizontal_rule

        # Print first horizontal rule
        print(horizontal_rule)

        # Print string
        print(content)

        # Print second horizontal rule
        print(horizontal_rule)

    # Case of no heading
    else:

        # Handle case of in place printing
        if ip is True:

            # Print string
            print(f"\r\033[K{content}", end="", flush=True)

        else:

            # Print string
            print(f"{content}")

    # Print lines after
    if lines_after:
        print(lines_after)