import os

class Location:
    def __init__(self,directory:str):
        self.is_dir = True
        self.dir = directory

    def check_dir(self):
        return True if os.path.isdir(self.dir) else False
