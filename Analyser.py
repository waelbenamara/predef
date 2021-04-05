from radon.complexity import average_complexity, cc_visit
from radon.raw import analyze


def cyclomaticComplexity(filename):
    with open(filename) as fobj:
        source = fobj.read()
        cc = cc_visit(source)
        return average_complexity(cc)


def generateRawMetrics(filename):
	with open(filename) as fobj:
         source = fobj.read()
	x = analyze(source)

def numberOfOperators(filename):
    with open(filename) as fobj:
        source = fobj.read()
    x = analyze(source)
    return x.loc

# def numberOfOperands():

# def totalNumberOfOperators():

# def totalNumberOfOperands():

# def halsteadProgramLength():

# def linesOfCode():

# def linesOfComments():


if __name__ == "__main__":
    print(numberOfOperators("test.py"))
    print(cyclomaticComplexity("test.py"))
