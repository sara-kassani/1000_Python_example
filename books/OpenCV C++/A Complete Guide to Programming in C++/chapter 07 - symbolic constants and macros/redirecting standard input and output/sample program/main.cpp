#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
    string  m_szLine;
    int     m_iNumber = 0;

    while ( getline( cin, m_szLine ) )
    {
        cout << setw( 5 ) << ++m_iNumber << m_szLine << endl;
    }

    return 0;
}