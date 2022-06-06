#include <iostream>
#include <iomanip> // Defines the standard manipulators (setw).

using namespace std;

int main()
{
    cout << '|'     << setw( 6 )            << 'X'          << '|'      << endl << endl;                    // Width of field: 6.
    cout << fixed   << setprecision( 2 )    << setw( 10 )   << 123.4    << endl << "1234567890" << endl;    // Fixed-point notation with a precision of 2 numbers after the decimal point and a field width of 10.

    return 0;
}