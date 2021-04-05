from Cell import Cell
import numpy as np
import collections
class Maze:
	def __init__(self,x,y):
		self.cells = [[]]
		self.start = None
		self.goal = None
		self.x = x
		self.y = y
		self.depth = 4



	def print_maze(self):
		print("-----------------")
		for x in self.cells:
			line = ""
			for y in x:
				line = line + y.data
			line = line+ " | "
			print(line)
		print("-----------------")

	def get_cell(self,x,y):
		tmp = np.array(self.cells)
		tmp = tmp.flatten()
		for cell in tmp:
			if cell.x == x and cell.y == y:
				return cell

		
	def set_direction(self):
		tmp = np.array(self.cells)
		tmp = tmp.flatten()
		for cell in tmp:
			print(cell.x,cell.y)
			#set west
			if cell.x == 0:
				cell.west = None
			else:
				cell.west = self.get_cell(cell.x -1,cell.y)

			# set north
			if cell.y == self.y:
				cell.north = None
			else:
				cell.north = self.get_cell(cell.x, cell.y+1)

			#set east
			if cell.x == self.x:
				cell.east = None
			else:
				cell.east = self.get_cell(cell.x+1,cell.y)

			#set south
			if cell.y == 0:
				cell.south == None
			else:
				cell.south = self.get_cell(cell.x,cell.y-1)

	def set_depths(self):
		tmp = np.array(self.cells)
		tmp = tmp.flatten()
		for cell in tmp:
			delta_x = abs(self.start.x - cell.x)
			delta_y = abs(self.start.y - cell.y)
			cell.depth = max(delta_x, delta_y)





	def DLS(self):
		tmp = np.array(self.cells)
		tmp = tmp.flatten()
		tmp = tmp.tolist()
		tmp_2 = []
		print(len(tmp))
		print("self depth ",self.depth)
		for cell in tmp:
			print(cell.x,cell.y,cell.depth,self.depth)
			if cell.depth <= self.depth:
				tmp_2.append(self.get_cell(cell.x, cell.y))
		counter = 0
		print('---------------------')
		for cell in tmp_2 :
			cell.data = str(counter) + "  "
			counter = counter + 1
		for cell in tmp_2:
			print(cell.x,cell.y)

	def DLS_2(self,node):
		ordered_list = [node]
		if (node.west!= None) and (node.west.is_obstacle  == False) and (node.west.depth <= self.depth):
			#self.DLS_2(node.west)
			print("I can go west")
		else:
			print("cannot go west")
			ordered_list.append(node.east)

		if (node.north!= None) and (node.north.is_obstacle == False) and (node.north.depth <= self.depth):
			#self.DLS_2(node.north)
			print("")
		else:
			ordered_list.append(node.north)

		if (node.east!= None) and (node.east.is_obstacle  == False) and (node.east.depth <= self.depth):
			#self.DLS_2(node.east)
			print("")
		else:
			ordered_list.append(node.west)

		if (node.south!= None) and (node.south.is_obstacle  == False) and (node.south.depth <= self.depth):
			#self.DLS_2(node.south)
			print("")
		else:
			ordered_list.append(node.west)

		print("ffffffffff")
		for cell in ordered_list:
			print(cell.x,cell.y)

	


	def DLS_3(self,node):
		#ordered_list = node
		explored = [node]
		while True:
			if (node.west!= None) and (node.west.is_obstacle  == False) and (node.west.depth <= self.depth) and (node.west not in explored):
				node.west.data = "mm "
				node = node.west
				explored.append(node)
				continue
				#self.DLS_3(node)

			if (node.north!=None) and (node.north.is_obstacle == False) and (node.north.depth <= self.depth ) and (node.north not in explored):
				node.north.data = "mm "
				node = node.north
				explored.append(node)
				continue
				#self.DLS_3(node)

			if (node.east!= None) and (node.east.is_obstacle  == False) and (node.east.depth <= self.depth) and (node.east not in explored):
				node.east.data = "mm "
				node = node.east
				explored.append(node)
				continue
				#self.DLS_3(node)

			if (node.south!= None) and (node.south.is_obstacle  == False) and (node.south.depth <= self.depth) and (node.south not in explored):
				node.south.data = "mm "
				node = node.south
				explored.append(node)
				continue
				#self.DLS_3(node)

			return explored

	def LSD_4(self,node):
		counter = 1
		explored_set = collections.deque([node])
		explored_2 = [node]
		while (len(explored_set)>0):
			current_node = explored_set.pop()
			print(len(explored_set))
			#print(current_node.x,current_node.y)
			frontier = current_node.list_ordered_adj()
			try:
				print("west ",frontier[0].x,frontier[0].y)
			except:
				print("west = Nome")
			try:
				print("north ",frontier[1].x,frontier[1].y)
			except:
				print("north = Nome")
			try:	
				print("east ",frontier[2].x,frontier[2].y)
			except:
				print("east = None")
			try:	
				print("south ",frontier[3].x,frontier[3].y)
			except :
				print("south = None")
			for adjacent in frontier:
				if (adjacent != None) and (adjacent.is_obstacle == False) and (adjacent.depth <= self.depth) and (adjacent not in explored_2):
					tmp = str(counter)
					if len(tmp) == 1:
						tmp = "0"+tmp+" "
					else:
						tmp = tmp +" "
					adjacent.data = tmp
					explored_set.append(adjacent)
					explored_2.append(adjacent)
					counter = counter + 1
			self.print_maze()
					#return ""
		return explored_set














			

				



	'''				
	def IDS(self):
		explored = []
		frontier = [self.start]
		for node in frontier:
			if node != self.goal:
				frontier.pop()
	'''





	

			


