from tkinter import Tk, Canvas, BOTH
from random import randrange as rnd


class Snake:
    """docstring"""

    def __init__(self, start_length, coords):
        """Constructor"""

        # длина змеи
        self.length = start_length

        # координаты положения головы змеи
        self.x = coords[0]
        self.y = coords[1]

    # метод увеличения длины змеи
    def length_grow(self):
        """Snake grows!"""
        return self.length+1

    # движение влево
    def go_left(self):
        """Go to the Left!"""
        return self.x-1

    # движение вправо
    def go_right(self):
        """Go to the Right!"""
        return self.x+1

    # движение вверх
    def go_up(self):
        """Go Up!"""
        return self.y-1

    # движение вниз
    def go_down(self):
        """Go Down!"""
        return self.y+1


class Map:
    """docstring"""

    def __init__(self, canvas, size):
        """Constructor"""

        # размер сетки
        self.length = size[0]
        self.width = size[1]

        # начало построения сетки
        self.x_start = 50
        self.y_start = 20

        # размер квадратов сетки
        self.rectangle_size = 20

        self.canvas = canvas

    def paint(self):

        # отрисовка сетки
        for i in range(self.length):
            for j in range(self.width):
                self.canvas.create_rectangle(self.x_start + self.rectangle_size * i,
                                             self.y_start + self.rectangle_size * j,
                                             self.x_start + self.rectangle_size * (i + 1),
                                             self.y_start + self.rectangle_size * (j + 1),
                                             outline="black", fill=None)

    def new_bonus(self):
        coord_x = rnd(self.length)
        coord_y = rnd(self.width)
        self.canvas.create_rectangle(self.x_start + self.rectangle_size * coord_x,
                                     self.y_start + self.rectangle_size * coord_y,
                                     self.x_start + self.rectangle_size * (coord_x + 1),
                                     self.y_start + self.rectangle_size * (coord_y + 1),
                                     outline="black", fill="green")


def main():
    start_coords = [20, 20]
    map_size = [20, 20]

    root = Tk()
    root.title("Snake")
    root.geometry("500x500")

    canvas = Canvas(root)

    map = Map(canvas, map_size)
    map.new_bonus()

    snake = Snake(start_length=2, coords=start_coords)

    map.paint()

    canvas.pack(fill=BOTH, expand=1)
    root.mainloop()


if __name__ == '__main__':
    main()