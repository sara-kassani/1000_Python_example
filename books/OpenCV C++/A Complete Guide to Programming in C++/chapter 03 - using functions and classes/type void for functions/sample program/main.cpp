#include <iostream>
#include <cstdlib> // Prototypes of srand(), rand().

using namespace std;

int main()
{
    unsigned int m_uiSeed;

    int z1;
    int z2;
    int z3;

    cout << " --- Random Numbers --- \n" << endl;
    cout << "To initialize the random number generator, please enter an integer value: ";
    cin >> m_uiSeed; // Input an integer.

    srand( m_uiSeed ); // Generate a new sequence of numbers based on the seed.

    /* Compute three random numbers. */
    z1 = rand();
    z2 = rand();
    z3 = rand();

    cout << "\nThree random numbers: " << z1 << " " << z2 << " " << z3 << endl;

    while( 1 );

    return 0;
}