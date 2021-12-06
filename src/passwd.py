import os, subprocess
from getpass import getpass

class Getpass:
    def is_root(self):
        return os.geteuid() == 0

    def test_sudo(self,pwd=""):
        args = "sudo -S su".split()
        kwargs = dict(stdout=subprocess.PIPE,
                  encoding="ascii")
        if pwd:
            kwargs.update(input=pwd)
        cmd = subprocess.run(args, **kwargs)
        return ("OK" in cmd.stdout)

    def prompt_sudo(self):
        ok = self.is_root() or self.test_sudo()
        if not ok:
            pwd = getpass("password: ")
            ok  = self.test_sudo(pwd)
        return ok
    def ask(self):
        if self.prompt_sudo():
            print("Access granted !")
            print(self.test_sudo())
        else:
            print("Access denied !")
if __name__ == "__main__":
    Getpass().ask()
