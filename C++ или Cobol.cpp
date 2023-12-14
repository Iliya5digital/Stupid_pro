#include <iostream>
using namespace std;
int main(){
int n, m, k;
cin >>n >>m >>k;
int res, i=0;
while (res!=n){
    if (i==2 && res==m) break;
    int f, g; //количество, необходимое, чтоб С++ было в группе больше g количество возможных групп с С++
    f=k/2+1;
    g=m/f;
    res=g*k; //количество людей, владеющих С++
    i++;
}
    if (i==2 && res==m) cout <<-1;
    else cout <<i;
    return 0;
}