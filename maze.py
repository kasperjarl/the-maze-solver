from gui import Window, Point, Line, Cell
from time import sleep
import random


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed=None):
        self._cells = []
        if seed:
            self._seed = random.seed(seed)
        self.x1 = x1 # represents how many pixels from the left the maze should start
        self.y1 = y1 # represents how many pixels from the top the maze should start
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x # width
        self.cell_sizy_y = cell_size_y # height 
        self.win = win
        
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            a = []
            for j in range(self.num_rows):
                a.append(Cell(Point(0,0), Point(0,0), self.win))
            self._cells.append(a)
        self._draw_cell(self.num_cols, self.num_rows)

    def _draw_cell(self, i, j):
        starting_x = self.x1 # top left corner
        end_x = self.x1 + self.cell_size_x # bottom right corner

        for i in range(self.num_cols):
            starting_y = self.y1
            end_y = self.y1 + self.cell_sizy_y
            for j in range(self.num_rows):
                self._cells[i][j]._x1 = starting_x
                self._cells[i][j]._x2 = end_x
                self._cells[i][j]._y1 = starting_y
                self._cells[i][j]._y2 = end_y
                self._cells[i][j].draw(self._cells[i][j])
                self._animate()
                starting_y += self.cell_sizy_y
                end_y += self.cell_sizy_y
            starting_x += self.cell_size_x
            end_x += self.cell_size_x

        self._animate()


    def _animate(self):
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        cell_entrance = self._cells[0][0]
        cell_entrance.has_top_wall = False
        self._draw_cell(self.num_cols, self.num_rows)
        cell_exit = self._cells[-1][-1]
        cell_exit.has_bottom_wall = False
        self._draw_cell(self.num_cols, self.num_rows)
        

        
        
                

