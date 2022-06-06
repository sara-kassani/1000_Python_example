#include <iostream>

using namespace std;

const long m_clDelay = 10000000L;

int main()
{
    int m_iTic;

    cout    << "\nHow often should the tone be output? ";
    cin     >> m_iTic;

    do
    {
        for ( long i = 0; i < m_clDelay; ++i );

        cout << "Now the tone!\a" << endl;
    } while ( --m_iTic > 0 );

    cout << "End of the acoustic interlude!\n";

    return 0;
}