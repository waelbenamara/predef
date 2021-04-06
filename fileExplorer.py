import os

def exploreFiles(rootPath):
    filesList = []
    for file in os.listdir(rootPath):
        if os.path.isfile((os.path.join(rootPath, file))):
            if file.endswith(".py"):
                if file.startswith("get-pip"):
                    continue
                filesList.append(os.path.join(rootPath, file))
        else:
            exploreFiles(os.path.join(rootPath, file))
    return filesList

def mergeFiles(files):
    with open('projectFile.py', 'w') as outfile:
     for file in files:
        with open(file) as infile:
            outfile.write(infile.read())
        outfile.write("\n")

# if __name__ == "__main__":
#    print(exploreFiles("p1"))