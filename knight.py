"""
    Copyright (C) 2022  paulpls <https://github.com/paulpls>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
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
        (15,15),
    ]
    friendlies = []
    dimensions = (32,32)
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



