#include <iostream>

using namespace std;

int main()
{
    int number = 0;
    int sumNumber = 0;
    cout << "Enter your number: "; cin >> number;
    for(int i = 0; i < 10; i++){
        if((number %10)%2 == 0){
            sumNumber = sumNumber + number %10;
        }
        number = number / 10;
    }
    cout << "Sum of even numbers are: " << sumNumber << endl;
    return 0;
}
