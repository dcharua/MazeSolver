# Maze Solver - Daniel Charua & Mauricio Rico - 26/09/18
import numpy as np
import sys
# Expanding python's default recursion limit
sys.setrecursionlimit(999999)

class Maze:
    #constructor with file read from input
    def __init__(self):
        self.path = ""
        tmp = []
        #Reading col & row size
        a, b = input().rstrip().split(' ')
        self.col = int(a)
        self.row =  int(b)
        #Reading Start and End point
        a, b = input().rstrip().split(' ')
        self.start_point = int(a), int(b)
        a, b = input().rstrip().split(' ')
        self.end_point = int(a), int(b)
        #Reading maze
        for i in range(self.row):
            tmp.append(list(map(int, input().rstrip())))
        #passing inverted maze to np arry
        self.maze = np.array(tmp[::-1])
        self.solve(self.start_point, self.path)
        #self.printMaze()

    #Function to print maze for debugging
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

    #Recursive funcion to solve maze
    def solve(self, coordinates, path):
        c, r = coordinates
        #Base case, end point found,
        if coordinates == self.end_point:
            return True
        #otherwise if its a wall or visited  return False
        elif self.maze[r][c] == 1:
            return False
        elif self.maze[r][c] == 2:
            return False
        #setting visited
        self.maze[r][c] = 2

        #Exploring first to the right if its possible than down, left and up in that order
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

    #function to get path inverted to match actual path taken
    def getPath(self):
        return self.path[::-1]

if __name__ == "__main__":
    maze = Maze()
    print( maze.getPath())
