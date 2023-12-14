#include <iostream>
using namespace std;
int main(){
int a, b, k;
cin >>a >>b >>k;
for (int i=0; i<k; i++){
 if ((a-1)*b>=a*(b-1)) a-=1;
 else b-=1;
}
cout <<a <<" " <<b;
    return 0;
}