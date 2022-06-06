#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    unsigned short m_usSeed;

    cout    << "Enter a seed number between 0 and 65535: ";
    cin     >> m_usSeed;

    srand( m_usSeed );

    cout << endl;

    for ( unsigned short i = 1; i <= 20; ++i )
    {
        cout << setw( 2 ) << right << i << " number: " << setw( 3 ) << rand() % 100 + 1 << endl;
    }

    return 0;
}