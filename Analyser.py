from radon.complexity import average_complexity, cc_visit
from radon.raw import analyze
from radon.metrics import h_visit

class Analyser:
	def __init__(self, filename):
		with open(filename) as fobj:
			self.sourceFile = fobj.read()
		self.rawMetrics = self.generateRawMetrics()
		self.mcCabeMetrics = self.cyclomaticComplexity()
		self.halsteadMetrics = self.generateHalsteadMetrics()
		
	
	def cyclomaticComplexity(self):
		cc = cc_visit(self.sourceFile)
		return average_complexity(cc)


	def generateRawMetrics(self):
		raw = analyze(self.sourceFile)
		return raw

	def generateHalsteadMetrics(self):
		hl = h_visit(self.sourceFile)
		return hl


	def numberOfOperators(self):
		return self.halsteadMetrics.total[0]

	def numberOfOperands(self):
		return self.halsteadMetrics.total[1]

	def totalNumberOfOperators(self):
		return self.halsteadMetrics.total[2]

	def totalNumberOfOperands(self):
		return self.halsteadMetrics.total[3]

	def halsteadProgramLength(self):
		return self.halsteadMetrics.total[5]

	def linesOfCode(self):
		return self.rawMetrics.loc

	def linesOfComments(self):
		return self.rawMetrics.comments

if __name__ == "__main__":
	analyzer = Analyser("test.py")
	print(analyzer.halsteadProgramLength())
	print(analyzer.linesOfCode())
	print(analyzer.linesOfComments())
	print(analyzer.numberOfOperands())
	print(analyzer.numberOfOperators())
	print(analyzer.totalNumberOfOperands())
	print(analyzer.totalNumberOfOperators())
