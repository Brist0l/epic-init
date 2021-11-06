import colorama

colorama.init(autoreset=True)
class Choice:
    def __init__(self):
        colorama.init(autoreset=True)
       
        self.use_git = True
        self.path = ""
        self._host_online = True
        self._start_now = True

        self.quesion = colorama.Fore.BLUE
        self.hints = colorama.Fore.GREEN
        self.yes = ["","y","Y","Yes","yes","ha bancho"]
    
    def git(self):
        if not input(f"{self.quesion}Do You Want To Work With Git(Y/n):") in self.yes:
           self.use_git = False 
   
    def location(self):
        while self.path == "":
            print(f"{self.hints}Hint: Press {colorama.Fore.RED}Tab{colorama.Fore.GREEN} for autocompletion.")
            #readline.set_completer(autocomplete.MyCompleter([x for x in os.listdir(f"/home/{getpass.getuser()}")]).complete)
            #readline.parse_and_bind('tab: complete')
            self.path=input(f"{self.quesion}Enter Location of project:") 
   
    def host_online(self):
        if not input(f"{self.quesion}Do You Want To Host It Online (Github) ? (Y/n)") in self.yes:
            self._host_online = False
    
    def start_now(self):
        if not input(f"{self.quesion}Do You Want To Start Now ? (Y/n)") in self.yes:
            self._start_now = False
    
    def _value(self):
        return self.use_git,self.path,self._host_online,self._start_now

if __name__ == "__main__":
    x=Choice()
    x.git()
    x.location()
    x.host_online()
    x.start_now()

