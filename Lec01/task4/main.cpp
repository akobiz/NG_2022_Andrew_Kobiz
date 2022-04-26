#include <iostream>

using namespace std;

int main()
{
    int motherboard, gpu, cpu, discount;
    cout << "Motherboard price($): "; cin >> motherboard;
    cout << "Videocard price($): "; cin >> gpu;
    cout << "CPU price($): "; cin >> cpu;
    cout << "Discount(%): "; cin >> discount;
    cout << "Your PC will cost " << (motherboard+gpu+cpu)-(((motherboard+gpu+cpu)*discount)/100) << "$" << endl;
    return 0;
}
