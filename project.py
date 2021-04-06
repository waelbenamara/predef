from fileExplorer import exploreFiles
class Project:
    def __init__(self, rootpath):
        self.rootFolder = rootpath
        self.files = exploreFiles(self.rootFolder)
        self.allRawMetrics = None
        self.allmcCabeMetrics = None
        self.allHalsteadMetrics = None

    