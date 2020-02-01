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

|   var   |                          name                           |       type        | default |
| :-----: | :-----------------------------------------------------: | :---------------: | :-----: |
| content |                         Content                         | str / list / dict |   ""    |
|    t    |            [Tabs](#using-new-lines-and-tabs)            |        int        |    0    |
|   la    |        [Lines After](#using-new-lines-and-tabs)         |        int        |    0    |
|   lb    |        [Lines Before](#using-new-lines-and-tabs)        |        int        |    0    |
|    c    |                 [Color](#using-colors)                  |        str        |  None   |
|   ip    |             [In Place](#printing-in-place)              |       bool        |  False  |
|    h    |              [Heading](#printing-headings)              |       bool        |  False  |
|   hr    |      [Horizontal Rule](#printing-horizontal-rules)      |       bool        |  False  |
|   hrc   | [Horizontal Rule Character](#printing-horizontal-rules) |        str        |   "-"   |
|   hrl   |  [Horizontal Rule Length](#printing-horizontal-rules)   |        int        |   72    |
|  dhrl   |  [Dynamic Horizontal Rule Length](#printing-headings)   |       bool        |  False  |
|    r    |                [Row](#tabularizing-data)                |       bool        |  False  |
|    p    |              [Padding](#tabularizing-data)              |        int        |   20    |
|    a    |             [Alignment](#tabularizing-data)             |        str        | "left"  |
|   sb    |            [Status Box](#using-status-boxes)            |       bool        |  False  |
|   st    |           [Status Type](#using-status-boxes)            |        str        |   "i"   |

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
Hello word
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
print("-" * 15)
print("Hello world")
print("-" * 15)
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

### Tabularizing Data

```
headers = ["Name", "Age", "Location", "Gender"]
rows = [
    ("Joey", 32, "London, UK", "M"),
    ("Penny", 27, "Beijing, China", "F"),
    ("Caroline", 30, "Austin, USA", "F"),
    ("Diego", 24, "Lima, Peru", "M"),
    ("Donny", 29, "La Linea de la Concepcion, Spain", "M")
]
```

```
pr(headers, r=True, h=True)
for row in rows:
    pr(row, r=True)
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
pr(headers, r=True, h=True, hrc="=", p=padding, a="c")
for row in rows:
    pr(row, r=True, p=padding)
```

```
Name                      |            Age            |         Location          |          Gender
============================================================================================================
Joey                      | 32                        | London, UK                | M
Penny                     | 27                        | Beijing, China            | F
Caroline                  | 30                        | Austin, USA               | F
Diego                     | 24                        | Lima, Peru                | M
Donny                     | 29                        | La Linea de la Concepci   | M
```

Where:

- r = indicates whether the content should be treated as a table row `bool`

- h = indicates whether the content should be treated as a table header, i.e. a row with a horizontal rule underneath `bool`

- hrc = desired character used to construct the horizontal rule `str`

- p = desired padding (width) of each column `int`

- a = desired alignment of each table cell `str`

Accepted alignment options include:

- Left --> l, left

- Center --> c, center

- Right --> r, right

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

---
