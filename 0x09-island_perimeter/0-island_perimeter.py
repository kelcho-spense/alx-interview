#!/usr/bin/python3
""" Module that contains the island_perimeter function """


def island_perimeter(grid):
    """ Function that returns the perimeter of island described in grid
    Args:
        grid (list[list(int)]): An island

    Returns:
        perimeter (int): Perimeter of the island.

    """
    perimeter = 0

    if grid != []:
        nColumns = len(grid[0])
        nRows = len(grid)

    for a in range(nRows):
        for b in range(nColumns):
            if grid[a][b] == 1:
                if (a - 1) == -1 or grid[a - 1][b] == 0:
                    perimeter += 1
                if (a + 1) == nRows or grid[a + 1][b] == 0:
                    perimeter += 1
                if (b - 1) == -1 or grid[a][b - 1] == 0:
                    perimeter += 1
                if (b + 1) == nColumns or grid[a][b + 1] == 0:
                    perimeter += 1

    return perimeter
