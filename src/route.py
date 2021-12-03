import os
from collections import Counter
import choices 

class Route:
    def __init__(self):
        self.file_present = ['autocomplete.py','git.py','choices.py','location.py','route.py']
    
    def route(self):
       print(choices.Choice()._value() )

    def _check(self):
         files=os.listdir(os.getcwd())

         if Counter(files) == Counter(self.file_present):
             return True
         else:
             return False


        





