#include <iostream>

using namespace std;

int main()
{
    float m_fX;
    float m_fY;

    cout << "Enter two different numbers:\n";

    if ( cin >> m_fX && cin >> m_fY )
    {
        float m_fMin;

        if ( m_fX < m_fY )
        {
            m_fMin = m_fX;
        } else
        {
            m_fMin = m_fY;
        }

        cout << "\nThe smaller number is: " << m_fMin << endl;
    } else
    {
        cout << "\nInvalid input!" << endl;
    }

    return 0;
}