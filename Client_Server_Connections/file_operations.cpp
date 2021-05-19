#include <iostream> 
#include <fstream>
#include <stdio.h>

using namespace std;

int main()
{
    ifstream fout;
    fout.open("test.txt");
    string line; 
    while (fout) {
        getline(fout, line);
        cout << line << endl;
    }

    fout.close();

    return 0;
}