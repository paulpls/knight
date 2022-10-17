#Knight Map

author: [paulpls](https://github.com/paulpls)


###PURPOSE

Generates a map based on the movements of the knight piece in chess. The current location of the knight(s) are marked on the board, and each square is labeled according to the number of moves it would take to reach it.


###SYNOPSIS

```knight [OPTIONS]
```

```knight [OPTIONS] [-n <num>] [-f [(x0,y0), ...]]
```


###OPTIONS

The following options are available for modifying the command output.

| flag                    | behavior                                                                                                                                                                       |   |   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|
| `-l`                    | Display text labels in the squares. Each square is numbered according to how many moves it takes the knight(s) to reach it. This is the default behavior.                      |   |   |
| `-L`                    | Do not display text labels. Overrides `-l`.                                                                                                                                    |   |   |
| `-h`                    | Highlight the map according to time, i.e. squares that take the same number of moves to reach will be marked similarly.                                                        |   |   |
| `-H`                    | Highlight the map in reverse. The map is marked based on how many moves it would take an enemy knight to reach, or capture on, each square. Overrides `-h`.                    |   |   |
| `-n <num>`              | Set the number of knights to `num`. Must be greater than zero. Defaults to 1.                                                                                                  |   |   |
| `-g <x>,<y>`            | Set the grid dimensions to `x,y`. Both values must be greater than zero. Defaults to 8,8.                                                                                      |   |   |
| `-f [(<x0>,<y0>), ...]` | Place friendly pieces on each square listed. The knight is unable to move to a piece occupied by a friendly piece, so this option can be used to add complexity to the output. |   |   |



