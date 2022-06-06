#include <iostream>
#include <string>

using namespace std;

int main()
{
    string message ( "\nLearn from your mistakes!" );

    cout << message << endl;

    int m_iLen = message.length();

    cout << "Length of the string: " << m_iLen << endl;

    srand( 12 );

    int b = rand();

    cout << "\nRandom number: " << b << endl;

    return 0;
}