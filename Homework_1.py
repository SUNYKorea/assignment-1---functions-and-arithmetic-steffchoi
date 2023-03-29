# Name: Stephanie Choi
# SBUID: 115343881

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius 

def what_to_wear(celsius):
    if celsius < -10:
        clothing = 'puffy jacket'
    elif -10 <= celsius < 0:
        clothing = 'scarf'
    elif 0 <= celsius < 10:
        clothing = 'sweater'
    elif 10 <= celsius < 20:
        clothing = 'light jacket'
    elif 20 <= celsius:
        clothing = 't-shirt'
    return clothing

celsius = fahrenheit2celsius(float(input('Enter temperature in fahrenheit: ')))
print('The temperature today is ' + '{:.1f}'.format(celsius) + ' degrees celsius, so you should wear a ' + what_to_wear(celsius))

# This function will be fruitful becuase it returns a value(the type of clothing)


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x1 * y3) + (x2 * y1) + (x3 * y2)))/ 2)
    return area

x1 = float(input('Enter the x coordinate of vertex 1: '))
y1 = float(input('Enter the y coordinate of vertex 1: '))
x2 = float(input('Enter the x coordinate of vertex 2: '))
y2 = float(input('Enter the y coordinate of vertex 2: '))
x3 = float(input('Enter the x coordinate of vertex 2: '))
y3 = float(input('Enter the y coordinate of vertex 2: '))

print('The area of the triangle is ' + '{:.2f}'.format(shoelace_triangle_area(x1, y1, x2, y2, x3, y3)))

def euclidean_distance(x1, y1, x2, y2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    perimeter = euclidean_distance(x1, y1, x2, y2) + euclidean_distance(x1, y1, x3, y3) + euclidean_distance(x2, y2, x3, y3)
    return perimeter

print('The perimeter of the triangle is ' + '{:.2f}'.format(compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)))


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


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

