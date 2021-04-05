from radon.complexity import cc_visit


filename = "test.py"

with open(filename) as fobj:
	source = fobj.read()

cc = cc_visit(source)
print(cc[0].complexity)

