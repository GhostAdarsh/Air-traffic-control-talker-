import pathfinding 
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder


matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
#create a grid 

grid = Grid(matrix = matrix)

# start nd end 

start = grid.node(0,0)
end = grid.node(8, 5)

# create finder movement 
finder = AStarFinder() 

# use finder to find path 

path, runs = finder.find_path(start, end, grid)

print(path)

