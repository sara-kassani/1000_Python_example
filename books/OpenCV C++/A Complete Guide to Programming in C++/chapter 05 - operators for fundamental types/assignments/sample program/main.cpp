#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float m_fX;
    float m_fY;

    cout    << "Please enter a starting value: ";
    cin     >> m_fX;

    cout    << "\nPlease enter the increment value: ";
    cin     >> m_fY;

    m_fX += m_fY;

    cout    << "\nAnd now multiplication!";
    cout    << "\nPlease enter a factor: ";
    cin     >> m_fY;

    m_fX *= m_fY;

    cout    << "\nFinally division.";
    cout    << "\nPlease supply a divisor: ";
    cin     >> m_fY;

    m_fX /= m_fY;

    cout << "\nAnd this is your current lucky number: " << fixed << setprecision( 0 ) << m_fX << endl;

    return 0;
}