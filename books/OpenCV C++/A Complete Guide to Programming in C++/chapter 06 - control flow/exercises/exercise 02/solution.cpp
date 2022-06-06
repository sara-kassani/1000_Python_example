#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout << setw( 45 ) << "****** MULTIPLICATION TABLE ******\n\n" << setw( 11 ) << 1;

    for ( int i = 2; i <= 10; ++i )
    {
        cout << setw( 5 ) << i;
    }

    cout << endl << setw( 56 ) << right << "-----------------------------------------------------" << endl;

    for ( int i = 1; i <= 10; ++i )
    {
        cout << right << setw( 5 ) << i << " |" << setw( 4 ) << i;

        for ( int j = 2; j <= 10; ++j )
        {
            cout << setw( 5 ) << i * j;
        }

        cout << endl;
    }

    return 0;
}