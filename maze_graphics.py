from gui import Window, Point, Line

class Cell:
    def __init__(self, top_left_corner, bottom_right_corner, _win, has_left_wall=True, has_right_wall=True,
                 has_top_wall=True, has_bottom_wall=True):
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
        if cell.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            bottom_wall.draw(self._win.canvas, fill_color)
        if cell.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            right_wall.draw(self._win.canvas, fill_color)
        if cell.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            top_wall.draw(self._win.canvas, fill_color)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"

        from_center_point = Point(((self._x1 + self._x2) / 2), ((self._y1 + self._y2) / 2))
        to_center_point = Point(((to_cell._x1 + to_cell._x2) / 2), ((to_cell._y1 + to_cell._y2) / 2))

        from_to_line = Line(from_center_point, to_center_point)
        from_to_line.draw(self._win.canvas, line_color)

        