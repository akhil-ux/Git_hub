#include <iostream>
#include <stdlib.h>
using namespace std;
static int count;
class Employee
{
    int id;
    static int count=0;
public:
    void setdata(void)
    {
        cout << "enter the id" << endl;
        cin >> id;
        count++;
    }
    void getdata(void)
    {
        cout << "employee id is " << id <<8"and employee number is "<<count<< endl;
        
    }
};
    int Employee ::  count;
int main()
{
    Employee harry;
    harry.setdata();
    harry.getdata();
    return 0;
}