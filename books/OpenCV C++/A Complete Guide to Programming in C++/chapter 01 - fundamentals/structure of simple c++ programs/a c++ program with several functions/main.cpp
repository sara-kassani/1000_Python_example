#include <iostream> // Input/output stream header.

using namespace std; // Standard namespace.

/* [ Prototypes ] */
void PrintLine();
void PrintMessage();

int main()
{
    cout << "Hello! The program starts in main()." << endl;

    PrintLine();
    PrintMessage();
    PrintLine();

    cout << "At the end of main()." << endl;

    return 0;
}

/*
 * Prints a line of dashes.
 *
 * return   nothing
 */
void PrintLine()
{
    cout << "--------------------------------" << endl;
}

/*
 * Prints "In function PrintMessage()."
 *
 * return   nothing
 */
void PrintMessage()
{
    cout << "In function PrintMessage()." << endl;
}