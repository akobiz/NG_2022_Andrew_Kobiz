#include <iostream>

using namespace std;

int main()
{
    int number = 0;
    int hashNumber = 0;
    cout << "Enter your number: "; cin >> number;
    int firstNumber = number;
    while (firstNumber > 9) {
        firstNumber = firstNumber/10;
    }
    for(int i = 0; i < 15; i++){
        if(number%10 == (number/10)%10 || number%10 == firstNumber){
            hashNumber = hashNumber + number%10;
            firstNumber = 0;
        }
        number = number/10;
    }
    if(hashNumber == 0) cout << "There are no hash codes." << endl;
    else cout << "Hash code of this number is: " << hashNumber << endl;
    return 0;
}
