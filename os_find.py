import os

class DirectorySearch:
    def find(self, path, dir):
        try: 
            os.chdir(path)
        except Exception as e:
            print(e)
        wdir = os.getcwd()
        for searchDir in os.listdir("."):
            if searchDir == dir:
                print(os.getcwd() + dir)
                self.find(wdir + searchDir, dir)

search = DirectorySearch()
search.find("./tree", "python")
        

