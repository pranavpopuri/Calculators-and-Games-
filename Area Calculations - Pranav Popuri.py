import math

z = input("Do for what shape do you want to find the area? Your choices are square, rectangle, triangle, circle, regular pentagon, regular hexagon, and trapezoid")

#Square

if z == ("square"):
    def areaS(s):

        return s*s

    print(areaS(float(input("Choose the side length for the square"))))
    print("square complete")

#Rectangle

if z == ("rectangle"):
    def areaR(w, l):

        return w*l

    print(areaR(float(input("Choose the length for the rectangle")), float(input("Choose the width for the rectangle"))))

#Triangle

if z == ("triangle"):
    def areaT(b, h):

        return 0.5 * b * h

    print(areaT(float(input("Choose the base for the triangle")), float(input("Choose the height for the triangle"))))

#Circle

if z == ("circle"):
    def areaC(r):

        return math.pi * r**2

    print(areaC(float(input("Choose a radius for the circle"))))

#RegularPentagon

if z == ("regular pentagon"):
    def areaP(p):

        return 0.25* math.sqrt(5*(5+math.sqrt(20))) * p**2

    print(areaP(float(input("Choose a side length for the regular pentagon"))))

#RegularHexagon

if z == ("regular hexagon"):
    def areaH(h):

        return 3 * math.sqrt(3)/2 * h**2

    print(areaH(float(input("Choose a side length for the regular hexagon"))))

#Trapezoid

if z == ("trapezoid"):
    def areaTr(a, b, h):

        return (a+b)/2 * h

    print(areaTr(float(input("Choose a length for the top base of the trapezoid")) , float(input("Choose a length for the bottom base of the trapezoid")), float(input("Choose a length for the height of the trapezoid"))))


