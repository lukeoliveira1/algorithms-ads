#include <iostream>

using namespace std;

int main()
{
   int A = 5, *B, **C, ***D;
   
   B = &A ; //dobro
   C = &B; //triplo
   D = &C; //quadruplo
   
   cout<<A<<endl;
   cout<<*B*2<<endl;
   cout<<**C*3<<endl;
   cout<<***D*4<<endl;
   
   return 0;
    
}
