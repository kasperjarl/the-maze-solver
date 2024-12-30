from gui import Window, Point, Line
from maze_graphics import Cell

def main():
    win = Window(800, 600)

    # cells
    cell_1 = Cell(Point(10,10), Point(50, 50), win)
    cell_2 = Cell(Point(60, 10), Point(100, 50), win, has_left_wall=False)
    cell_3 = Cell(Point(110, 10), Point(150, 50), win, has_bottom_wall=False)
    cell_4 = Cell(Point(160, 10), Point(200, 50), win, has_right_wall=False)
    cell_5 = Cell(Point(210, 10), Point(250, 50), win, has_top_wall=False)
    cell_6 = Cell(Point(260, 10), Point(300, 50), win, 
                  has_bottom_wall=False, has_right_wall=False,
                  has_left_wall=False, has_top_wall=False)

    # drawing
    win.draw_cell(cell_1)
    win.draw_cell(cell_2)
    win.draw_cell(cell_3) 
    win.draw_cell(cell_4) 
    win.draw_cell(cell_5) 
    win.draw_cell(cell_6) 


    win.wait_for_close()


if __name__ == "__main__":
    main()