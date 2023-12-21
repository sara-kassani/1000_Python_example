"""
A class named OnlineShop was defined with the class attributes set accordingly:

• Sector to the Value 'electronics'
• sector_code to the value 'ele'
• is_public_company to the value False

Display all user-defined OnlineShop class attribute names with their values
"""

class OnlineShop:
    sector="Electronics"
    sector_code="ELE"
    is_public_company=False

for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith("_"):
        print(f"{attr} -> {value}")


"""
sector -> Electronics
sector_code -> ELE
is_public_company -> False
"""