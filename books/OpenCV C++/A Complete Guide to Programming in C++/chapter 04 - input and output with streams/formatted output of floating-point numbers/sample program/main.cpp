#include <iostream>

using namespace std;

int main()
{
    double m_dX = 12.0;

    cout.precision( 2 ); // Set precision to 2 (numbers after the decimal point).

    cout << " By default: " << m_dX         << endl;
    cout << " showpoint:  " << showpoint    << m_dX << endl;
    cout << " fixed:      " << fixed        << m_dX << endl;
    cout << " scientific: " << scientific   << m_dX << endl;

    return 0;
}