class Result:
    def __init__(self, project):
        self.NumberOfOperators = project.NumberOfOperators
        self.NumberOfOperands = project.NumberOfOperands
        self.TotalNumberOfOperators = project.TotalNumberOfOperators
        self.TotalNumberOfOperands = project.TotalNumberOfOperands
        self.HalsteadProgramLength = project.HalsteadProgramLength
        self.LinesOfCode = project.LinesOfCode
        self.McCabeCyclomaticComplexity = project.McCabeCyclomaticComplexity
        self.LinesOfComments = project.LinesOfComments
