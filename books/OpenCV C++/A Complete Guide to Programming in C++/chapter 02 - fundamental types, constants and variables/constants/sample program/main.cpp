#include <iostream>

using namespace std;

int main()
{
    cout << "Value of 0xFF = " << 0xFF << " (decimal)" << endl;           // cout outputs integers as decimal integers.
    cout << "Value of 27 = " << hex << 27 << " (hexadecimal)" << endl;    // The manipulator hex changes output to hexadecimal format (dec changes to decimal format).

    return 0;
}