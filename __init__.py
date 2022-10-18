from random import randint
from .color import Colors


class KnightGrid:

    def __init__(self, dimensions=(8,8)):
        """
            A grid of squares. Defaults to an 8x8 grid.
    
        """
        def _generate(dimensions):
            """Helper method for generating the grid."""
            xmax, ymax = dimensions
            grid = {}
            # Create new squares, alternating the colors in a checkered pattern.
            for x in range(xmax):
                if x % 2 == 0:
                    # Even rows start with a light square for an even column,
                    # and a dark square for an odd column.
                    for y in range(ymax):
                        if y % 2 == 0:
                            grid[(x,y)] = Square(color=Colors.color("L"))
                        else:
                            grid[(x,y)] = Square(color=Colors.color("D"))
                else:
                    # Odd rows start with a dark square for an even column,
                    # and a light square for an odd column.
                    for y in range(ymax):
                        if y % 2 == 0:
                            grid[(x,y)] = Square(color=Colors.color('D'))
                        else:
                            grid[(x,y)] = Square(color=Colors.color('L'))
            return grid
        # Generate the grid
        self.grid = _generate(dimensions)
        # Set grid bounds
        self.xmax, self.ymax = dimensions


    def get(self, coords):
        """
            Get a square from the grid using the provided (x,y) coordinates.

        """
        return self.grid.get(coords, None)



class Square:

    def __init__(self, color=Colors.color("R"), highlight=None, content=None):
        """
            Instance of a square in the grid.

        """
        self.color = color
        self.highlight = highlight
        self.content = content


    def isEmpty(self):
        """
            Returns `True` if square has no content.

        """
        return self.content is None


    def display(self, visible=True):
        """
            Return a string representation of the square for output.

        """
        color = self.highlight if self.highlight else self.color
        content = self.content if visible and self.content else " "
        reset = Colors.color("R")
        return f"{color}{content} {reset}"



