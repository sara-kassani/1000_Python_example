#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int     m_iArticleNumber;
    int     m_iArticleQuantity;
    double  m_iArticlePrice;

    cin >> m_iArticleNumber >> m_iArticleQuantity >> m_iArticlePrice;

    cout << setw( 20 ) << "Article Number" << setw( 20 ) << "Number of Pieces" << setw( 20 ) << "Price per piece" << endl;
    cout << setw( 13 ) << m_iArticleNumber << setw( 15 ) << m_iArticleQuantity << setw( 15 ) << m_iArticlePrice << " Dollar";

    return 0;
}