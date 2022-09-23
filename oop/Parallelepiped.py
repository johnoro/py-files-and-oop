from .Rectangle import Rectangle

class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def get_volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()
        print("Height: ", self.height)
        print("Volume: ", self.get_volume())
