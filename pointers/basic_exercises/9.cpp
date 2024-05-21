#include <iostream>

using namespace std;

/*
Escreva uma função que dado um número real passado como parâmetro, retorne à parte inteira e a parte
fracionaria deste número. Escreva um programa que chama a função Prototipo: void frac(float num, int*
inteiro, float* frac);
*/

void frac(float num, int *inteiro, float *frac) {

  *inteiro = (int)num;
  *frac = num - *inteiro;

  cout<<"Parte inteira: "<<*inteiro<<"\nParte Frac: "<<*frac<<endl;
}

int main() {
  float num, fracionario;
  int inteiro;
  
  cin>>num;

  frac(num, &inteiro, &fracionario);
  
  return 0;
}
