//Maze solver - Daniel Charua A01017419 - Mauricio Rico
#include <iostream>
#include <string>
using namespace std;

class Maze{
public:
  int row;
  int col;
  int *maze;
  int start[2];
  int end[2];
  string path;
  string finalPath;
  //Contructor destructor
  Maze(){ path = ""; finalPath = "";}
  ~Maze(){delete(maze);}

  //function to read file
  void readFile(){
    string  line;
    //Read rows and cols
    cin >> line;
    col = stoi(line);
    cin >> line;
    row = stoi(line);
    maze = (int *) malloc(col * row * sizeof(int));
    //Read start point
    cin >> line;
    start[0] = stoi(line);
    cin >> line;
    start[1] = stoi(line);
    //Read end point
    cin >> line;
    end[0] = stoi(line);
    cin >> line;
    end[1] = stoi(line);
    //Read start maze
    for (int i=0; i < row; i++){
      cin >> line;
      for (int j=0; j< row; j++){
        maze[j + ((row-i-1) * row)] =line[j] -'0';
      }
    }
    solveMaze(start[0], start[1]);
  }

  //function to print maze with path for debugging
  void printMaze(){
    printPath();
    for (int i = 0; i < row; i++){
      for (int j = 0; j <col; j++){
        cout<< maze[j + (i * row)];
      }
      cout<<endl;
    }
  }

  //function used recursivly to solve maze
  bool solveMaze(int c, int r){
    if (c == end[0] && r == end[1]){
        return true;
      }
    else if( maze[c + (r * row)] == 1)
        return false;
    else if(maze[c + (r * row)] == 2)
        return false;
    maze[c + (r * row)] = 2;

    if (c < col-1 && solveMaze(c+1, r)){
        path.append("R");
        return true;
      }
    else if(r > 0 && solveMaze(c, r-1)){
        path.append("D");
        return true;
      }
    else if(c > 0 && solveMaze(c-1, r)){
        path.append("L");
        return true;
      }
    else if(r <row -1  && solveMaze(c, r+1)){
        path.append("U");
        return true;
      }
    return false;
  }

  //function to print path
  void printPath(){
    int size = path.length();
    for (int i = size; i >= 0; i--)
      finalPath+=path[i];
    cout<< finalPath;
  }
};

int main(){
  Maze * m = new Maze();
  m->readFile();
  m->printPath();
  delete m;
  return 0;
}
