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

