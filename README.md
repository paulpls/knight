# Knight Map

author: [paulpls](https://github.com/paulpls)


### PURPOSE

Generates a map based on the movements of the knight piece in chess. The current location of the knight(s) are marked on the board, and each square is labeled according to the number of moves it would take to reach it.


### SYNOPSIS

```
python3 knight.py
```


### OPTIONS (TODO)

The following options will be available for modifying the command output.

| flag                                    | behavior                                                                                                                                                                       |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -l                                      | Display text labels in the squares. Each square is numbered according to how many moves it takes the knight(s) to reach it. This is the default behavior.                      |
| -L                                      | Do not display text labels. Overrides `-l`.                                                                                                                                    |
| -h                                      | Highlight the map according to time, i.e. squares that take the same number of moves to reach will be marked similarly.                                                        |
| -H                                      | Highlight the map in reverse. The map is marked based on how many moves it would take an enemy knight to reach, or capture on, each square. Overrides `-h`.                    |
| -n <num>                                | Set the number of knights to `num`. Must be greater than zero. Defaults to 1.                                                                                                  |
| -g `<x>,<y>`                              | Set the grid dimensions to `x,y`. Both values must be greater than zero. Defaults to 8,8.                                                                                      |
| -f `[(<x0>,<y0>), ...]`                   | Place friendly pieces on each square listed. The knight is unable to move to a piece occupied by a friendly piece, so this option can be used to add complexity to the output. |


### SCREENSHOTS

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



