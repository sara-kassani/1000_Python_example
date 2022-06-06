#include <iostream>

using namespace std;

int main()
{
    int m_iI( 2 );
    int m_iJ( 8 );

    cout << m_iI++  << endl; // Output: 2
    cout << m_iI    << endl; // Output: 3
    cout << m_iJ--  << endl; // Output: 8
    cout << --m_iJ  << endl; // Output: 6

    return 0;
}