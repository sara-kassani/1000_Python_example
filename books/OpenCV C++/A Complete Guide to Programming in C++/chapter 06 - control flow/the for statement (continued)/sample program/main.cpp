#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    long    m_lEuro;
    long    m_lMaxEuro;
    double  m_dRate;

    cout << "\n* * * TABLE OF EXCHANGE " << " Euro - US-$ * * *\n\n";

    cout    << "\nPlease give the rate of exchange:  one Euro in US-$: ";
    cin     >> m_dRate;
    cout    << "\nPlease enter the maximum euro: ";
    cin     >> m_lMaxEuro;

    cout << '\n' << setw( 12 ) << "Euro" << setw( 20 ) << "US-$" << "\t\tRate: " << m_dRate << endl;

    cout << fixed << setprecision( 2 ) << endl;

    long m_lLower;
    long m_lUpper;
    long m_lStep;

    for ( m_lLower = 1, m_lStep = 1; m_lLower <= m_lMaxEuro; m_lStep *= 10, m_lLower = 2 * m_lStep )
    {
        for ( m_lEuro = m_lLower, m_lUpper = m_lStep * 10; m_lEuro <= m_lUpper && m_lEuro <= m_lMaxEuro; m_lEuro += m_lStep )
        {
            cout << setw( 12 ) << m_lEuro << setw( 20 ) << m_lEuro * m_dRate << endl;
        }
    }

    return 0;
}