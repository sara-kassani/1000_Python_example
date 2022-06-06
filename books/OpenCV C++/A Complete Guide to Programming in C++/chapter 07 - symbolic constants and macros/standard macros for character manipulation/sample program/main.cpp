#include <iostream>
#include <ctype.h>

using namespace std;

int main()
{
    char m_char;
    long m_lNChar = 0;
    long m_lNConv = 0;

    while ( cin.get( m_char ) )
    {
        ++m_lNChar;

        if ( islower( m_char ) )
        {
            m_char = toupper( m_char );

            ++m_lNConv;
        }

        cout.put( m_char );
    }

    clog << "\nTotal of characters:           " << m_lNChar << "\nTotal of converted characters: " << m_lNConv << endl;

    return 0;
}