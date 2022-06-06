#include <cmath>
#include <iostream>

using namespace std;

int main()
{
    cout << "Number \tSquare Root"  << endl;
    cout << " 4     \t"             << sqrt( 4 )        << endl;
    cout << "12.25  \t"             << sqrt( 12.25 )    << endl;
    cout << " 0.0121\t"             << sqrt( 0.0121 )   << endl << endl;

    double m_dNum;

    cin >> m_dNum;

    cout << "\nNumber\tSquare Root" << endl;
    cout << m_dNum << "\t" << sqrt( m_dNum ) << endl;

    return 0;
}