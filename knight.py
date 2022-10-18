from app.grid import Grid


def main():
    initialSquare = (4,4)
    grid = Grid()
    grid.put(initialSquare)
    print(grid.display())



if __name__ == "__main__":
    main()



