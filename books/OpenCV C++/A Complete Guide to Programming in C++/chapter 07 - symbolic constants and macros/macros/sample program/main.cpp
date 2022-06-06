#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

#define PI      3.1415926536
#define START   0.0
#define END     ( 2.0 * PI )
#define STEP    ( PI / 8.0 )
#define HEADER  ( cout << "  ****** Sine Function Table *****\n\n" )

int main()
{
    HEADER;

    cout << setw( 16 ) << "x" << setw( 20 ) << "sin(x)\n" << "  -----------------------------------------" << fixed << endl;

    for ( double i = START; i < END + STEP / 2; i += STEP )
    {
        cout << setw( 20 ) << i << setw( 16 ) << sin( i ) << endl;
    }

    cout << endl << endl;

    return 0;
}