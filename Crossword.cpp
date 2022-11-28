#include <iostream> 
#include <fstream> 
#include <set>
#include <string>
#include <vector>
#include <stdlib.h>
#include "color.hpp"

using std::string;
using std::cout;
using std::vector;
using std::set;
using std::pair;
using std::ifstream;

set<string> words; 

int n;
int m; 
char grid[1000][1000];
bool visited[1000][1000];
int wordsFound = 0;


enum DirectionEnum{
    up,
    down,
    left,
    right,
    up_right,
    up_left,
    down_right,
    down_left
};

string reverse(string s){
    string temp = "";
    for(int i = s.size() - 1; i >= 0;i--){
        temp+=s[i];
    }
    return temp;
}

void dfs(int r, int c,string current,vector<pair<int,int> > coordinates, DirectionEnum direction){
    if(r > n || r < 0 || c > n || c < 0){
        return;
    }
    current+=grid[r][c];
    coordinates.push_back(std::make_pair(r,c));
    if(words.count(current) == 1 || words.count(reverse(current)) == 1){
        for(int i = 0; i < coordinates.size();i++){
            visited[coordinates[i].first][coordinates[i].second] = 1;
        }
        wordsFound++;
        return;
    }
    switch(direction){
        case up:
            dfs(r-1,c,current,coordinates,direction);
            break;
        case down:
            dfs(r+1,c,current,coordinates,direction);
            break;
        case left:
            dfs(r,c-1,current,coordinates,direction);
            break;
        case right:
            dfs(r,c+1,current,coordinates,direction);
            break;
        case up_right:
            dfs(r-1,c+1,current,coordinates,direction);
            break;
        case up_left:
            dfs(r-1,c-1,current,coordinates,direction);
            break;
        case down_left:
            dfs(r+1,c-1,current,coordinates,direction);
            break;
        case down_right:
            dfs(r+1,c+1,current,coordinates,direction);
            break;
    }

}





int main(){
    ifstream input("Crossoword.txt");
    input >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n;j++){
            input >> grid[i][j];
        }
    }
    input >> m; 
    for(int i = 0; i < m; i++){
        string s; 
        input >> s; 
        words.insert(s);
    }
    for(int i = 0; i < n; i++) for(int j = 0; j < n;j++){
        vector<pair<int,int> > coordinates; 
        dfs(i,j,"",coordinates,DirectionEnum::up);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::down);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::left);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::right);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::up_left);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::up_right);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::down_left);
        coordinates.clear();
        dfs(i,j,"",coordinates,DirectionEnum::down_right);
        coordinates.clear();
    }
    cout << "I found " << wordsFound/2 << " words!" << std::endl;
    cout << std::endl;cout << std::endl;
    cout << std::endl;cout << std::endl;
    cout << std::endl;cout << std::endl;
    for(int i = 0; i < n; i++){ 
        for(int j = 0; j < n; j++){
            if(visited[i][j]){
                cout << dye::red(grid[i][j]) << "  ";
            }else{
                cout << dye::white(grid[i][j]) << "  ";
            }
        }
        cout << std::endl;
    }
    cout << std::endl;
    cout << std::endl;
    cout << std::endl;
    cout << std::endl;
    for(int i = 0; i < n; i++){ 
        for(int j = 0; j < n; j++){
            if(visited[i][j]){
                cout << dye::red(grid[i][j]) << "  ";
            }else{
                cout << dye::white("*") << "  ";
            }
        }
        cout << std::endl;
    }




    return 0;
}