![banner](https://user-images.githubusercontent.com/62158353/196378923-aadf87eb-f64b-44fb-932f-153afc182829.png)
  
# Knight Map
  
version: 1.0.0  
author: [paulpls](https://github.com/paulpls)  
license: [GPL 3.0](./LICENSE.md)  
  

## PURPOSE
  
Generates a map based on the movements of the knight piece in chess.
  
Given coordinates `(x,y)`, the knight can move to squares within the following set:
  
    N(x,y)  =  ( x ± a, y ± b )  ∪  ( x ± b, y ± a )
            for a=1, b=2
  
The knight's complex movement gives rise to many interesting patterns and scenarios. Because the vector is not a pair of even or odd numbers, the knight is forced to change color each time it moves. Due to this, it can only attack squares of an opposite color to its own. Moreover, once the knight moves, it will be able to attack only the same colored squares as that from which it came.
  
This color-swapping compulsion makes some squares quickly reachable, but can be unforgiving in other cases. By making these movement patterns both visible and configurable, this tool aims to help to provide a better understanding of how the knight maneuvers around its environment. The movement vector can also be changed to allow the study of other jumping pieces.
  
Output settings can be changed by modifying the parameters in [knight.py](./knight.py#L23). By placing more knights, friendly pieces, or changing the grid dimensions, countless scenarios can be studied. The movement vector defaults to (1,2), but it can be changed to any pair of positive, non-zero integers.  
  
  
  
## SYNOPSIS
  
```
python knight.py
```
  
  
  
## DEPENDENCIES
- python *(3.8.10)*
- color terminal emulator *(eg xterm)*
  

  
## LICENSE
  
Copyright (C) 2022  [paulpls](https://github.com/paulpls)
    
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
  

  
# SCREENSHOTS
  
**[1]** *Knight in the center, no labels*
  
![knight1](https://user-images.githubusercontent.com/62158353/196326404-e38a6b10-4705-476c-a7e6-8a9d596c1210.png)
  
  
**[2]** *Knight unable to reach corner due to being blocked by friendlies*
  
![knight2](https://user-images.githubusercontent.com/62158353/196326415-230f916c-a8f2-49fa-bb21-ac0e09d72ba6.png)
  
  
**[3]** *Knight unable to leave corner due to being blocked by friendlies*
  
![knight3](https://user-images.githubusercontent.com/62158353/196326425-7b5e1b58-08e4-48c0-9ab6-327711eff6bf.png)
  
  
**[4]** *Two knights in opposite corners with some friendlies*
  
![knight4](https://user-images.githubusercontent.com/62158353/196326432-b25a76c1-5d7a-476f-826b-1f4adc7d6d40.png)
  
  
**[5]** *Knight with only one escape path*
  
![knight5](https://user-images.githubusercontent.com/62158353/196326441-d9e8a576-d70a-4627-8921-8eb4b74959e1.png)
  
  
**[6]** *Knight in corner, unblocked*
  
![knight6](https://user-images.githubusercontent.com/62158353/196326447-33f0a8c7-9d38-4cc1-8efc-9af690a828a5.png)
  
  
  
