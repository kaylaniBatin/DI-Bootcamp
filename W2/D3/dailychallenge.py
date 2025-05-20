import math

class Circle:
    def __init__(self, *, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Must provide either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(Radius: {self.radius:.2f}, Diameter: {self.diameter:.2f}, Area: {self.area():.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented


# Example usage:
if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=12)
    c3 = Circle(radius=3)

    print(c1)
    print(c2)

    c4 = c1 + c3
    print("After adding c1 and c3:", c4)

    print("Is c1 > c2?", c1 > c2)
    print("Is c1 == c3?", c1 == c3)

    circles = [c1, c2, c3, c4]
    circles.sort()
    print("\nSorted Circles:")
    for c in circles:
        print(c)

    # Bonus: Turtle drawing of sorted circles
    try:
        import turtle

        screen = turtle.Screen()
        screen.title("Sorted Circles")
        t = turtle.Turtle()
        t.penup()
        t.speed(0)

        start_x = -200
        for c in circles:
            t.goto(start_x + c.radius, 0)
            t.pendown()
            t.circle(c.radius)
            t.penup()
            start_x += c.diameter + 10  # spacing

        screen.mainloop()
    except ImportError:
        print("Turtle module not available.")