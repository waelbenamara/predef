import os

def exploreFiles(rootPath):
    filesList = []
    for file in os.listdir(rootPath):
        if os.path.isfile((os.path.join(rootPath, file))):
            if file.endswith(".py"):
                filesList.append(os.path.join(rootPath, file))
        else:
            exploreFiles(os.path.join(rootPath, file))
    return filesList

# if __name__ == "__main__":
#    print(exploreFiles("p1"))