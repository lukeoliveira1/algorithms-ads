#include <iostream>

using namespace std;

int main()
{
    float matriz[3][3];
    
    for(int i=0; i < 3; i++) {
        for(int j=0; j < 3; j++) {
        cout<<&matriz[i][j] << "\n";
        }
    }

    return 0;
}
