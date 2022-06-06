#include <iostream>
#include <string> // Declaration of class string.

using namespace std;

int main()
{
    string prompt( "What is your name: " );
    string name;
    string line( 40, '-' ); // An empty string with 40 '-' characters is possible.
    string total = "Hello ";

    cout << prompt;

    getline( cin, name ); // Inputs a name in one line.

    total = total + name; // Concatenates and assigns strings.

    cout << line << endl << total << endl;
    cout << " Your name is " << name.length() << " characters long!" << endl; // Displays the length of the name.
    cout << line << endl;

    return 0;
}