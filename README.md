# pr

A high-level shorthand print formatter for Python 3 or above

---

## Overview

The objective of pr is to streamline the debugging process by allowing developers...

---

## Installation

Run `pip3 install pr` in your terminal.

---

## Arguments

|   var   |                   name                    |       type        | default |
| :-----: | :---------------------------------------: | :---------------: | :-----: |
| content |                  Content                  | str / list / dict |   ""    |
|   lb    | [Lines Before](#using-new-lines-and-tabs) |        int        |    0    |
|    t    |     [Tabs](#using-new-lines-and-tabs)     |        int        |    0    |
|   la    | [Lines After](#using-new-lines-and-tabs)  |        int        |    0    |
|    c    |          [Color](#using-colors)           |        str        |   ""    |
|   ip    |      [In Place](#printing-in-place)       |       bool        |  False  |
|    h    |                  Heading                  |       bool        |  False  |
|   hr    |              Horizontal Rule              |       bool        |  False  |
|   hrc   |         Horizontal Rule Character         |        str        |   "-"   |
|   hrl   |          Horizontal Rule Length           |        int        |   72    |
|  dhrl   |      Dynamic Horizontal Rule Length       |       bool        |  False  |
|    r    |                    Row                    |       bool        |  False  |
|    p    |                  Padding                  |        int        |   20    |
|    a    |                 Alignment                 |        str        | "left"  |

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
pr("Hello world", lb=1, t=1, la=1)
```

or

```
pr("Hello world", 1, 1, 1)
```

```

  Hello world

```

Where:

- lb = number of lines before the printed string `int`

- t = number of tabs before the printed string `int`

- la = number of lines after the printed string `int`

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

- ip = boolean indicating whether content should be printed in place `bool`

Equivalent to:

```
for i in range(101):
    print(f"\r\033[KPercent complete: {i}%", end="", flush=True)
```

---
