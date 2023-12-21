"""
A class named OnlineShop was defined with the class attributes set accordingly:
• Sector to the Value 'electronics'
• sector_code to the value 'ele'
• is_public_company to the value False

Using the builtin deiattrQ function remove the class attribute sector_code. In response, print the rest of the
user-defined OnlineShop class attribute names
"""

class OnlineShop:
    sector= "Electronics"
    sector_code= "ELE"
    is_public_company=False

delattr(OnlineShop, "sector_code")

attrs= [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith("_")]

print(attrs)

"""['sector', 'is_public_company']"""