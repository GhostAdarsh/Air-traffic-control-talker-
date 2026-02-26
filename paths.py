import pathfinding 
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
grid = Grid(matrix=matrix)
start = grid.node(0, 0)  # Starting position (x=0, y=0)
end = grid.node(9, 5)    # Ending position (x=9, y=5)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path = finder.find_path(start, end, grid)
grid.cleanup()
print(path)
