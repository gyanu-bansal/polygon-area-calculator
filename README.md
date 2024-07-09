# Polygon Area Calculator

This Python project calculates the area of rectangles and squares using object-oriented programming principles.

## How to Use

### Prerequisites

- Python 3.x installed on your system.


## Classes and Methods

### Rectangle Class

- `__init__(self, width, height)`: Initializes a rectangle with given width and height.
- `get_area(self)`: Returns the area of the rectangle.
- `get_perimeter(self)`: Returns the perimeter of the rectangle.
- `get_diagonal(self)`: Returns the diagonal length of the rectangle.
- `get_picture(self)`: Returns a string representation of the rectangle as a picture of stars (`*`). Returns "Too big for picture." if dimensions exceed 50x50.
- `get_amount_inside(self, other)`: Calculates how many times another rectangle (`other`) can fit inside the current rectangle.
- `set_width(self, width)`: Sets the width of the rectangle.
- `set_height(self, height)`: Sets the height of the rectangle.
- `__str__(self)`: Returns a string representation of the rectangle.

### Square Class (Inherits from Rectangle)

- `__init__(self, side)`: Initializes a square with equal side lengths.
- `set_side(self, side)`: Sets the side length of the square.
- `set_width(self, width)`: Sets the width (and height) of the square.
- `set_height(self, height)`: Sets the height (and width) of the square.
- `__str__(self)`: Returns a string representation of the square.

## How to Use

1. **Save the script** as `polygon_area_calculator.py` or any preferred name.
2. **Ensure Python 3.x is installed** on your system.
3. **Open a terminal or command prompt**.
4. **Navigate to the directory** where the script is saved.
5. **Run the script** by executing the command:
   
   ```bash
   python polygon_area_calculator.py
