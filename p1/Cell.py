class Cell:
	def __init__(self,data,x,y):
		self.west = None
		self.north = None
		self.east = None
		self.south = None
		self.westcost = 2
		self.eastcost = 2
		self.northcost = 3
		self.southcost = 1
		self.x = x
		self.y = y
		self.data = data
		self.depth = None
		self.is_obstacle = False

	def list_ordered_adj(self):
		return [self.west,self.north,self.east,self.south]
		
	def preOrderDFS(self,root)
		if root:
			print(root.x,root.y)
			self.preOrderDFS(root.west)
			self.preOrderDFS(root.north)
			self.preOrderDFS(root.east)
			self.preOrderDFS(root.south)





