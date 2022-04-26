#include <iostream>

using namespace std;

int main()
{
    int age;
    cout << "Enter your age: ";
    cin >> age;
    if(age < 10)
        cout << "Wo-ow! You're such an adult!!" << endl;
    else {
        cout << "Do you study?(1/0): ";
        cin >> age;
        if (age == 1) cout << "You're amazing!" << endl;
        if (age == 0) cout << "So... why?" << endl;
    }
    return 0;
}
