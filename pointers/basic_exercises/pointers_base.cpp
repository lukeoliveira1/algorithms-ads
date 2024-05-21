#include <ctime>
#include <iostream>
#include <stdlib.h>

using namespace std;

void one() {
  int a = 2;
  float b = 2.5;
  char c = 'c';

  cout << "Questão 1" << endl;
  cout << "Valores Antigos" << endl;
  cout << a << endl;
  cout << b << endl;
  cout << c << endl;

  int *ptrInt;
  float *ptrFloat;
  char *ptrChar;

  // ponteiros recebendo endereço dos valores das variáveis
  ptrInt = &a;
  ptrFloat = &b;
  ptrChar = &c;

  // alterando valores das variáveis com ponteiros
  *ptrInt = 1;
  *ptrFloat = 1.5;
  *ptrChar = 'd';

  cout << "Valores Novos" << endl;
  cout << a << endl;
  cout << b << endl;
  cout << c << endl;
}

int two(int *ptrA, int *ptrB) {
  // criando variavel para receber a soma
  int soma = *ptrA + *ptrB;
  // atribuindo o valor da soma em A
  *ptrA = soma;
  return *ptrA;
}

void three() {
  // criando array
  float array[10];

  // imprimindo endereço de cada posição
  for (int i = 0; i < 10; i++) {
    cout << &array[i] << "\n";
  }
}

void four() {
  // criando matriz
  float matriz[3][3];

  // imprimindo endereço de cada posição
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout << &matriz[i][j] << "\n";
    }
  }
}

void five() {
  int arr[10]; // arr: arranjo com 10 inteiros
  int *ptr;    // ptr:  ponteiro para um inteiro
  int x;       // receber valor

  ptr = &arr[0]; // inicializa ponteiro

  // preenchendo conteúdo do arranjo via ponteiro
  for (int i = 0; i < 10; ++i) {
    cin >> x;
    *(ptr + i) = x; // ponteiro vai avançando de posição no vetor
  }

  for (int i = 0; i < 10; ++i) { // imprimindo cada valor dobrado
    cout << arr[i] * 2 << " ";
  }
}

void six() {
  int arr[10]; // arr: arranjo com 10 inteiros
  int *ptr;    // ptr:  ponteiro para um inteiro
  int x;       // receber valor

  ptr = &arr[0]; // inicializa ponteiro

  // preenchendo conteúdo do arranjo via ponteiro
  for (int i = 0; i < 10; ++i) {
    cin >> x;
    *(ptr + i) = x; // ponteiro vai avançando de posição no vetor
  }

  // imprimindo endereço de posições pares
  for (int i = 0; i < 10; ++i) {
    if (arr[i] % 2 == 0) {
      cout << &arr[i] << endl;
    }
  }
}

void seven() {
  int A = 5, *B, **C, ***D;

  B = &A; // dobro
  C = &B; // triplo
  D = &C; // quadruplo

  cout << A << endl;
  cout << *B * 2 << endl;
  cout << **C * 3 << endl;
  cout << ***D * 4 << endl;
}

void eight(int *pt1, int *pt2, int *pt3) {
  if (*pt1 == *pt2 == *pt3) {
    cout << "1" << endl; // se valores forem igual
    cout << pt1 << " " << pt2 << " " << pt3 << endl;
  } else {
    cout << "0" << endl; // se forem diferentes

    // ordenando do menor para o maior
    if ((*pt1 > *pt2) and (*pt1 > *pt3)) {
      if (*pt2 > *pt3) {
        cout << *pt3 << " " << *pt2 << " " << *pt1 << endl;
        ;
      } else {
        cout << *pt2 << " " << *pt3 << " " << *pt1 << endl;
      }
    } else if ((*pt2 > *pt1) and (*pt2 > *pt3)) {
      if (*pt1 > *pt3) {
        cout << *pt3 << " " << *pt1 << " " << *pt2 << endl;
      } else {
        cout << *pt1 << " " << *pt3 << " " << *pt2 << endl;
      }
    } else {
      if (*pt1 > *pt2) {
        cout << *pt2 << " " << *pt1 << " " << *pt3 << endl;
      } else {
        cout << *pt1 << " " << *pt2 << " " << *pt3 << endl;
      }
    }
  }
}

void nine(float num, int *inteiro, float *frac) {

  *inteiro = (int)num;    // inteiro recebe parte inteira
  *frac = num - *inteiro; // fracionário recebe o número - parte inteira

  cout << "Parte inteira: " << *inteiro << "\nParte frac: " << *frac << endl;
}

int ten(float *vet, int N) {
  int n = 0; // contador de negativos

  for (int i = 0; i < N; i++) {
    cout << vet[i] << " "; // imprimindo vetor
  }

  cout << endl;

  for (int i = 0; i < N; i++) {
    if (vet[i] < 0) { // se valor < 0 então n++
      cout << vet[i] << " ";
      n++;
    }
  }

  cout << endl;

  return n;
}

void eleven(int *vet, int &min, int &max, int n) {
  int maximo = vet[0];
  int minimo = vet[0];

  // pegando o max e o min
  for (int i = 0; i < n; i++) {
    if (vet[i] > maximo) {
      maximo = vet[i];
    }
    if (vet[i] < minimo) {
      minimo = vet[i];
    }
  }

  // imprimindo o vetor
  for (int i = 0; i < n; i++) {
    cout << vet[i] << " ";
  }

  cout << endl;

  cout << "Menor valor: " << minimo << ", Maior valor: " << maximo;
}

