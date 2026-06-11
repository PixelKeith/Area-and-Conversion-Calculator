import math

def area_square(side):
    return side ** 2

def area_parallelogram(base, height):
    return base * height

def area_rectangle(length, width):
    return length * width

def area_trapezoid(base1, base2, height ):
    return (base1 + base2) * height / 2

def area_triangle(base, height):
    return (base * height) / 2

def area_circle(radius):
    return math.pi * (radius ** 2)