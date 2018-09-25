import numpy as np

class Maze:
    def __init__(self, filename):
        self.path = ""
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
        self.solve(self.start_point, self.path)
        #self.printMaze()


    def printMaze(self):
        c, r = self.start_point
        self.maze[r][c] = 3
        c, r = self.end_point
        self.maze[r][c] = 4
        print('\nCol: %d, Rows: %d' % (self.col, self.row))
        print('start_point: %s marked with 3' % (self.start_point,))
        print('end_point: %s marked with 4' % (self.end_point,))
        print('Path taken: %s ' % (self.path[::-1]))
        print (self.maze)

    def solve(self, coordinates, path):
        c, r = coordinates
        if coordinates == self.end_point:
            return True
        elif self.maze[r][c] == 1:
            return False
        elif self.maze[r][c] == 2:
            return False
        self.maze[r][c] = 2

        if (c < self.col-1 and self.solve((c+1, r), self.path)):
            self.path +="R"
            return True
        elif (r > 0 and self.solve((c, r-1), self.path)):
            self.path +="D"
            return True
        elif (c > 0 and self.solve((c-1, r), self.path)):
            self.path +="L"
            return True
        elif(r < self.row-1 and self.solve((c, r+1), self.path)):
            self.path +="U"
            return True
        return False

    def getPath(self):
        return self.path[::-1]

if __name__ == "__main__":
    maze = Maze(input())
    print( maze.getPath())
