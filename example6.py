from math import pi
import random


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)

    def info(self):
        return f"Radius - {self.radius}, Area - {self.area()}, Length - {self.length()}"


def circle_creator(n):
    result = []
    for i in range(n):
        tmp = Circle(random.randint(0, 10000))
        result.append(tmp)
    return result


if __name__ == '__main__':
    my_circles = circle_creator(100)
    # for circle in my_circles:
    #     print(circle.info())

    max_circle = my_circles[0]
    for circle in my_circles[1:]:
        if circle.area() > max_circle.area():
            max_circle = circle

    print(max_circle.info())

    max_circle_length = max(my_circles, key=lambda c: c.length())

    print("Legth: ", max_circle_length.info())

    max_circle_radius = max(my_circles, key=lambda c: c.radius)
    print("radius: ", max_circle_radius.info())

