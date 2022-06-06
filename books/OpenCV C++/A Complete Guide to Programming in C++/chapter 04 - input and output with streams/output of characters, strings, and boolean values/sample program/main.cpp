#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
    int m_iNumber = ' ';
    cout << "The white space code is as follows: " << m_iNumber << endl;

    string m_sPrompt = "\nPlease enter a character followed by <return>: ";
    cout << m_sPrompt;

    char m_char;
    cin >> m_char;

    m_iNumber = m_char;

    cout << "The characters', " << m_char << ", code is: " << m_iNumber << endl << endl;

    cout << "octal" << setw( 12 ) << "decimal" << setw( 12 ) << "hexadecimal" << endl;
    cout << uppercase << oct << m_iNumber << dec << setw( 10 ) << m_iNumber << hex << setw( 8 ) << m_iNumber << endl;

    return 0;
}