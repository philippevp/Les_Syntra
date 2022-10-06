import turtle as turtle
from utils.usefull_functions import teken_huis

# Maak class Huis
# maak ''' comment '''
# toon help()
# verschillende __init__ tonen
# method teken()
# attribuut zonder init toevoegen
# class Point
# print(Object)
# __str__
# print(Object)

class Huis:
    '''
    Dit is een huis in turtle
    '''
    def __init__(self):
        self.lengte = int()

    def __str__(self):
        return f"huis met lengte {self.lengte}, naam {self.naam}"

    def set_lengte(self, lengte):
        self.lengte = lengte
    
    def get_lengte(self):
        return self.lengte

    def set_naam(self, naam):
        self.naam = naam
    
    def teken(self):
        teken_huis(self.lengte)



thuis = Huis()
thuis.set_naam("weltevree")
# print(thuis)
thuis.set_lengte(100)

print(thuis)

thuis.teken()

turtle.done()

# print(thuis.lengte)

# x = thuis.get_lengte()
# print(x)

# buur = Huis()
# print(buur.get_lengte())
# buur.set_lengte(50)
# print(buur.get_lengte())
# print(thuis.get_lengte())

# print(help(Huis))











# turtle.mainloop()


