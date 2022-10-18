from random import randint
from .color import Colors


class Grid:

    def __init__(self, dimensions=(8,8)):
        """
            A grid of squares. Defaults to an 8x8 grid.
    
        """
        def _generate(dimensions):
            """Helper method for generating the grid."""
            xmax, ymax = dimensions
            content = "  "
            # Create new squares, alternating the colors in a checkered pattern.
            grid = {}
            for x in range(xmax):
                if x % 2 == 0:
                    # Even rows start with a light square for an even column,
                    # and a dark square for an odd column.
                    for y in range(ymax):
                        if y % 2 == 0:
                            color = Colors.color("L")
                        else:
                            color = Colors.color("D")
                        grid[(x,y)] = Square(
                            color = color,
                            content = content,
                        )
                else:
                    # Odd rows start with a dark square for an even column,
                    # and a light square for an odd column.
                    for y in range(ymax):
                        if y % 2 == 0:
                            color = Colors.color("D")
                        else:
                            color = Colors.color("L")
                        grid[(x,y)] = Square(
                            color = color,
                            content = content,
                        )
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


    def display(self, showLabels=True):
        """
            Return a string representation of the grid for display purposes.

        """
        out = []
        # Iterate through the grid by row and collect the outputs
        for y in range(self.ymax):
            out.append("".join([
                self.grid[(x,y)].display(showLabels=showLabels) for x in range(self.xmax)
            ]))
        return "\n".join(out)


    def put(self, coords, content="N ", color=Colors.color("N")):
        """
            Put a piece on the board. Defaults to a knight with a knight label.

        """
        square = self.grid.get(coords, None)
        if square:
            square.content = content
            square.color = color



class Square:

    def __init__(self, color=Colors.color("R"), highlight=None, content=None):
        """
            Instance of a square in the grid.

        """
        self.color = color
        self.content = content


    def isEmpty(self):
        """
            Returns `True` if square has no content.

        """
        return self.content is None


    def display(self, showLabels=True):
        """
            Return a string representation of the square for display purposes.

        """
        color = self.color
        content = self.content if showLabels and self.content else "  "
        reset = Colors.color("R")
        return f"{color}{content}{reset}"



