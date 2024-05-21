#include <iostream>

using namespace std;

int main()
{
    int arr[10];     /* arr: arranjo com 10 inteiros */
    int *ptr;         /* el:  ponteiro para um inteiro */
    int i;
    int x;
      
    ptr = &arr[0];  /* inicializa ponteiro */
      
    /* preenchendo conteúdo do arranjo via ponteiro */
    for (i=0; i<10; ++i) {
        cin>>x;
        *(ptr + i) = x; //ponteiro vai avançando de posição no vetor
    }
    
    for (i=0; i<10; ++i) {
        if(arr[i] % 2 == 0) {
            cout<<&arr[i]<<endl;
        }
    }
    return 0;
    
}
