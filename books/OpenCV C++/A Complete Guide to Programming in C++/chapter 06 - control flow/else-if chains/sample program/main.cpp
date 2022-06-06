#include <iostream>

using namespace std;

int main()
{
    float m_fLimit;
    float m_fSpeed;
    float m_fTooFast;

    cout    << "\nSpeed limit: ";
    cin     >> m_fLimit;
    cout    << "\nSpeed: ";
    cin     >> m_fSpeed;

    if ( ( m_fTooFast = m_fSpeed - m_fLimit ) < 10 )
    {
        cout << "You were lucky!" << endl;
    } else if ( m_fTooFast < 20 )
    {
        cout << "Fine payable: 40,-. Dollars" << endl;
    } else if ( m_fTooFast < 30 )
    {
        cout << "Fine payable: 80,-. Dollars" << endl;
    } else
    {
        cout << "Hand over your driver's license!" << endl;
    }

    return 0;
}