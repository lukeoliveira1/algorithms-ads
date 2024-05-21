#include <iostream>

#include <ctime>
#include <cstdlib>

using namespace std;

int negativos(float *vet, int N) {
    int n=0;
    
    for(int i=0; i<N;i++) {
       cout<<vet[i]<<" ";
    }
    
    cout<<endl;
    
    for(int i=0; i<N;i++) {
        if (vet[i] < 0) {
            cout<<vet[i];
            n++;
        }
    }
    
    cout<<endl;
    
    return n;
}

int main()
{
   float arr[10];
   
   srand((unsigned(time(0))));

   for(int i=0; i< 10;i++) {
       int aleatorio=rand()%(5-(-5)+1)-5;
	   arr[i]=aleatorio;
   }
   
   
//   float *ptr;
//   ptr = &arr[0];
   
   cout<<negativos(arr, 10);
   return 0;
    
}
