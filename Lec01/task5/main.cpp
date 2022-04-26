#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a, b, c, discr;
    cout << "Enter three numbers: "; cin >> a >> b >> c;
    cout << "Quadratic equation: " << a << "x^2 + " << b << "x - " << c << " = 0" << endl;
    discr = pow(b, 2) - 4*(-a)*c;
    cout << "D = " << discr << endl;;
    if (discr < 0) cout << "There are no roots." << endl;
    if (discr == 0) cout << "There are 1 root: x = " << (-b + sqrt(discr))/(2*a) << endl;
    if (discr > 0){
        cout << "There are 2 roots: x1 = " << int((-b + sqrt(discr)) / (2 * a)) << endl;
        cout << "                   x2 = " << int((-b - sqrt(discr)) / (2 * a)) << endl;
    }

    return 0;
}
