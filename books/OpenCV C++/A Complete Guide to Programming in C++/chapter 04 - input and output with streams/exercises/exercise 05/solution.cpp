#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
    char    m_char;
    string  m_sWord;

    cout << "Let's go! Press the return key: ";
    cin.get();

    cout    << "Enter a word containing three characters at most: ";
    cin     >> setw( 3 ) >> m_sWord;

    cout << "Your input: " << m_sWord << endl;

    return 0;
}