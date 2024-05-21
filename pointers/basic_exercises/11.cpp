#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

/*
Escreva uma função que receba um array de inteiros V e os endereços de duas
variáveis inteiras, min e max, e armazene nessas variáveis o valor mínimo e
máximo do array. Escreva também uma função ao main que use essa função.
*/

const int MAX = 20000000;

void minMax(int vetor[], int *min, int *max) {
  int menor = MAX, maior = 0;

  for (int i = 0; i < 10; i++) {
    if (vetor[i] < menor) {
      menor = vetor[i];
    }
    if (vetor[i] > maior) {
      maior = vetor[i];
    }
  }

  *max = maior;
  *min = menor;
  cout << "teste Maior: " << maior << endl;
  cout << "teste Menor: " << menor << endl;
  cout << "Maior: " << *max << endl;
  cout << "Menor: " << *min << endl;
}

int main() {
  int v[10];
  int max = 0, min = 0;
  int aleatorio;

  srand(unsigned(time(0)));

  for (int i = 0; i < 10; i++) {
    aleatorio = rand() % (20 - 1 + 1) + 1;
    v[i] = aleatorio;
  }

  for (int i = 0; i < 10; i++) {
    cout << v[i] << " ";
  }

  cout << endl;
  minMax(v, &max, &min);
  cout << "Mínimo: " << min << "\nMáximo: " << max << endl;
  return 0;
}
