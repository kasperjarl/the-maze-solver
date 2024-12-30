from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.canvas = Canvas(master=self.__root)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x # horizontial 
        self.y = y # vertical 

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.x1 = self.point_1.x
        self.y1 = self.point_1.y
        self.x2 = self.point_2.x
        self.y2 = self.point_2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2
        )

