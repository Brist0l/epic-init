import os
from collections import Counter
import choices 

class Route:
    def __init__(self):
        self.file_present = ['autocomplete.py','git.py','choices.py','location.py','route.py','main.py']
    
    def file_check(self):
         files=os.listdir(os.getcwd())
         files.remove("__pycache__")

         if Counter(files) == Counter(self.file_present):
             return True
         else:
             return False


        





