#include <iostream>

using namespace std;


int two(int *ptrA, int *ptrB) {
    int soma = *ptrA + *ptrB;
    *ptrA = soma;
    return *ptrA;
}

int main()
{
    int a = 5;
    int b = 2;
    cout<<two(&a, &b);

    return 0;
}