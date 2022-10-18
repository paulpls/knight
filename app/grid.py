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
            content = None
            # Create new squares, alternating the colors in a checkered pattern.
            grid = {}
            for x in range(xmax):
                for y in range(ymax):
                    grid[(x,y)] = Square(
                        color = Colors.square_color((x,y)),
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
            out.append(
                "".join(
                    [
                        self.grid[(x,y)].display(
                            showLabels = showLabels
                        ) for x in range(self.xmax)
                    ]
                )
            )
        return "\n".join(out)


    def put(self, coords, content="N", color=Colors.color("P")):
        """
            Put a piece on the board. Defaults to a knight with a knight label.

        """
        square = self.grid.get(coords, None)
        if square:
            square.content = content
            square.color = color


    def generate(self, squares=[(3,4)], put=False, content=None, color=None):
        """
            Generate a list of squares that are a knight's move from the square(s)
                provided. General formula is as follows:
                 
                >       N(a,b) = (x±a, y±b) ∪ (x±b, y±a)
                >         for a=1, b=2
                 
        """
        def _valid(square):
            """Check for validity against the grid dimensions."""
            x,y = square
            xmax = self.xmax
            ymax = self.ymax
            return all([
                0 <= x <= xmax,
                0 <= y <= ymax,
            ])

        def _replace(square, content):
            """True if square is appropriate to replace."""
            if square.content:
                return all([
                    square.content not in ["N","F"],
                    square.content > content,
                ])
            else:
                return True
    
        def _gen(square):
            """Generate new squares based on knight movements."""
            out = []
            x,y = square
            # Get a new list of available squares according to the set defined above
            for s in [
                (x+1, y+2), (x+1, y-2), # +1,+2  +1,-2
                (x-1, y+2), (x-1, y-2), # -1,+2  -1,-2
                (x+2, y+1), (x+2, y-1), # +2,+1  +2,-1
                (x-2, y+1), (x-2, y-1), # -2,+1  -2,-2
            ]:
                if _valid(s):
                    out.append(s)
            return out
    
        # Get list of next squares
        next = []
        # Begin with provided squares
        for square in squares:
            # Generate new squares
            for new in _gen(square):
                # Find new squares in grid
                gridSquare = self.get(new)
                if gridSquare is not None:
                    if put: 
                        if _replace(gridSquare, content):
                            self.put(new, content, color)
                            next.append(new)
        # Return list of squares
        return next



class Square:

    def __init__(self, color=Colors.color("R"), content=None):
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
            Labels are always shown for pieces.

        """
        if self.content in ["N", "F"]:
            showLabels = True
        color = self.color
        content = self.content if showLabels and self.content else " "
        reset = Colors.color("R")
        return f"{color}{content} {reset}"



