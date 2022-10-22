import turtle as turtle
import math

def teken_veelhoek(lengte, hoeken, richting):
    for x in range(hoeken):
        turtle.forward(lengte)
        if richting == "left":
            turtle.left(360/hoeken)
        elif richting == "right":
            turtle.right(360/hoeken)


def teken_vierkant(lengte):
    for x in range(4):
        turtle.forward(lengte)
        turtle.left(90)


def teken_driehoek(lengte, richting="right"):
    for x in range(3):
        turtle.forward(lengte)
        if richting == "right":
            turtle.right(120)
        elif richting == "left":
            turtle.left(120)


# def teken_huis(lengte):
#     teken_vierkant(lengte= lengte)
#     teken_driehoek(lengte)   

def teken_huis(lengte):
    teken_veelhoek(lengte, 4, "left")
    turtle.setheading(90)
    turtle.forward(lengte)
    turtle.setheading(60)
    teken_veelhoek(lengte, 3, "right")



def teken_parallelogram(lengte_A, lengte_B, hoek):
    turtle.forward(lengte_A)
    turtle.left(hoek)
    turtle.forward(lengte_B)
    turtle.left(180-hoek)
    turtle.forward(lengte_A)
    turtle.left(hoek)
    turtle.forward(lengte_B)
    turtle.left(180-hoek)


def distance_between_points(point_1, point_2):
    som_kwadraten = math.pow((point_2.x-point_1.x), 2) + math.pow((point_2.y-point_1.y), 2)
    return math.sqrt(som_kwadraten)

def hoogte_gelijkbenige_driehoek(lengte):
    return math.sqrt(math.pow(lengte,2) - math.pow(lengte/2, 2))