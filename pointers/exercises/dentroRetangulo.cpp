#include <iostream>

using namespace std;

//Usando typedef na struct para encurtar o comando na declaração
typedef struct _Ponto {
int x;
int y;
} Ponto;

//const - não é modificável
int dentroRet (const Ponto* v1, const Ponto* v2, const Ponto* p){
     if(((*p).x >= (*v1).x && (*p).x <= (*v2).x)&&((*p).y >= (*v1).y && (*p).y <= (*v2).y)){
        return 1;
    }
    else{
        return 0;
    }
}

int main()
{
    Ponto v1,v2,P;

    cout << "Insira a coordenada do vértice inferior esquerdo do retângulo: \n";
    cout << "X = ";
    cin >> v1.x;
    cout << "Y = ";
    cin >> v1.y;
    cout << "Agora insira a coordenada do vértice superior direito do retângulo\n";
    cout << "X = ";
    cin >> v2.x;
    cout << "Y = ";
    cin >> v2.y;

    cout << "As coordenadas dos vértices retângulo são: "<<"("<<v1.x <<"," <<v1.y<<")"<<"(" <<v2.x<<","<< v2.y<<")"<<endl;
    cout<<"\nInsira a posição do ponto"<<endl;
    cout<<"X = ";
    cin>>P.x;
    cout<<"Y = ";
    cin>>P.y;
   
    cout<<dentroRet(&v1, &v2, &P);

    return 0;
}
