#include <iostream>

using namespace std;

void one() {
    int a = 2;
    float b = 2.5;
    char c = 'c';
    
    cout<<a<<endl;
    cout<<b<<endl;
    cout<<c<<endl;
    
    int *ptrInt;
    float *ptrFloat;
    char *ptrChar;
    
    //ponteiros recebendo endereço dos valores das variáveis 
    ptrInt = &a;
    ptrFloat = &b;
    ptrChar = &c;
    
    //alterando valores das variáveis com ponteiros
    *ptrInt = 1;
    *ptrFloat = 1.5;
    *ptrChar = 'd';
    
    cout<<a<<endl;
    cout<<b<<endl;
    cout<<c<<endl;
}

int main()
{
    one();
    return 0;
}
