#include <iostream>

using namespace std;

int ** alocarMatriz(int nl, int nc){
    int **mtr, aleatorio;
    
    srand((unsigned)time(0));
    
    
    //alocando memória para linhas
    mtr = new int * [nl];
    
    //alocando memória para colunas
    for(int i=0; i< nl; i++) {
        mtr[i] = new int [nc];
    }
    
    //preenchendo matriz
    for(int i=0; i<nl; i++) {
        for(int j=0; j<nc; j++) {
            aleatorio = rand()%(1 - 0 + 1) + 0;
            mtr[i][j]= aleatorio;
            // if(i ==j) {
            //     mtr[i][j] = 1;
            // } else {
            //     mtr[i][j]=0;
            // }
        }
    }
    
    //imprimindo matriz
     for(int i=0; i<nl; i++) {
        for(int j=0; j<nc; j++) {
            cout<<mtr[i][j]<<" ";
        }
        cout<<endl;
     }
     
     return mtr;
    
}

void deletarMatriz(int ** Pmatriz, int nl){
    
    for(int i=0; i<nl; i++) {
            delete[] Pmatriz[i];
    }
    delete[] Pmatriz;

}

int ehMatrizIdentidade ( int ** mat, int nl) {
    int res;
    
    if(mat[0][0] == 1) {
        
        for(int i=0; i<nl; i++) {
            for(int j=0; j<nl; j++) {
                
                if(j != i) {
                    if(mat[i][j] == 0) {
                        res = 1;
                    } else {
                        res = 0;
                        break;
                    }
                } else {
                    if(mat[i][j] == 1) {
                        res = 1;  
                    } else {
                        res = 0;
                        break;
                    }
                }
            }
        }  
    } else {
        res = 0;
    }
    
     return res;
}

int main()
{
   
    int ordem=5;
    int **ptrMatriz;
    
    ptrMatriz = alocarMatriz(ordem, ordem);
    cout<<ehMatrizIdentidade(ptrMatriz, ordem);
    deletarMatriz(ptrMatriz, ordem);
    return 0;
}