print("x")

from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
    [1, 1, 0, 0, 0, 0,],
    [1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1,],
    [1, 1, 0, 0, 0, 0,]]


grid = Grid(matrix = matrix)

start = grid.node(0,0)
end = grid.node(5,2)

finder = AStarFinder(diagonal_movement= DiagonalMovement.always)

path, runs = finder.find_path(start, end, grid)

print(path)
