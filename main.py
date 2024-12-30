from gui import Window, Point, Line, Cell
from maze import Maze

def main():
    win = Window(800, 600)

    test = Maze(10,10,5,7,50,50, win)
    test._break_entrance_and_exit()
    print(test._cells[0][0].has_top_wall)
    print(test._cells[-1][-1].has_bottom_wall)

    
    win.wait_for_close()


if __name__ == "__main__":
    main()