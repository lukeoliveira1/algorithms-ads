#include <iostream>

using namespace std;

int ** alocarMatriz(int nl, int nc){
    int **mtr;
    
    //alocando memória para linhas
    mtr = new int * [nl];
    
    //alocando memória para colunas
    for(int i=0; i< nl; i++) {
        mtr[i] = new int [nc];
    }
    
    //preenchendo matriz
    for(int i=0; i<nl; i++) {
        for(int j=0; j<nc; j++) {
            mtr[i][j]= i+1;
        }
    }
    
    //imprimindo matriz
     for(int i=0; i<nl; i++) {
        for(int j=0; j<nc; j++) {
            cout<<mtr[i][j]<<" ";
        }
        cout<<endl;
     }
     
     cout<<endl;
     return mtr;
    
}

void deletarMatriz(int ** Pmatriz, int nl){
    
    for(int i=0; i<nl; i++) {
            delete[] Pmatriz[i];
    }
    delete[] Pmatriz;

}

int main()
{
   
    int nl=4;
    int nc=5;
    int **ptrMatriz;
    
    ptrMatriz = alocarMatriz(nl,nc);
    deletarMatriz(ptrMatriz, nl);
    return 0;
}