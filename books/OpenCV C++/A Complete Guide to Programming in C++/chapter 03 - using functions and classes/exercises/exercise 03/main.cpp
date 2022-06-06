#include <iostream>
#include <string>

using namespace std;

int main()
{
    string m_string1 = "I have learned something new again!";

    cout << m_string1.length() << endl;

    string m_sLine1;
    string m_sLine2;

    getline( cin, m_sLine1 );
    getline( cin, m_sLine2 );

    string m_string2 = m_sLine1 + " * " + m_sLine2;

    cout << m_string2;

    return 0;
}