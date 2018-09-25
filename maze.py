import numpy as np
class Maze:
    def __init__(self, filename):
        tmp = []
        lines = list(open(filename))
        a, b = lines[0].rstrip().split(' ')
        self.col = int(a)
        self.row =  int(b)
        a, b = lines[1].rstrip().split(' ')
        self.start_point = int(a), int(b)
        a, b = lines[2].rstrip().split(' ')
        self.end_point = int(a), int(b)
        for line in reversed(lines[3:]):
            tmp.append(list(map(int, line.rstrip())))
        self.maze = np.array(tmp)
        self.solve(self.start_point)
        c, r = self.start_point
        self.maze[r][c] = 3
        c, r = self.end_point
        self.maze[r][c] = 4
        self.printMaze()

    def printMaze(self):
        print('\nCol: %d, Rows: %d' % (self.col, self.row))
        print('start_point: %s marked with 3' % (self.start_point,))
        print('end_point: %s marked with 4' % (self.end_point,))
        print (self.maze)

    def solve(self, coordinates):
        c, r = coordinates
        if coordinates == self.end_point:
            print("Maze solved")
            print(coordinates)
            return True
        elif self.maze[r][c] == 1:
            print ('wall at %d,%d' % (c, r))
            return False
        elif self.maze[r][c] == 2:
            print ('visited at %d,%d' % (c, r))
            return False
        print ('visiting %d,%d' % (c, r))
        self.maze[r][c] = 2

        if ((c < self.col-1 and self.solve((c+1, r)))
            or (r > 0 and self.solve((c, r-1)))
            or (c > 0 and self.solve((c-1, r)))
            or (r < self.row-1 and self.solve((c, r+1)))):
            return True
        return False



if __name__ == "__main__":
    maze = Maze("maze1.txt")
