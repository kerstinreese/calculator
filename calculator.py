class Calculator:
    def __init__(self, name):
        self.name = name
    def add(self, x, y):
        print(self.name + " hat berechnet: " + str(x) + " + " + str(y) + " = " + str(x + y))
    def sub(self, x,y):
        print(self.name + " hat berechnet: " + str(x) + " - " + str(y) + " = " + str(x - y))
