from utils.usefull_classes import Point


def calculate_slope(point_1, point_2):
    if isinstance(point_1, tuple) and isinstance(point_2, tuple):
        if point_2[0]-point_1[0] == 0:
            print("De teller is 0, delen door 0 is niet mogelijk")
            slope = "limiet is oneindig"
        else:
            slope = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])

    elif isinstance(point_1, Point) and isinstance(point_2, Point):
        if point_2.x - point_1.x == 0:
            print("De teller is 0, delen door 0 is niet mogelijk")
            slope = "limiet is oneindig"
        else:
            slope = (point_2.y - point_1.y) / (point_2.x - point_1.x)
        
    print(slope)
    return slope

# calculate_slope((0,0), (10, 10))
# calculate_slope(Point(0, 0), Point(0, 20))

def get_tuple_points_from_user():
    print("Voor het eerste punt, ")
    x_coord = int(input("geef de x-coordinaat : "))
    y_coord = int(input("geef de y-coordinaat : "))
    punt_1 = (x_coord, y_coord)
    print("Voor het tweede punt, ")
    x_coord = int(input("geef de x-coordinaat : "))
    y_coord = int(input("geef de y-coordinaat : "))
    punt_2 = (x_coord, y_coord)

    return punt_1, punt_2


def get_obj_points_from_user():
    print("Voor het eerste punt, ")
    x_coord = int(input("geef de x-coordinaat : "))
    y_coord = int(input("geef de y-coordinaat : "))
    punt_1 = Point(x_coord, y_coord)
    print("Voor het tweede punt, ")
    x_coord = int(input("geef de x-coordinaat : "))
    y_coord = int(input("geef de y-coordinaat : "))
    punt_2 = Point(x_coord, y_coord)

    return punt_1, punt_2

# punt_1, punt_2 = get_tuple_points_from_user()
# calculate_slope(punt_1, punt_2)

punt_1, punt_2 = get_obj_points_from_user()
calculate_slope(punt_1, punt_2)