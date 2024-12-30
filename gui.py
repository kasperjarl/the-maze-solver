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

class Cell:
    def __init__(self, top_left_corner, bottom_right_corner, _win, has_left_wall=True, 
                 has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = top_left_corner.x
        self._x2 = bottom_right_corner.x
        self._y1 = top_left_corner.y
        self._y2 = bottom_right_corner.y
        self._win = _win

    def draw(self, cell, fill_color="blue"):
        if cell.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            left_wall.draw(self._win.canvas, fill_color)
        elif not cell.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            left_wall.draw(self._win.canvas, "white")
        if cell.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            bottom_wall.draw(self._win.canvas, fill_color)
        elif not cell.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            bottom_wall.draw(self._win.canvas, "white")   
        if cell.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            right_wall.draw(self._win.canvas, fill_color)
        elif not cell.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            right_wall.draw(self._win.canvas, "white")
        if cell.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            top_wall.draw(self._win.canvas, fill_color)
        elif not cell.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            top_wall.draw(self._win.canvas, "white")

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"

        from_center_point = Point(((self._x1 + self._x2) / 2), ((self._y1 + self._y2) / 2))
        to_center_point = Point(((to_cell._x1 + to_cell._x2) / 2), ((to_cell._y1 + to_cell._y2) / 2))

        from_to_line = Line(from_center_point, to_center_point)
        from_to_line.draw(self._win.canvas, line_color)