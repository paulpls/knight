"""
    Copyright (C) 2022 paulpls <https://github.com/paulpls>
    
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


class Runtime:

    @staticmethod
    def run(knights=[(3,3)], friendlies=[], dimensions=(8,8), showLabels=True, reverse=False):
        """
            Show a map with knights placed arbitrarily on the board.
                
          knights: List of (x,y) coords for placing knights
       friendlies: List of (x,y) coords for placing friendly pieces
       dimensions: Board dimensions
       showLabels: Show content labels
          reverse: Use 'reverse' (enemy) highlighting
    
        """
        def _gen(grid, square):
            """Place the knight on `square` and color the map according to its movement."""
            # Setup highlighting scheme
            X = "L" if showLabels else "H"
            if reverse:
                # In 'reverse' color, the 4th pass marks the BEST squares to be on if you
                #   are a defending piece. These squares take a long time to reach for an
                #   attacking knight. Though there are further squares that may take longer,
                #   in terms of a typical chessboard, some of these destinations are close
                #   enough to the knight's starting square that it can really present a
                #   difficulty getting there without sacrificing time.
                content = [
                    ("1", Colors.color(f"{X}4")),
                    ("2", Colors.color(f"{X}3")),
                    ("3", Colors.color(f"{X}2")),
                    ("4", Colors.color(f"{X}1")), # [!] Ideal squares
                    ("5", Colors.color(f"{X}6")),
                    ("6", Colors.color(f"{X}5")),
                    ("7", Colors.color(f"{X}7")),
                ]
            else:
                # In normal color, the 4th pass marks some of the WORST squares to reach if
                #   are a knight on the offence. Inversely to the logic above, these squares
                #   take the longest time to reach of any nearby destination.
                content = [
                    ("1", Colors.color(f"{X}1")),
                    ("2", Colors.color(f"{X}2")),
                    ("3", Colors.color(f"{X}3")),
                    ("4", Colors.color(f"{X}4")), # [!] Inopportune squares
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
    
    
        # Initialize the grid and success detector
        g = Grid(dimensions)
        successful = True
        # Place friendlies
        for friend in friendlies:
            # Test for validity
            if g.test(friend, purpose="place friend"):
                g.put(friend, "F", Colors.square_color(friend))
            else:
                successful = False
        # Place knights and color the map according to movement
        for knight in knights:
            # Test for validity
            if g.test(knight, purpose="place knight"):
                g.put(knight, "N", Colors.square_color(knight))
                _gen(g, knight)
            else:
                successful = False
        # Print to stdout if success is detected
        if successful:
            print(
                g.display(
                    showLabels=showLabels,
                )
            )



