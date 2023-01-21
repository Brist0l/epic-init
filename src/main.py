import choices, route, colorama, location

class Order:
    def __init__(self):
        colorama.init()
        
        self.true = colorama.Fore.GREEN # color for a value if it is true
        self.false = colorama.Fore.RED  # color for a value if it is false
        
        #( 0  ,    1     ,       2     ,      3   )
        #(Git , Location , host_online , start_now)

        self.values = None 
        # print(f"{self.true}[+] All Files Present" if route.Route().file_check() else f"{self.false}[-] All Files Are Not Present")

    def get_choices(self):
        x = choices.Choice()
        x.git()
        x.location()
        x.host_online()
        x.start_now()
        x.editor()
        self.values = x.get_value()
        print(f"{colorama.Fore.YELLOW} These are the values:")
        for i in self.values.keys():
            print(f"{i}: {self.values.get(i)}")

    def location(self):
       location.Location(self.values[1])
    
x=Order()
x.get_choices()

