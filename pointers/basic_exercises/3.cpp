#include <iostream>

using namespace std;

int main()
{
    float array[10];
    
    for(int i=0; i < 10; i++) {
        cout<<&array[i] << "\n";
    }

    return 0;
}
