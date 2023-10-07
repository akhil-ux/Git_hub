#include <iostream>
#include <stdlib.h>
using namespace std;

class student
{
private:
    int a, b, c;

public:
    int d, e;
    void setdata(int a, int b, int c,int d , int e);
    void getdata()
    {
        cout << "Value of a is  " << a << endl;
        cout << "Value of b is  " << b << endl;
        cout << "Value of c is  " << c << endl;
        cout << "Value of d is  " << d << endl;
        cout << "Value of e is  " << e << endl;
    }
};                                                              
void student ::setdata(int a1, int b1, int c1,int d1 , int e1)
{
    a = a1;
    b = b1;
    c = c1;
    d=d1;
    e=e1;
}
int main()
{
    student akhil;
    akhil.setdata(1, 2, 3,19,20);
    akhil.getdata();

    return 0;
}