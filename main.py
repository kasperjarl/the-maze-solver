from gui import Window, Point, Line, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # test_cell = Cell(Point(0,0), Point(0,0), win)
    # # test_cell.visited = False
    # print(test_cell.visited)

    test = Maze(10, 10, 10, 14, 25, 25, win)
    test._break_entrance_and_exit()
    test._break_walls_r(0,0)
    test._reset_cells_visited()
    test.solve()
    print("done")
    
    win.wait_for_close()



if __name__ == "__main__":
    main()

