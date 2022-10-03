import subprocess

class Check:
    def __init__(self) -> None:
        self.yes = ["","y","Y","Yes","yes"]
        self.editors = {
            "vim": ["vim", "vi improved"],
            "nvim": ["nvim", "neovim", "neo vim"],
            "vscode": ["code", "vsc", "vscode", "visual studio code"],
            "atom": ["atom"],
            "codium": ["codium", "vscodium"]
        }

    def checkGit(self) -> bool:
        return subprocess.check_output(["git", "--version"]).decode()[0:3] == "git"

    def checkEditor(self, editor:str) -> str:
        for i in self.editors.values():
            if editor in i:
                return i[0]
        else:
            return "unknown editor"

if __name__ == "__main__":
   chk = Check()
   print("Git Works" if chk.checkGit() else "git failed")
   print(chk.checkEditor("neovim"))

