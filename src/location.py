import os
import colorama
import sys
import getpass

class Location:
    def __init__(self,directory:str):
        colorama.init(autoreset=True)

        self.is_dir = True
        self.dir = directory
            
        self.quesion = colorama.Fore.BLUE
        self.hints = colorama.Fore.GREEN
        self.errors = colorama.Fore.RED
        self.paragraphs = colorama.Fore.LIGHTBLUE_EX

        self.yes = ["","y","Y","Yes","yes","ha bancho"]

    def check_dir(self):
        return True if os.path.isdir(self.dir) else False

    def create_path(self):
        if self.check_dir() is False:
            print(f"{self.errors}[-] Folder Does not exist !")
            dir_make = input(f"{self.quesion}Do You Want To Create The Directory? :")
            if dir_make not in self.yes:
                sys.exit(f"{colorama.Fore.CYAN}ThankYou for using epic-init")   
            print(f"{self.paragraphs}[+] Creating Directory {self.hints}{self.dir}")
            try:
                os.mkdir(self.dir)
            except PermissionError:
                print(f"{self.errors}[-] Error With Permisions.")
                print(f"{self.paragraphs} Root Password Would Be Needed.")
            except OSError as error:
                print(f"[-]Error : {self.errors}{error}{colorama.Fore.RESET} occured.")
                          
        
if __name__ == "__main__": 
    Location("/root/hello").create_path()
