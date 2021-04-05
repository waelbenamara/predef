import os

def exploreFiles(rootPath):
    for file in os.listdir(rootPath):
        if os.path.isfile((os.path.join(rootPath, file))):
            if file.endswith(".py"):
                print(os.path.join(rootPath, file))
        else:
            exploreFiles(os.path.join(rootPath, file))


if __name__ == "__main__":
    exploreFiles("p1")