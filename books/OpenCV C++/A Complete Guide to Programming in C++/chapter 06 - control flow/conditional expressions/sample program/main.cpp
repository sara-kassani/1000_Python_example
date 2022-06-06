#include <iostream>

using namespace std;

int main()
{
    float m_fX;
    float m_fY;

    cout << "Type two different numbers:\n";

    if ( !( cin >> m_fX && cin >> m_fY ) )
    {
        cout << "Invalid input!" << endl;
    } else
    {
        cout << "\nThe greater value is: " << ( m_fX > m_fY ? m_fX : m_fY ) << endl;
    }

    return 0;
}