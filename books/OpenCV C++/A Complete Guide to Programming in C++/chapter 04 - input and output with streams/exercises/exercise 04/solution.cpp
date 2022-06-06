#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    unsigned int    m_usCode;
    unsigned char   m_ucCode;

    cin >> m_usCode;

    m_ucCode = m_usCode;

    cout << "Character: " << m_ucCode << endl << "Character code (decimal): " << m_usCode << endl << "Character code (octal): " << oct << m_usCode << endl << "Character code (hexadecimal): " << hex << m_usCode;


    while(1);

    return 0;
}