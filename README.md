# pr

A high-level shorthand print formatter for Python 3 or above

---

## Overview

The objective of pr is to streamline the debugging process by allowing developers to implement complex print formatting with minimal effort.

---

## Installation

Run `pip3 install pr`

---

## Arguments

|   var   |                          name                           |           type            | default |
| :-----: | :-----------------------------------------------------: | :-----------------------: | :-----: |
| content |              [Content](#printing-a-string)              | str / list / dict / tuple |   ""    |
|    t    |            [Tabs](#using-new-lines-and-tabs)            |            int            |    0    |
|   la    |        [Lines After](#using-new-lines-and-tabs)         |            int            |    0    |
|   lb    |        [Lines Before](#using-new-lines-and-tabs)        |            int            |    0    |
|    b    |                [Bullet](#using-bullets)                 |           bool            |  False  |
|   bc    |           [Bullet Character](#using-bullets)            |            str            |   "•"   |
|    c    |                 [Color](#using-colors)                  |            str            |  None   |
|   cs    |            [Color Span](#using-color-spans)             |           bool            |  False  |
|   ip    |             [In Place](#printing-in-place)              |           bool            |  False  |
|    h    |              [Heading](#printing-headings)              |           bool            |  False  |
|   hr    |      [Horizontal Rule](#printing-horizontal-rules)      |           bool            |  False  |
|   hrc   | [Horizontal Rule Character](#printing-horizontal-rules) |            str            |   "-"   |
|   hrl   |  [Horizontal Rule Length](#printing-horizontal-rules)   |            int            |   72    |
|  dhrl   |  [Dynamic Horizontal Rule Length](#printing-headings)   |           bool            |  False  |
|    r    |                 [Row](#tabulating-data)                 |           bool            |  False  |
|   rl    |              [Row List](#tabulating-data)               |           bool            |  False  |
|    p    |               [Padding](#tabulating-data)               |            int            |   20    |
|    a    |              [Alignment](#tabulating-data)              |            str            | "left"  |
|   sb    |            [Status Box](#using-status-boxes)            |           bool            |  False  |
|   st    |           [Status Type](#using-status-boxes)            |            str            |   "i"   |

---

## Examples

### Importing the Module

```
from pr import pr
```

### Printing a String

```
pr("Hello world")
```

```
Hello world
```

Equivalent to:

```
print("Hello world")
```

### Printing an Empty String

```
pr()
```

```

```

Equivalent to:

```
print("\n")
```

or

```
print("")
```

### Using New Lines and Tabs

```
pr("Hello world", t=1, la=1, lb=1)
```

or

```
pr("Hello world", 1, 1, 1)
```

```

  Hello world

```

Where:

- t = number of tabs before the printed string `int`

- la = number of lines after the printed string `int`

- lb = number of lines before the printed string `int`

Equivalent to:

```
print(\n\tHello world\n)
```

### Using Bullets

```
shopping_list = [
    "eggs",
    "bacon",
    "cucumbers",
    "bottled water",
    "fresh straberries",
    "fine cheese",
    "pasta",
]
```

```
for item in shopping_list:
    pr(item, b=True)
```

```
• eggs
• bacon
• cucumbers
• bottled water
• fresh straberries
• fine cheese
• pasta
```

```
for item in shopping_list:
  pr(item, b=True, bc="@")
```

```
@ eggs
@ bacon
@ cucumbers
@ bottled water
@ fresh straberries
@ fine cheese
@ pasta
```

Where:

- c = indicates whether to add a bullet point before the content `bool`

- bc = desired bullet character `str`

Equivalent to:

```
for item in shopping_list:
  print(f"{•} {item}")
```

```
for item in shopping_list:
  print(f"{@} {item}")
```

### Using Colors

```
pr("Hello world", c="r")
```

```
Hello word  <-- appears red in terminal
```

Where:

- c = desired color of text `str`

Equivalent to:

```
print(\u001b[31mHello world\u001b[0m)
```

Accepted colors include:

- Black --> ba, black

- Blue --> bu, blue

- Cyan --> c, cyan

- Green --> g, green

- Magenta --> m, magenta

- Red --> r, red

- White --> w, white

- Yellow --> y, yellow

### Using Color Spans

```
color_span = [
    "Roses are ",
    ("red", "r"),
    " and violets are ",
    ("blue", "bu")
]

pr(color_span, cs=True)
```

```
Roses are [red] and violets are [blue]  <--  words in square brackets appear in their respective colors
```

Where:

- c = indicates whether to treat the iterable as spans of colored text `bool`

Equivalent to:

```
print("Roses are \u001b[31mred\u001b[0m and violets are \u001b[34mblue\u001b[0m")
```

### Printing In Place

Printing in place avoids the default Python behavior of printing content on a new line for each call to the print function. Instead, printing in place displays content on the same line, flushing the contents of the previous print statement each time. Such functionality is extremely useful within large loops.

```
for i in range(101):
  pr(f"Percent complete: {i}%", ip=True)
```

```
Percent complete: {1-100}%
```

Where:

- ip = indicates whether content should be printed in place `bool`

Equivalent to:

```
for i in range(101):
    print(f"\r\033[KPercent complete: {i}%", end="", flush=True)
```

### Printing Headings

```
pr("Hello world", h=True)
```

```
------------------------------------------------------------------------
Hello world
------------------------------------------------------------------------
```

```
pr("Hello world", h=True, hrl=20)
```

```
--------------------
Hello world
--------------------
```

```
pr("Hello world", h=True, dhrl=True)
pr("Hello world, goodbye Mars", h=True, dhrl=True)
```

```
------------
Hello world
------------

--------------------------
Hello world, goodbye Mars
--------------------------
```

Where:

- h = indicates whether content should be printed as a heading `bool`

- hrl = desired length of horizontal rule above and below the heading string `int`

- dhrl = indicates whether the length of the horizontal rule above and below the heading string should be dynamic, i.e. match the length of the content `bool`

Equivalent to:

```
print("-" * 72)
print("Hello world")
print("-" * 72)
```

```
print("-" * 20)
print("Hello world")
print("-" * 20)
```

```
content = "Hello world"
length = len(content) + 1

print("-" * length)
print(content)
print("-" * length)
```

### Printing Horizontal Rules

```
pr(hr=True)
```

```
------------------------------------------------------------------------
```

```
pr(hr=True, hrl=20, hrc="=")
```

```
====================
```

Where:

- hr = indicates whether to print a horizontal rule `bool`

- hrl = desired length of horizontal rule `int`

- hrc = desired character used to construct the horizontal rule `str`

Equivalent to:

```
print("-" * 72)
```

```
print("=" * 20)
```

### Tabulating Data

```
header = ["Name", "Age", "Location", "Gender"]
rows = [
    ("Joey", 32, "London, UK", "M"),
    ("Penny", 27, "Beijing, China", "F"),
    ("Caroline", 30, "Austin, USA", "F"),
    ("Diego", 24, "Lima, Peru", "M"),
    ("Donny", 29, "La Linea de la Concepcion, Spain", "M")
]
```

```
pr(header, r=True, h=True)
for row in rows:
    pr(row, r=True)
```

or

```
pr(header, r=True, h=True)
pr(rows, rl=True)
```

or

```
header_and_rows = [header] + rows

pr(header_and_rows, rl=True, h=True)
```

```
Name                 | Age                  | Location             | Gender
----------------------------------------------------------------------------------------
Joey                 | 32                   | London, UK           | M
Penny                | 27                   | Beijing, China       | F
Caroline             | 30                   | Austin, USA          | F
Diego                | 24                   | Lima, Peru           | M
Donny                | 29                   | La Linea de la Con   | M
```

```
padding = 25

pr(header, r=True, h=True, hrc="=", p=padding, a="c")
for row in rows:
    pr(row, r=True, p=padding)
```

or

```
padding = 25

pr(header, r=True, h=True, hrc="=", p=padding, a="c")
pr(rows, rl=True, p=padding)
```

```
           Name           |            Age            |         Location          |          Gender
============================================================================================================
Joey                      | 32                        | London, UK                | M
Penny                     | 27                        | Beijing, China            | F
Caroline                  | 30                        | Austin, USA               | F
Diego                     | 24                        | Lima, Peru                | M
Donny                     | 29                        | La Linea de la Concepci   | M
```

Where:

- r = indicates whether the content should be treated as a table row `bool`

- rl = indicates whether the content should be treated as a list of rows `bool`

- h = indicates whether the content should be treated as a table header, i.e. a row with a horizontal rule underneath `bool`

- hrc = desired character used to construct the horizontal rule `str`

- p = desired padding (width) of each column `int`

- a = desired alignment of each table cell `str`

Accepted alignment options include:

- Left --> l, left

- Center --> c, center

- Right --> r, right

Remarks:

- Avoid using colors with tabulated data for the time being as Python's string formatter does not play well with with ANSI color codes

### Using Status Boxes

```
pr("Initializing launch sequence...", sb=True, la=1)
pr("Thrusters activated", t=1, sb=True, st="s")
pr("Satcom operational", t=1, sb=True, st="s")
pr("Communications online", t=1, sb=True, st="s")
pr("Major Tom present", t=1, sb=True, st="f")
pr("Aborting launch sequence...", lb=1, sb=True)
```

```
[i] Initializing launch sequence...


	[✔] Thrusters activated
	[✔] Satcom operational
	[✔] Communications online
	[✘] Major Tom present


[i] Aborting launch sequence...
```

Where:

- sb = indicates whether to include a status box before the printed content `bool`

- st = desired status type to display in the status box `str`

Accepted status types include:

- Info --> i, info

- Success --> s, success

- Fail --> f, fail

### Pretty Printing Data

Pretty printing is enabled by default when a structure such as a dictionary, list, or tuple is passed into pr. This will print the data over multiple lines if necessary rather than attempt to print everything on a single line as the default print statement will do.

```
d = {
    "personal_info": {"name": "Jose", "age": "23", "location": "Christchurch, New Zealand", "gender": "M"},
    "hobbies": ["running", "swimming", "reading", "photography", "birdwatching", "surfing"]
}
```

```
pr(d)
```

```
{'hobbies': ['running',
             'swimming',
             'reading',
             'photography',
             'birdwatching',
             'surfing'],
 'personal_info': {'age': '23',
                   'gender': 'M',
                   'location': 'Christchurch, New Zealand',
                   'name': 'Jose'}}
```

Equivalent to:

```
from pprint import pprint

pprint(d)
```

---
