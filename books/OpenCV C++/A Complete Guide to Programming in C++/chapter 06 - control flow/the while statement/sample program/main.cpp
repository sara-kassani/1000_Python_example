#include <iostream>

using namespace std;

int main()
{
    int     m_iX;
    int     m_iCount    = 0;
    float   m_fSum      = 0.0;

    cout << "Please enter some integers:\n" << "(Break with any letter)" << endl;

    while ( cin >> m_iX )
    {
        m_fSum += m_iX;
        ++m_iCount;
    }

    cout << "The average of the numbers: " << m_fSum / m_iCount << endl;

    return 0;
}