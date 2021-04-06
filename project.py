from fileExplorer import exploreFiles,mergeFiles
from Analyser import Analyser
class Project:
    def __init__(self, rootpath):
        self.rootFolder = rootpath
        self.files = exploreFiles(rootpath)
        self.NumberOfOperators = 0
        self.NumberOfOperands = 0
        self.TotalNumberOfOperators = 0
        self.TotalNumberOfOperands = 0
        self.HalsteadProgramLength = 0
        self.LinesOfCode = 0
        self.McCabeCyclomaticComplexity = 0
        self.LinesOfComments = 0

    def analyse(self):
    	print(self.files)
    	for file in self.files:
    		analyser = Analyser(file)
    		self.McCabeCyclomaticComplexity= self.McCabeCyclomaticComplexity + analyser.cyclomaticComplexity()
    		self.NumberOfOperators = self.NumberOfOperators + analyser.numberOfOperators()
    		self.NumberOfOperands= self.NumberOfOperands + analyser.numberOfOperands()
    		self.TotalNumberOfOperators = self.TotalNumberOfOperators + analyser.totalNumberOfOperators()
    		self.TotalNumberOfOperands = self.TotalNumberOfOperands + analyser.totalNumberOfOperands()
    		self.LinesOfCode = self.LinesOfCode + analyser.linesOfCode()
    		self.LinesOfComments = self.LinesOfComments + analyser.linesOfComments()
    		self.HalsteadProgramLength = self.HalsteadProgramLength + analyser.halsteadProgramLength()
    	self.McCabeCyclomaticComplexity = self.McCabeCyclomaticComplexity/(len(self.files))
    	
    	
    		


