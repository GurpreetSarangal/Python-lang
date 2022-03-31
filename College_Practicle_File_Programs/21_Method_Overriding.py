class parent1:
    def print_name(self):
        print("Hello World")
    
class child(parent1):
    def print_name(self):
        print("Hi World")
        parent1.print_name(self)

obj = child()
obj.print_name()
    
