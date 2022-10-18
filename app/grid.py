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
            # Create new squares, alternating the colors in a checkered pattern
            # using square_color()
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


    def test(self, coords, silent=False, purpose=None):
        """
            Test coords for validity within bounds, raising an exception if not,
                unless silenced. Returns boolean result of test.

            An optional string `purpose` can be provided which is added to any
                error messages that arise.

        """
        result = False
        try:
            x,y = coords
            valid = (
                x >= 0,
                x <= self.xmax,
                y >= 0,
                y <= self.ymax,
            )
            assert all(valid)
            result = True
        # Scary-colored error message for out-of-bounds coordinates 
        except AssertionError as e:
            if not silent:
                color = Colors.color("L4")
                reset = Colors.color("R")
                purpose = "<none>" if purpose is None else f"<{purpose}>"
                err = f"ERR: {purpose} Coordinates ({x},{y}) are not within bounds ({self.xmax},{self.ymax})"
                msg = f"{color}{err}{reset}"
                print(msg)
        # Let other errors pass silently
        except Exception as e:
            pass
        # Return the result
        return result


    def get(self, coords):
        """
            Get a square from the grid using the provided (x,y) coordinates.

        """
        if self.test(coords, purpose="method Grid.get()"):
            # Return grid square at coords, or None
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
                if self.test(s, silent=True):
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



