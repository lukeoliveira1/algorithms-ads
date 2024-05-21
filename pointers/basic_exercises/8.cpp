#include <iostream>

using namespace std;

void eight(int *pt1, int *pt2, int *pt3) {
    if(*pt1 == *pt2 == *pt3) {
        cout<<"1"<<endl;
    } else {
        cout<<"0"<<endl;
    }
    
    if((*pt1 > *pt2) and (*pt1 > *pt3)) {
        if(*pt2 > *pt3) {
            cout<<*pt3<<" "<<*pt2<<" "<<*pt1;
        } else {
            cout<<*pt2<<" "<<*pt3<<" "<<*pt1;
        }
    } else if ((*pt2 > *pt1) and (*pt2 > *pt3)) {
        if(*pt1 > *pt3) {
            cout<<*pt3<<" "<<*pt1<<" "<<*pt2;
        } else {
            cout<<*pt1<<" "<<*pt3<<" "<<*pt2;
        }
    } else {
        if(*pt1 > *pt2) {
            cout<<*pt2<<" "<<*pt1<<" "<<*pt3;
        } else {
            cout<<*pt1<<" "<<*pt2<<" "<<*pt3;
        }
    }
    
    
}

int main()
{
   int a=22, b=12, c=33;
   
   eight(&a, &b, &c);
   return 0;
    
}
