import imp


import math
from unittest import result

def cost_per_square_of_pizza(prijs, diameter):
    straal = diameter/2
    oppervlakte = math.pi * (straal ** 2)
    result = prijs / oppervlakte

    print(f"{result}")
    return result

cost_per_square_of_pizza(18, 18)