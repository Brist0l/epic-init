import colorama

colorama.init(autoreset=True)
class Choice:
    def __init__(self) -> None:
        colorama.init(autoreset=True)
       
        self.use_git = True
        self.path = ""
        self._host_online = True
        self._start_now = True
        self._editor = "Not Chosen" 

        self.question = colorama.Fore.BLUE
        self.hints = colorama.Fore.GREEN
        self.reset = colorama.Style.RESET_ALL
        self.yes = ["","y","Y","Yes","yes","ha bancho"]
    
    def git(self) -> None:
        if not input(f"{self.question}Do You Want To Work With Git(Y/n): {self.reset}") in self.yes:
           self.use_git = False 
   
    def location(self) -> None:
        while self.path == "":
            print(f"\n{self.hints}Hint: Press {colorama.Fore.RED}Tab{colorama.Fore.GREEN} for autocompletion.")
            #readline.set_completer(autocomplete.MyCompleter([x for x in os.listdir(f"/home/{getpass.getuser()}")]).complete)
            #readline.parse_and_bind('tab: complete')
            self.path=input(f"{self.question}Enter Location of project:{self.reset} ") 
   
    def host_online(self) -> None:
        if not input(f"\n{self.question}Do You Want To Host It Online (Github) ? (Y/n){self.reset} ") in self.yes:
            self._host_online = False
    
    def start_now(self) -> None:
        if not input(f"\n{self.question}Do You Want To Start Now ? (Y/n){self.reset} ") in self.yes:
            self._start_now = False
    
    def editor(self) -> None:
        if self._start_now:
            self._editor = input(f"\n{self.question}What is your editor of Choice? {self.reset}")

    def get_value(self) -> dict:
        return {
            "useGit": self.use_git,
            "path": self.path,
            "hostOnline": self._host_online, 
            "startNow": self._start_now,
            "editor": self._editor
        }

