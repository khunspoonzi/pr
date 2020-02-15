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
    tl=4,  # tab length
    b: bool = False,  # bullet
    bc: str = "\u2022",  # bullet character
    c: str = None,  # color
    cs: bool = False,  # color span
    ip: bool = False,  # in place
    h: bool = False,  # heading
    hr: bool = False,  # horizontal rule
    hrc: str = "-",  # horizontal rule character
    hrl: int = 72,  # horizontal rule length
    dhrl: bool = False,  # dynamic horizontal rule length
    r: bool = False,  # row
    rl: bool = False,  # row list
    p: int = 20,  # padding
    a: str = "left",  # alignment
    sb: bool = False,  # status box
    st: str = "info",  # status type
    dbg=True,  # debug
) -> None:
    """ Extends the existing python print function """

    # Return if debug is True
    if dbg is False:
        return

    # Check if horizontal rule length is default
    if hrl == 72:

        # Shorten horizontal rule length by tabs
        hrl = hrl - (t * 4)

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
        if type(content) in [list, tuple]:

            # Check if row or row list is True
            if r is True or rl is True:

                # Check if only a single row
                if r is True and rl is False:

                    # Reformat content into a single-element list
                    content = [content]

                # Iterate over rows
                for i, row in enumerate(content):

                    # Check if ANSI color exists
                    if color:

                        # Add color to each row item
                        row = [f"{color}{item}{RESET}" for item in row]

                    # Initialize table row dict
                    trow_dict = {
                        "row": row,
                        "padding": p,
                        "alignment": a,
                    }

                    # Handle case of table heading
                    if h is True:

                        # Handle case of row list
                        if rl is True:

                            # Only add horzontal rule for first row
                            if i == 0:

                                # Add header boolean to table row dict
                                trow_dict["header"] = True

                                # Add horizontal rule character to table row dict
                                trow_dict["horizontal_rule_character"] = hrc

                        # Otherwise handle case of single row heading
                        else:

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

            # Otherwise chec if color span is True
            elif cs is True:

                # Initialize string to print
                to_print = ""

                # Iterate over content
                for item in content:

                    # Get item type
                    item_type = type(item)

                    # Check if item is a string
                    if item_type == str:

                        # Append to string to print
                        to_print += item

                    # Otherwise check if item is a list or tuple
                    elif item_type in [list, tuple]:

                        # Ensure that the length of the item is 2
                        if len(item) != 2:

                            # Raise exception
                            raise Exception(
                                "Format of color span should be: ('my string', 'red')"
                            )

                        # Unpack string and color
                        string, color = item

                        # Lowercase color
                        color = color.lower()

                        # Get ANSI color
                        color = colors.get(color)

                        # Handle case of existint ANSI color
                        if color:

                            # Wrap string in color
                            string = f"{color}{string}{RESET}"

                        # Append to string to print
                        to_print += string

                    # Handle all other types
                    else:

                        # Raise exception
                        raise Exception(f"Unhandled type in color span: {type(item)}")

                # Print color span content
                print(to_print)

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
        content = f"{color}{content}{RESET}"

    # Check if bullet argument is True
    if b is True:

        # Add bullet character to content
        content = f"{bc} {content}"

    # Check if status box argument is True
    elif sb is True:

        # Initialize status box
        status_box = "[i]"

        # Handle case of success
        if st in ["s", "success"]:

            # Redefine status box
            status_box = "[" + GREEN + "\u2714" + RESET + "]"

        # Handle case of fail
        elif st in ["f", "fail"]:

            # Redefine status box
            status_box = "[" + RED + "\u2718" + RESET + "]"

        # Add status box to content
        content = f"{status_box} {content}"

    # Construct tabs
    tabs = " " * tl * t

    # Append tabs to string
    content = f"{tabs}{content}"

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
