from fileExplorer import exploreFiles,mergeFiles
from Analyser import Analyser
class Project:
    def __init__(self, rootpath):
        self.rootFolder = rootpath
        self.source = mergeFiles(exploreFiles(rootpath),rootpath)
        self.allRawMetrics = None
        self.allmcCabeMetrics = None
        self.allHalsteadMetrics = None
    	