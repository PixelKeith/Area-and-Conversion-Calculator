import math

def display_area(area):
    print(f"\nThe area is: {area}\n")

def area_square():
    side = float(input("\nEnter side: "))
    area = side ** 2

    display_area(area)

def area_parallelogram():
    base = float(input("\nEnter base: "))
    height = float(input("\nEnter height: "))
    area = base * height

    display_area(area)

def area_rectangle():
    length = float(input("\nEnter length: "))
    width = float(input("\nEnter width: "))
    area = length * width

    display_area(area)

def area_trapezoid():
    a = float(input("\nEnter a: \n"))
    b = float(input("\nEnter b: \n"))
    height = float(input("\nEnter height: "))
    area = (a + b) * height / 2

    display_area(area)

def area_triangle():
    base = float(input("\nEnter base: "))
    height = float(input("\nEnter height: "))
    area = (base * height) / 2

    display_area(area)

def area_circle():
    radius = float(input("\nEnter radius: "))
    area = math.pi * radius ** 2

    display_area(area)