#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
    string m_sLabel;
    double m_dPrice;

    cout    << "Please enter an article label: ";
    cin     >> setw( 16 ) >> m_sLabel; // Set the maximum field width (16).

    cin.sync();     // Clear the buffer.
    cin.clear();    // Reset any set error flags.

    cout    << "\nEnter the price of the article: ";
    cin     >> m_dPrice;

    cout << fixed << setprecision( 2 ) << "\nArticle:" << "\n  Label:  " << m_sLabel << "\n  Price:  " << m_dPrice << endl;

    return 0;
}