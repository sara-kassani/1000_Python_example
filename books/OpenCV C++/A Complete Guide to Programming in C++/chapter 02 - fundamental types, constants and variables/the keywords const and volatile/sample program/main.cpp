#include <iostream>

using namespace std;

const double m_cdPi = 3.141593;

int main()
{
    double m_dArea;
    double m_dCircuit;
    double m_dRadius = 1.5;

    m_dArea     = m_cdPi * m_dRadius * m_dRadius;
    m_dCircuit  = 2 * m_cdPi * m_dRadius;

    cout << "\nTo Evaluate a Circle\n" << endl;
    cout << "Radius: " << m_dRadius << endl << "Circumference: " << m_dCircuit << endl << "Area: " << m_dArea << endl;

    return 0;
}