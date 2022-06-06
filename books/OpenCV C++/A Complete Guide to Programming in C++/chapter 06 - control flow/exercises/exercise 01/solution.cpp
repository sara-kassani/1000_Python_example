#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    long    m_lMaxEuro;
    double  m_dRate;

    cout << "\n* * * TABLE OF EXCHANGE " << " Euro - US-$ * * *\n\n";

    cout    << "\nPlease give the rate of exchange:  one Euro in US-$: ";
    cin     >> m_dRate;
    cout    << "\nPlease enter the maximum euro: ";
    cin     >> m_lMaxEuro;

    cout << '\n' << setw( 12 ) << "Euro" << setw( 20 ) << "US-$" << "\t\tRate: " << m_dRate << endl;

    cout << fixed << setprecision( 2 ) << endl;

    long m_lStep    = 1;
    long m_lLower   = 1;
    long m_lUpper;
    long m_lEuro;

    while ( m_lLower <= m_lMaxEuro )
    {
        m_lUpper    = m_lStep * 10;
        m_lEuro     = m_lLower;

        while ( m_lEuro <= m_lUpper && m_lEuro <= m_lMaxEuro )
        {
            cout << setw( 12 ) << m_lEuro << setw( 20 ) << m_lEuro * m_dRate << endl;

            m_lEuro += m_lStep;
        }

        m_lStep     *= 10;
        m_lLower    = 2 * m_lStep;
    }

    return 0;
}