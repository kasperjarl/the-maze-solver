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


    def _animate(self):
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        cell_entrance = self._cells[0][0]
        cell_entrance.has_top_wall = False 
        # self._cells[0][0].draw(self._cells[0][0])
        self._draw_cell(self.num_cols, self.num_rows)
        cell_exit = self._cells[-1][-1]
        cell_exit.has_bottom_wall = False
        # self._cells[0][0].draw(self._cells[-1][-1])
        self._draw_cell(self.num_cols, self.num_rows)

    def is_valid_cell(self, i, j):
        return (0 <= i < self.num_cols and
                0 <= j < self.num_rows)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            # above_cell
            if self.is_valid_cell(i, j - 1) and not self._cells[i][j - 1].visited:
                    to_visit.append(self._cells[i][j - 1])
            # left_cell
            if self.is_valid_cell(i - 1, j) and not self._cells[i - 1][j].visited:
                    to_visit.append(self._cells[i - 1][j])
            # under_cell
            if self.is_valid_cell(i, j + 1) and not self._cells[i][j + 1].visited:
                    to_visit.append(self._cells[i][j + 1]) 
            # right_cell
            if self.is_valid_cell(i + 1, j) and not self._cells[i + 1][j].visited:
                    to_visit.append(self._cells[i + 1][j])
    
            # if zero directions from current cell
            if not to_visit:
                 self._cells[i][j].draw(self._cells[i][j])
                 return
            
            random_choice = random.choice(to_visit)
            if (
                 (self._cells[i][j]._x1, self._cells[i][j]._y1) ==
                 (random_choice._x1, random_choice._y2)
                ):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j].draw(self._cells[i][j])
                self._break_walls_r(i, j - 1)
            # Left Wall break down
            if (
                 (self._cells[i][j]._x1, self._cells[i][j]._y1) ==
                 (random_choice._x2, random_choice._y1)
            ):
                self._cells[i][j].has_left_wall = False
                self._cells[i][j].draw(self._cells[i][j])
                self._break_walls_r(i - 1, j)

            # Bottom wall break down
            if (
                 (self._cells[i][j]._x2, self._cells[i][j]._y2) ==
                 (random_choice._x2, random_choice._y1)
            ):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j].draw(self._cells[i][j])
                self._break_walls_r(i, j + 1)
            
            # Right wall break dwon
            if (
                 (self._cells[i][j]._x2, self._cells[i][j]._y2) ==
                 (random_choice._x1, random_choice._y2)
            ):
                self._cells[i][j].has_right_wall = False
                self._cells[i][j].draw(self._cells[i][j])
                self._break_walls_r(i + 1, j)
            
    def _reset_cells_visited(self):
         i = 0
         j = 0
         for list in self._cells:
              for cell in list:
                #    print(f"cell[{i}][{j}] | top_wall: {cell.has_top_wall} left_wall: {cell.has_left_wall}, bottom_wall: {cell.has_bottom_wall}, right_wall: {cell.has_right_wall}")
                   cell.visited = False
                   j += 1
              i += 1

    def solve(self):
         return self._solve_r(i=0, j=0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
         
         # if at the end cell:
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
         

         ### I think it's something like the below, where we need to add if there is a wall.
         ### We also need to figure out the "for each direction" par
        directions = []

        # above_cell
        if self.is_valid_cell(i, j - 1) and not self._cells[i][j - 1].visited and self._cells[i][j].has_top_wall == False:
            directions.append(self._cells[i][j - 1])
        # left_cell
        if self.is_valid_cell(i - 1, j) and not self._cells[i - 1][j].visited and self._cells[i][j].has_left_wall == False:
            directions.append(self._cells[i - 1][j])
        # under_cell
        if self.is_valid_cell(i, j + 1) and not self._cells[i][j + 1].visited and self._cells[i][j].has_bottom_wall == False:
            directions.append(self._cells[i][j + 1]) 
        # right_cell
        if self.is_valid_cell(i + 1, j) and not self._cells[i + 1][j].visited and self._cells[i][j].has_right_wall == False:
            directions.append(self._cells[i + 1][j])

        for random_choice in directions:
            self._cells[i][j].draw_move(random_choice)

            if (
                 (self._cells[i][j]._x1, self._cells[i][j]._y1) ==
                 (random_choice._x1, random_choice._y2)
                ):
                
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(random_choice, undo=True)
            # Left Wall break down
            if (
                 (self._cells[i][j]._x1, self._cells[i][j]._y1) ==
                 (random_choice._x2, random_choice._y1)
            ):
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(random_choice, undo=True)

            # Bottom wall break down
            if (
                 (self._cells[i][j]._x2, self._cells[i][j]._y2) ==
                 (random_choice._x2, random_choice._y1)
            ):
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(random_choice, undo=True)
            
            # Right wall break dwon
            if (
                 (self._cells[i][j]._x2, self._cells[i][j]._y2) ==
                 (random_choice._x1, random_choice._y2)
            ):
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(random_choice, undo=True)
        return False



            