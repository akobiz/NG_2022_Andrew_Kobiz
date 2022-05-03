#include <iostream>

using namespace std;

int main()
{
    short size;
    cout << "Enter your size: "; cin >> size;
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            if(i == 0 || i == size - 1) cout << '*';
            if(i != 0 && i != size - 1 && j == 0) cout << '*';
            if(i != 0 && i != size - 1 && j < size - 2 ) cout << ' ';
            if(i != 0 && i != size - 1 && j == size - 1 ) cout << '*';


        }
        cout << endl;
    }
    cout << endl;
    return 0;
}
