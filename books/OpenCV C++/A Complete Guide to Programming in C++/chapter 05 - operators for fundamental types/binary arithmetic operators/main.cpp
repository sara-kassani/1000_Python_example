#include <iostream>

using namespace std;

int main()
{
    double m_dX;
    double m_dY;

    cout    << "Enter two floating-point variables: ";
    cin     >> m_dX >> m_dY;
    cout    << "The average of the two numbers is: " << ( m_dX + m_dY ) / 2.0 << endl;

    return 0;
}