int twelve(int *vet1, int *vet2, int n1, int n2) {
  int cont = 0; // contador para pos do novo vetor

  for (int i = 0; i < 5; i++) {
    if (vet1[i] == vet2[i]) { // se os valores forem iguais +1pos
      cont++;
    } else {
      cont = cont + 2; // se forem diferentes +2pos
    }
  }

  // qntd quantidade de pos no vetor
  int *vet = new int(cont * sizeof(int));

  for (int i = 0; i < cont; i++) {
    vet[i] = rand() % 100;
  }

  int j = 0;
  int v1 = 0;
  int v2 = 0;

  // preenchendo e ordenando novo vetor
  for (int i = 0; i < 5; i++) {

    if (vet1[v1] == vet2[v2]) {
      vet[j] = vet1[v1];
      j++;
      v1++, v2++;
    }
    if (vet1[v1] < vet2[v2]) {
      vet[j] = vet1[v1];
      j++;
      v1++;
    }
    if (vet2[v2] < vet1[v1]) {
      vet[j] = vet2[v2];
      j++;
      v2++;
    }

    if ((v1 == 6) && (v2 == 4)) {
      vet[6] = vet2[4];
    }
  }

  cout << "Vetor unido e ordenado: ";
  for (int i = 0; i < cont; i++) {
    cout << vet[i] << " ";
  }

  cout << '\n';

  return cont;
}

void thirteen(int *vet1, int *vet2, int n1, int n2, int *qtd) {
  int cont = 0; // contador de pos novo vetor

  for (int i = 0; i < n1; i++) {
    if (vet1[i] == vet2[i]) {
      cont++;
    }
  }

  int *vet = new int(cont * sizeof(int));

  int j = 0;

  // preenchendo e ordendando vetor
  for (int i = 0; i < n2; i++) {

    if (vet1[i] == vet2[i]) {
      vet[j] = vet1[i];
      j++;
    }
  }

  cout << '\n';

  cout << "Vetor intersecção: ";
  for (int i = 0; i < cont; i++) {
    cout << vet[i] << " ";
  }

  cout << '\n';

  qtd = &cont;
  cout << "Quantidade de pos no vetor intersecção: " << *qtd;
}

void fourteen(int *vet, int qntd) {

  // preenchendo
  for (int i = 0; i < qntd; i++) {
    vet[i] = rand() % 20;
  }

  // exibindo
  for (int i = 0; i < qntd; i++) {
    cout << *(vet + i) << " ";
  }
}

int main() {
  one();

  int a = 5;
  int b = 2;
  cout << "\nQuestão 2 \n" << two(&a, &b) << endl;

  cout << "\nQuestão 3" << endl;
  three();

  cout << "\nQuestão 4" << endl;
  four();

  cout << "\nQuestão 5" << endl;
  five();

  cout << "\nQuestão 6" << endl;
  six();

  cout << "\nQuestão 7" << endl;
  seven();

  cout << "\nQuestão 8" << endl;
  int j = 22, d = 12, c = 33;
  eight(&j, &d, &c);

  cout << "\nQuestão 9" << endl;
  float num, fracionario;
  int inteiro;
  cin >> num;
  nine(num, &inteiro, &fracionario);

  cout << "\nQuestão 10" << endl;
  float arr[10];
  srand((unsigned(time(0))));
  for (int i = 0; i < 10; i++) {
    int aleatorio = rand() % (5 - (-5) + 1) - 5;
    arr[i] = aleatorio;
  }
  cout << ten(arr, 10) << endl;

  cout << "\nQuestão 11";
  int n;
  int *pmax, *pmin;
  cout << "\nDigite o tamanho do vetor: \n";
  cin >> n;
  int vet[11];
  int *ptr = &vet[0];
  // preenchendo aleatoriamente
  for (int i = 0; i < n; i++) {
    vet[i] = rand() % 50;
  }
  eleven(ptr, *pmax, *pmin, n);
  cout<<endl;

  cout << "\nQuestão 12";
  cout << "\n";
  int vet1[] = {1, 3, 4, 7, 9};
  int vet2[] = {1, 2, 4, 6, 8};
  int tam1 = sizeof vet1;
  int tam2 = sizeof vet2;
  int *ptr1 = &vet1[0];
  int *ptr2 = &vet2[0];
  twelve(ptr1, ptr2, tam1, tam2);
  cout << "\n";

  // cout << "Questão 13";
  // cout << "\n";
  // int qntdVet3;
  // int vet13One[] = {1, 3, 5, 6, 9};
  // int vet13Two[] = {1, 3, 5, 7, 8};
  // int tam13One = sizeof vet13One;
  // int tam13Two = sizeof vet13Two;
  // int *ptr13One = &vet13One[0];
  // int *ptr13Two = &vet13Two[0];
  // thirteen(ptr13One, ptr13Two, tam13One, tam13Two, &qntdVet3);

  // cout << "\nQuestão 14" << endl;
  // int qntd;
  // cin >> qntd;
  // int *vet14 = new int(qntd * sizeof(int));
  // fourteen(vet14, qntd);

  cout << "\nQuestão 15" << endl;
  cout << "adicionado 4bytes de memória no ponteiro" << endl;
  cout << "i segue 34" << endl;
  cout << "j será 33" << endl;

  cout << "\nQuestão 16" << endl;
  cout << "O código cria, preenche e exibe uma matriz 2x2" << endl;
  cout << "Ocorre alocação para as linhas, e em seguida para as colunas"
       << endl;
  cout << "No final é liberada a memória" << endl;

  return 0;
}
