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

|   var   |                   name                    | type | default |
| :-----: | :---------------------------------------: | :--: | :-----: |
| content |                  Content                  | str  |   ""    |
|   lb    | [Lines Before](#using-new-lines-and-tabs) | int  |    0    |
|    t    |     [Tabs](#using-new-lines-and-tabs)     | int  |    0    |
|   la    | [Lines After](#using-new-lines-and-tabs)  | int  |    0    |
|    c    |          [Color](#using-colors)           | str  |   ""    |
|   ip    |                 In Place                  | bool |  False  |
|    h    |                  Heading                  | bool |  False  |
|   hr    |              Horizontal Rule              | bool |  False  |
|   hrc   |         Horizontal Rule Character         | str  |   "-"   |
|   hrl   |          Horizontal Rule Length           | int  |   72    |
|  dhrl   |      Dynamic Horizontal Rule Length       | bool |  False  |
|    r    |                    Row                    | bool |  False  |
|    p    |                  Padding                  | int  |   20    |
|    a    |                 Alignment                 | str  | "left"  |

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

> <span style="color:red">Hello world</span>

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

```
pr("Hello world", lb=1, t=1, la=1)

---
```
