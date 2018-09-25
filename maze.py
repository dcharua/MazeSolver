import numpy as np
class Maze:
    def __init__(self, filename):
        tmp = []
        lines = list(open(filename))
        a, b = lines[1].rstrip().split(' ')
        self.start_point = int(a), int(b)
        a, b = lines[2].rstrip().split(' ')
        self.end_point = int(a), int(b)
        for line in reversed(lines[3:]):
            tmp.append(list(map(int, line.rstrip())))
        self.maze = np.array(tmp)
        self.solve(self.start_point)

    def printMaze(self):
        print (self.maze)
        
    def solve(self, coordinates):
        x, y = coordinates
        if coordinates == self.end_point:
            print("Maze solved")
            print(coordinates)
            return True
        elif self.maze[x][y] == 1:
            print ('wall at %d,%d' % (x, y))
            return False
        elif self.maze[x][y] == 2:
            print ('visited at %d,%d' % (x, y))
            return False
        print ('visiting %d,%d' % (x, y))
        self.maze[x][y] = 2

        if ((x < len(self.maze)-1 and self.solve((x+1, y)))
            or (y > 0 and self.solve((x, y-1)))
            or (x > 0 and self.solve((x-1, y)))
            or (y < len(self.maze)-1 and self.solve((x, y+1)))):
            return True
        return False



if __name__ == "__main__":
    maze = Maze("maze1.txt")
    maze.printMaze()
