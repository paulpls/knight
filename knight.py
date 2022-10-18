from app.grid import Grid
from app.color import Colors


def main(knights=[(3,3)], friendlies=[], dimensions=(8,8), showLabels=True, reverse=False):
    """
        Show a map with knights placed arbitrarily on the board.
            
      knights: List of (x,y) coords for placing knights
   friendlies: List of (x,y) coords for placing owned pieces
   dimensions: Board dimensions
   showLabels: Show content (highlight is always shown)
      reverse: Use 'reverse' (enemy) highlighting

    """
    def _gen(grid, square):
        """Place the knight on `square` and color the map according to its movement."""
        # Setup highlighting scheme
        X = "L" if showLabels else "H"
        if reverse:
            content = [
                ("1", Colors.color(f"{X}4")),
                ("2", Colors.color(f"{X}3")),
                ("3", Colors.color(f"{X}2")),
                ("4", Colors.color(f"{X}1")),
                ("5", Colors.color(f"{X}6")),
                ("6", Colors.color(f"{X}5")),
                ("7", Colors.color(f"{X}7")),
            ]
        else:
            content = [
                ("1", Colors.color(f"{X}1")),
                ("2", Colors.color(f"{X}2")),
                ("3", Colors.color(f"{X}3")),
                ("4", Colors.color(f"{X}4")),
                ("5", Colors.color(f"{X}5")),
                ("6", Colors.color(f"{X}6")),
                ("7", Colors.color(f"{X}7")),
            ]
        # Setup initial square
        N = square
        g.put(N, "N", Colors.square_color(N))
        # Add the initial square to a list so we can generate more
        N = [N]
        for c in content:
            N = g.generate(
                squares = N, 
                put = True, 
                content = c[0], 
                color = c[1],
            )
    
    def _color():
        """Returns the color of a piece (dark/light square)."""


    # Initialize the grid
    g = Grid(dimensions)
    # Place friendlies
    for f in friendlies:
        g.put(f, "F", Colors.square_color(f))
    # Place knights and color the map according to movement
    for square in knights:
        _gen(g, square)
    # Print to stdout
    print(g.display(showLabels=showLabels))



if __name__ == "__main__":

    # Setup parameters
    knights = [
        (7,7),
    ]
    friendlies = []
    dimensions = (16,16)
    showLabels = True
    reverse = False

    # Do the thing
    main(
        knights = knights,
        friendlies = friendlies,
        dimensions = dimensions,
        showLabels = showLabels,
        reverse = reverse,
    )



