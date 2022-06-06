#ifndef _MYMACROS_

#define _MYMACROS_

#include <iostream>

using namespace std;

#define ABS( x )    ( x > 0 ? x : -(x) )
#define MAX( x, y ) ( x > y ? x : y )

#define END     ( 2.0 * PI )
#define STEP    ( PI / 8.0 )
#define HEADER  ( cout << "  ****** Sine Function Table *****\n\n" )

#define CLS             ( cout << "\033[2J" )
#define LOCATE( r, c )  ( cout << "\033[" << r << ';' << c << 'H' )

#define SCCOLOR( f, b ) ( cout << "\033[3" << (f) << ";4" << (b) << "m" )
#define NORMAL          ( cout << "\033[0" )

#endif
