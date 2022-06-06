#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int m_iAc = 32;

    while ( true )
    {
        cout << "\nCharacter   Decimal   Hexadecimal\n\n";

        int m_iUpper;

        for ( m_iUpper = m_iAc + 20; m_iAc < m_iUpper && m_iAc < 256; ++m_iAc )
        {
            cout << "        " << ( char ) m_iAc << setw( 10 ) << dec << m_iAc << setw( 10 ) << hex << m_iAc << endl; 
        }

        if ( m_iUpper >= 256 ) { break; }

        cout << "\nGo on -> <return>,Stop -> <q>+<return>";

        char m_cAnswer;
        cin.get( m_cAnswer );

        if ( m_cAnswer == 'q' || m_cAnswer == 'Q' ) { break; }

        cin.sync();
    }

    return 0;
}