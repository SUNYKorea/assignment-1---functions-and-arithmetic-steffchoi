# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    radian = deg * math.pi / 180
    return radian

number_sides = int(input('Input the number of sides: '))
length_side = float(input('Input the length of a side: '))

def apothem(number_sides, length_side):
    apothem = length_side / (2 * math.tan(deg2rad(180 / number_sides)))
    return apothem

def polygon_area(number_sides, length_side):
    area = number_sides * length_side * apothem(number_sides, length_side) * (1/2)
    return area

print('The area of the polygon is ' + '{:.2f}'.format(polygon_area(number_sides, length_side)))
