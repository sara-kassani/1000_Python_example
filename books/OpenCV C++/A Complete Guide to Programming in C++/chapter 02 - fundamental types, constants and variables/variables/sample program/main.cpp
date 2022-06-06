#include <iostream>

using namespace std;

/* Global variables. */
int g_iVar1;
int g_iVar2 = 2; // Explicit initialization.

int main()
{
    char ch( 'A' ); // Local variable being initialized (or: char ch = 'A';)

    cout << "Value of gVar1: " << g_iVar1 << endl;
    cout << "Value of gVar2: " << g_iVar2 << endl;
    cout << "Character in ch: " << ch << endl;

    /* Local variables with and without initialization. */
    int m_iSum;
    int m_iNumber = 3;

    m_iSum = m_iNumber + 5;

    cout << "Value of sum: " << m_iSum << endl;

    getchar();

    return 0;
}