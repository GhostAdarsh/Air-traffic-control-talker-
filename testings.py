# this is to stage tests from all github uploads: 

print("x")
import pathfinding 
from pathfinding import * 
from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder

matrix = [
    1, 1, 1, 1, 1,
    1, 0, 1, 1, 1,
    1, 1, 1, 1, 1,
]
grid = Grid(matrix= matrix) 

# start and end nodes 
start = grid.node(0,0)
end = grid.node(5,2)

#creaste a finder with a movement style 
finder = AStarFinder

# use finder to find path 
path,runs = finder.find_path(start,end, grid) 

# print result 
print(path) 