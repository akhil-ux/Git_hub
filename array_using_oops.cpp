#include <iostream>
#include <stdlib.h>
using namespace std;
class Shop
{
    int itemid[100];
    int itemprice[100];
    int counter;

public:
    void initcounter(void)
    {
        counter = 0;
    }
    void setprice(void);
    void getprice(void);
};
void Shop ::setprice(void)
{
    cout << "enter id of ur item number"<<counter+1 << endl;
    cin >> itemid[counter];
    cout << "enter price of ur item"<<counter+1 << endl;
    cin >> itemprice[counter];
    counter++;
}
void Shop ::getprice(void)
{
    for (int i = 0; i < counter; i++)
    {
        cout << "price of the item ith id " << itemid[i] <<"is " << itemprice[i] << endl;
    }
}
int main()
{
    Shop Dukaan;
    Dukaan.initcounter();
    Dukaan.setprice();
    Dukaan.setprice();
    Dukaan.setprice();
    Dukaan.getprice();
    return 0;
}