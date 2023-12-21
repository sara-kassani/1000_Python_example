"""
A class named OnlineShop was defined with the class attributes set accordingly:

• Sector to the Value 'electronics'
• sector_code to the value 'ele'
• is_public_company to the value False

Using the del statement remove the class attribute named sector_code. In response, print the rest of the userdefined
OnlineShop class attribute names as a list
"""

class OnlineShop:
    sector="Electronics"
    sector_code="ELE"
    is_public_company=False

del OnlineShop.sector_code
attrs=[attr for attr in OnlineShop.__dict__.keys() if not attr.startswith("_")]

print(attrs)

"""['sector', 'is_public_company']"""