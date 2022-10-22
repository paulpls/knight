"""
    Copyright (C) 2022 Paul Clayberg <https://github.com/paulpls>
    
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
from app import Runtime
if __name__ == "__main__":

    ############################################################
    #                                                          #
    #    Edit this block to modify the output parameters.      #
    #                                                          #
    # 

    # Dimensions
    xmax = 8
    ymax = 8

    # Initial position - (x=0, y=0) is top left
    #          (x=xmax-1, y=ymax-1) is bottom right
    x = 3
    y = 3

    # Movement vector
    a = 1   # If both values are even, or if both are odd, the
    b = 2   # pieces will only move between like-colored squares.

    # List of (x,y) coordinates for knights on the board
    knights = [
        (x,y),
    ]

    # List of (x,y) coordinates for friendly pieces on the board
    friendlies = [
        # Example: Surround piece with friendlies
        #(x+a, y+b), (x+b, y+a),
        #(x+a, y-b), (x+b, y-a),
        #(x-a, y+b), (x-b, y+a),
        #(x-a, y-b), (x-b, y-a),
    ]

    # Show numeric labels (pieces are always shown)
    showLabels = True

    # Use 'reverse' highlighting
    reverse = False

    #                                                          #
    #    ------------------------------------------------      #
    #                                                          #
    ############################################################

    # Do the thing
    Runtime.run(
        knights = knights,
        friendlies = friendlies,
        dimensions = (xmax, ymax),
        showLabels = showLabels,
        reverse = reverse,
        vector = (a,b),
    )



