#include <iostream>

using namespace std;

int main()
{
    cout << showpos << 123 << endl; // Output: +123

    /* The above statement is equivalent to: */
    cout.setf( ios::showpos );
    cout << 123 << endl;

    cout << 22 << endl; // Other positive numbers are printed with their sign as well.

    cout << noshowpos << 123 << endl; // The output of a positive sign can be cancelled by the manipulator noshowpos.

    cout.unsetf( ios::showpos );
    cout << 123 << endl;

    getchar();

    return 0;
}