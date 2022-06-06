#include <iostream> 
#include <cmath> // Prototype of pow().

using namespace std;

int main()
{
    double x = 2.5;
    double y;

    /* By means of a prototype, the compiler generates the correct call or an error message. */
    y = pow( "x", 3.0 );    // Error. A string is not a number.
    y = pow( x + 3.0 );     // Error. Only one argument provided.
    y = pow( x, 3.0 );      // OK.
    y = pow( x, 3 );        // OK. The compiler converts the int value 3 to double.

    cout << "2.5 raised to 3 yields: " << y << endl;
    cout << "2 + (5 raised to the power 2.5) yields: " << 2.0 + pow( 5.0, x ) << endl; // Calculating with pow() is possible.

    return 0;
}