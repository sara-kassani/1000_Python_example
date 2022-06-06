#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double m_dRate = 1.15;

    cout << fixed << setprecision( 2 );
    cout << "\tEuro \tDollar\n";

    for ( int i = 1; i <= 5; ++i )
    {
        cout << "\t " << i << "\t " << i * m_dRate << endl;
    }

    return 0;
}