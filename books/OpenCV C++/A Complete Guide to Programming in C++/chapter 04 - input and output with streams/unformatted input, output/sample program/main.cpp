#include <iostream>
#include <string>

using namespace std;

string g_sHeader = "  --- Demonstrates Unformatted Input ---";

int main()
{
    string m_sWord;
    string m_sRest;

    cout << g_sHeader << "\n\nPress <return> to go on" << endl;

    cin.get(); // Read the newline without saving.

    cout << "\nPlease enter a sentence with several words!" << "\nEnd with <!> and <return>." << endl;

    cin >> m_sWord;
    getline( cin, m_sRest, '!' ); // Read the rest of the input after the first whitespace until the first '!' character.

    cout << "\nThe first word:  " << m_sWord << "\nRemaining text: " << m_sRest << endl;

    return 0;
}