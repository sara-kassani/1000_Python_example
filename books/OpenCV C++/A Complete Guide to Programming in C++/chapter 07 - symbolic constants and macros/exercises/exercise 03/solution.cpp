/* This solution was mostly influenced by the one within the book. */

#include <iostream>

using namespace std;

int main()
{
    char    m_char;
    int     m_iPred = 0;

    int m_iCtrls = 0;
    int m_iChars = 0;

    while ( cin.get( m_char ) )
    {
        if ( m_char <= 31 && m_char >= 0 && m_char != '\n' && m_char != '\t' )
        {
            m_iChars = 0;
            ++m_iCtrls;
        } else
        {
            if ( m_iCtrls > 0 )
            {
                cout.put( ' ' );

                m_iCtrls = 0;
            }

            switch ( ++m_iChars )
            {
                case 1:     { break; }
                case 2:     { cout.put( m_iPred ); }
                default:    { cout.put( m_char ); }
            }

            m_iPred = m_char;
        }
    }

    return 0;
}