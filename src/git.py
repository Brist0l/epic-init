import subprocess 

class Git:
    def __init__(self):
        self.git_installed = True

    def check_git(self):
        return True if "usr/bin/git" in subprocess.run("which git",capture_output=True,shell=True).stdout.decode else False
    



