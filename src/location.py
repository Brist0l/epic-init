import os
import colorama
import sys
import getpass
import subprocess

class Location:
    def __init__(self,directory:str):
        colorama.init(autoreset=True)

        self.is_dir = True
        self.dir = directory
            
        self.quesion = colorama.Fore.BLUE
        self.hints = colorama.Fore.GREEN
        self.errors = colorama.Fore.RED
        self.paragraphs = colorama.Fore.LIGHTBLUE_EX

        self.yes = ["","y","Y","Yes","yes"]

    def _check_dir(self):
        return True if os.path.isdir(self.dir) else False

    def create_path(self):
        if self._check_dir() is False:
            print(f"{self.errors}[-] Folder Does not exist !")
            dir_make = input(f"{self.quesion}Do You Want To Create The Directory? :")
            if dir_make not in self.yes:
                sys.exit(f"{colorama.Fore.CYAN}Thankyou for using epic-init")   
            print(f"{self.paragraphs}[+] Creating Directory {self.hints}{self.dir}")
            try:
                os.mkdir(self.dir)
                print(f"{self.paragraphs}[+]Folder Made")
            except PermissionError:
                print(f"{self.errors}[-] Error With Permisions.")
                print(f"{self.paragraphs}Root Password Would Be Needed.")
                x =input(f"{self.quesion}Do You Want Still Want To Continue? :")
                if x not in self.yes:
                    sys.exit("ThankYou For Using Epic Init")
                
                self._create_path_root()
        
            except OSError as error:
                sys.exit(f"[-]Error : {self.errors}{error}{colorama.Fore.RESET} occured.") 
            return 0
    
    def _create_path_root(self):
        print(f"User:{getpass.getuser()}")
        passwd=getpass.getpass(f"{self.quesion}Enter Root Password >")
        x=subprocess.Popen(f"sudo -S mkdir -p {self.dir}",stdin=subprocess.PIPE,shell=True)
        x.stdin.write(bytes(passwd,encoding="utf-8"))
        x.stdin.flush()
        print(f"{self.paragraphs}[+]Folder Made")
        return 0

    def get_path(self):
        if self.create_path() or self._create_path_root():
            return self.dir
        else:
            print(f"{self.errors}[-]Error In Locations")

if __name__ == "__main__": 
    Location("/something/of/maa").create_path()
