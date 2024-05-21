#include <ctime>
#include <iostream>
#include <stdlib.h>

using namespace std;

/*
Faça um programa que leia a quantidade de elementos n e crie dinamicamente um
vetor de n elementos e passe esse vetor para uma função que irá ler os elementos
desse vetor. Depois, no programa principal, o vetor preenchido deve ser
impresso.
*/

void preencherVetor(int *vet, int qntd) {

  srand(unsigned(time(0)));
  int aleatorio;

  for (int i = 0; i < qntd; i++) {
    aleatorio = rand() % (20 - 10 + 1) + 10;
    vet[i] = aleatorio;
  }
}

void mostrarVetor(int *vet, int n) {
  int i;

  for (i = 0; i < n; i++) {
    cout << *(vet + i) << " ";
  }
}

int main() {
  int qntd;
  cin >> qntd;

  int *vet = new int(qntd * sizeof(int));

  preencherVetor(vet, qntd);
  mostrarVetor(vet, qntd);
  return 0;
}
