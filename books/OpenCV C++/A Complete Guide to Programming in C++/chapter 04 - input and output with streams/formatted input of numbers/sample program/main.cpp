#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int m_iNumber = 0;

    cout    << "Enter a hexadecimal number: ";
    cin     >> hex >> m_iNumber;

    cout << "Your decimal input: " << m_iNumber << endl;

    cin.sync();
    cin.clear();

    double m_dX1 = 0.0;
    double m_dX2 = 0.0;

    cout    << "\nNow enter two floating-point values: " << endl;
    cout    << "1. Number: ";
    cin     >> m_dX1;
    cout    << "2. Number: ";
    cin     >> m_dX2;

    cout << fixed                               << setprecision( 2 )    << "\nThe sum of both numbers: "    << setw( 10 ) << m_dX1 + m_dX2 << endl;
    cout << "\nThe product of both numbers: "   << setw( 10 )           << m_dX1 * m_dX2                    << endl;

    return 0;
}