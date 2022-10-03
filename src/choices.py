import colorama,os,readline

import location,autocomplete,check

class Choice:
    def __init__(self):
        colorama.init(autoreset=True)
        
        self.chk = check.Check()
        self.lct = None

        self.use_git = True
        self.folder_name = ""
        self._host_online = True
        self._start_now = True
        self._editor_exec = None

        self.question = colorama.Fore.BLUE
        self.hints = colorama.Fore.GREEN
        self.red = colorama.Fore.RED
        self.reset = colorama.Style.RESET_ALL
        self.yes = ["","y","Y","Yes","yes"]
    
    def git(self):
        if not input(f"{self.question}Do You Want To Work With Git(Y/n): {self.reset}") in self.yes: # checks if git has to be used or not
           self.use_git = True

        # users wants to use git 
        # 
        # checking if git is installed or not
        if self.use_git and self.chk.checkGit():
            print(f"{self.hints}[+] Git Present")
        else:
            print(f"{self.red}[-] Git Not Found!")
            self.use_git = False
   
    def location(self):
        while self.folder_name == "":
            print(f"\n{self.hints}Hint: Press {colorama.Fore.RED}Tab{colorama.Fore.GREEN} for autocompletion.\nThis would create a folder with the same name\n")
            readline.set_completer(autocomplete.MyCompleter([x for x in os.listdir(os.path.expanduser('~'))]).complete)
            readline.parse_and_bind('tab: complete')
            self.folder_name = input(f"{self.question}Enter Location of project:{self.reset} ")
        self.lct = location.Location(self.folder_name)
        self.lct.create_path()

    def host_online(self):
        if self.use_git == True:
            if not input(f"\n{self.question}Do You Want To Host It Online (Github) ? (Y/n){self.reset} ") in self.yes:
                self._host_online = False
    
    def start_now(self):
        if not input(f"\n{self.question}Do You Want To Start Now ? (Y/n){self.reset} ") in self.yes:
            self._start_now = False
    
    def editor(self):
        if self._start_now:
            _editor = ""
            while _editor == "":
                _editor = input(f"\n{self.question}What is your editor of Choice? {self.reset}")
            self._editor_exec = self.chk.checkEditor(_editor)
            if self._editor_exec != "unknown editor":
                print(f"{self.hints}Starting {self._editor_exec}{self.reset}")
                os.system(f"{self._editor_exec} \"{self.path}\"")
            #else:
            #    print(f"{self.red} [-] Unrecognized editor; please enter the editor executable path:", end="")
            #    while True:
            #        self._editor_exec = self.chk.checkEditor(input("Enter path: "))
            #        if self._editor_exec == "unknown editor":
            #            print(f"{self.hints}Starting {self._editor_exec}{self.reset}")
            #            os.system(f"{self._editor_exec} \"{self.path}\"")
            #            break
            #            print(f"{self.red}[-] That command doesn't work; try again{self.reset} ", end="")
            #            continue
            ## TODO: ADD CHECK IF UNKNOWN EDITOR

    def get_value(self) -> dict:
        return {
            "useGit": self.use_git,
            "path":self.lct.get_path() ,
            "hostOnline": self._host_online, 
            "startNow": self._start_now,
            "editor": self._editor_exec
        }