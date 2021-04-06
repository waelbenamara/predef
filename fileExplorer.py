import os
filesList = []
def exploreFiles(rootPath):
    
    for file in os.listdir(rootPath):
        #print(rootPath)
        #print(os.path.isfile((os.path.join(rootPath, file))))
        if os.path.isfile((os.path.join(rootPath, file))):
            #print(os.path.join(rootPath, file))
            if file.endswith(".py"):
                #print(file)
                filesList.append(os.path.join(rootPath, file))
        else:
            exploreFiles(os.path.join(rootPath, file))
    return filesList

def mergeFiles(files,rootPath):
    with open(rootPath+'.py', 'w') as outfile:
        for file in files:
            with open(file) as infile:
                outfile.write(infile.read())
            outfile.write("\n")
    return rootPath+".py"

# if __name__ == "__main__":
#     print(exploreFiles("p1"))