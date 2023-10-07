#include<iostream>
#include<stdlib.h>
using namespace std;

int sum(int a , int b)
{
    return a+b;
}
int sum(int a , int b , int c)
{
    return a+b+c;
}
// float area(int a , int b) 

int main(){
cout<<sum(10,20)<<endl;
cout<<sum(10,20,30)<<endl;
return 0;
}