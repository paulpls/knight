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
from app import Runtime
if __name__ == "__main__":

    # NOTE Edit this block to modify the output parameters.
    knights = [
        (3,3),
    ]
    friendlies = []
    dimensions = (8,8)
    showLabels = True
    reverse = False
    vector = (1,2)

    # Do the thing
    Runtime.run(
        knights = knights,
        friendlies = friendlies,
        dimensions = dimensions,
        showLabels = showLabels,
        reverse = reverse,
        vector = vector,
    )



