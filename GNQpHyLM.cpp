#include <iostream>
using namespace std;
int main(){
    int a, b; //нод и нок
    cin >>a >>b; //нод и нок
    for (int i=a; i<b; i++){
        for (int j=a+1; j<b; j++) {
            if (i % a == 0 && j % a == 0) {
                cout << i << " " << j;
                break;
            }
            if (i==b-1 && j==b-1) cout<< -1;
            }
        }
    return 0;
}