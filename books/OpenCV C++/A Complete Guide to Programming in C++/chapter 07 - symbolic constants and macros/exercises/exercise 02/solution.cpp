#include <iostream>
#include <string>
#include <conio.h>
#include "myMacros.h"

using namespace std;

#define DELAY           10000000L
#define CLS             ( cout << "\033[2J" )
#define LOCATE( r, c )  ( cout << "\033[" << r << ';' << c << 'H' )

int main()
{
    int m_iX        = 2;
    int m_iY        = 3;
    int m_iDx       = 1;
    int m_iSpeed    = 0;

    string m_szFloor( 79, '-' );
    string m_szHeader = "****  JUMPING BALL  ****";

    CLS;

    LOCATE( 1, 25 );
    cout << m_szHeader;

    LOCATE( 25, 1 );
    cout << m_szFloor;

    SCCOLOR( 7, 4 );

    while ( true )
    {
        LOCATE( m_iY, m_iX );
        cout << 'o' << endl;

        for ( long m_lWait = 0; m_lWait < DELAY; ++m_lWait );

        if ( m_iX == 1 || m_iX == 79 ) { m_iDx = -m_iDx; }

        if ( m_iY == 24 )
        {
            m_iSpeed = -m_iSpeed;

            if ( m_iSpeed == 0 ) { m_iSpeed = -7; }
        }

        m_iSpeed += 1;

        LOCATE( m_iY, m_iX );
        cout << ' ';

        m_iY += m_iSpeed;
        m_iX += m_iDx;

        if ( _kbhit() )
        {
            switch ( _getch() )
            {
                case 27: // ESCAPE key.
                {
                    return 0;
                    break;
                }

                case 43: // + (plus) key.
                {
                    ++m_iSpeed;
                    break;
                }

                case 45: { --m_iSpeed; } // - (minus) key.
            }
        }
    }
}