#include <iostream>
#include <time.h>

using namespace std;

int main()
{
    char m_cPlayAgain;

    do
    {
        unsigned short  m_usAttempts    = 3;
        bool            m_bGuessed      = false;

        time_t m_ttSec;
        time( &m_ttSec );
        srand( ( unsigned ) m_ttSec );

        unsigned short m_usRandomNum = rand() % 15 + 1;
        unsigned short m_usGuessedNum;

        while ( m_usAttempts > 0 && !m_bGuessed )
        {
            cout    << endl << "You have " << m_usAttempts << " attempts at guessing the number left." << endl;
            cout    << "Your guess: ";
            cin     >> m_usGuessedNum;

            if ( m_usGuessedNum == m_usRandomNum )
            {
                cout << endl << "You've succesfully guessed the number " << m_usRandomNum << "." << endl;

                m_bGuessed = true;
            } else
            {
                --m_usAttempts;

                if ( m_usAttempts == 0 )
                {
                    cout << "You guessed incorrectly. The number was " << m_usRandomNum << "." << endl;
                } else
                {
                    cout << "Your guess was too " << ( m_usGuessedNum > m_usRandomNum ? "high" : "low" ) << "." << endl;
                }
            }
        }

        cout << endl << "Do you want to play again (Y/N): ";
        cin.get( m_cPlayAgain );
    } while ( m_cPlayAgain == 'Y' );

    return 0;
}