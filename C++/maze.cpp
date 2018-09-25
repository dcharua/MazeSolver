#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

class Maze{
public:
  int width;
  int height;
  int *maze = new int[width*height];
  int start[2];
  int end[2];
  // Maze(int w, int h){
  //   width = w;
  //   height = m;
  // }
  void readFile(string filename){
    int counter = 0, j = 0;
    ifstream file(filename);
    string line;
    if (file.is_open()) {
      while (getline(file , line )){
        if (counter > 2){
          for (int i=0; i < line.length(); i++){
            cout <<line[i] - '0'<<endl;
            maze[j*width + i] = line[i] - '0';
          }
          j++;
        }
        if (counter == 0){
          istringstream ss(line);
          string token;
          getline(ss,token,' ');
          width = stoi(token);
          getline(ss,token,' ');
          height = stoi(token);
        }
        if (counter == 1){
          istringstream ss(line);
          string token;
          getline(ss,token,' ');
          start[0] = stoi(token);
          getline(ss,token,' ');
          start[1] = stoi(token);
        }
        if (counter == 2){
          istringstream ss(line);
          string token;
          getline(ss,token,' ');
          end[0] = stoi(token);
          getline(ss,token,' ');
          end[1] = stoi(token);
        }
        counter++;
      }
    }
  }

  //ary[y*sizeX + x]
  ~Maze(){delete(maze);}
};

int main(){
  Maze * m = new Maze();
  m->readFile("maze1.txt");
}
