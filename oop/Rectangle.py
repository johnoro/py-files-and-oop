class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def display(self):
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Perimeter: ", self.get_perimeter())
        print("Area: ", self.get_area())
