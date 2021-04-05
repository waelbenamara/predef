from Cell import Cell
from Maze import Maze
from varname import nameof

cell00 = Cell('oo ',0,0)
cell10 = Cell('oo ',1,0)
cell20 = Cell('oo ',2,0)
cell30 = Cell('oo ',3,0)
cell40 = Cell('oo ',4,0)

cell01 = Cell('oo ',0,1)
cell11 = Cell('## ',1,1)
cell21 = Cell('oo ',2,1)
cell31 = Cell('oo ',3,1)
cell41 = Cell('oo ',4,1)

cell02 = Cell('ss ',0,2)
cell12 = Cell('## ',1,2)
cell22 = Cell('## ',2,2)
cell32 = Cell('oo ',3,2)
cell42 = Cell('oo ',4,2)

cell03 = Cell('oo ',0,3)
cell13 = Cell('## ',1,3)
cell23 = Cell('gg ',2,3)
cell33 = Cell('oo ',3,3)
cell43 = Cell('oo ',4,3)

cell04 = Cell('oo ',0,4)
cell14 = Cell('## ',1,4)
cell24 = Cell('## ',2,4)
cell34 = Cell('oo ',3,4)
cell44 = Cell('oo ',4,4)

cell05 = Cell('oo ',0,5)
cell15 = Cell('oo ',1,5)
cell25 = Cell('oo ',2,5)
cell35 = Cell('oo ',3,5)
cell45 = Cell('oo ',4,5)

cell11.is_obstacle = True
cell12.is_obstacle = True
cell22.is_obstacle = True
cell13.is_obstacle = True
cell14.is_obstacle = True
cell24.is_obstacle = True


my_maze = Maze(5,6)



maze = [[cell05,cell15,cell25,cell35,cell45],
		[cell04,cell14,cell24,cell34,cell44],
		[cell03,cell13,cell23,cell33,cell43],
		[cell02,cell12,cell22,cell32,cell42],
		[cell01,cell11,cell21,cell31,cell41],
		[cell00,cell10,cell20,cell30,cell40]]
my_maze.cells = maze

my_maze.start = cell02
my_maze.goal = cell23

my_maze.print_maze()
my_maze.set_direction()
my_maze.set_depths()

my_maze.LSD_4(my_maze.start)
my_maze.print_maze()










		



