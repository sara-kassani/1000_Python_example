"""
Implement a function called dispiay_info() which prints the name of the company and
if the user also passes an argument named price , it prints the price
"""

def display_info(company, **kwargs):
    print(f"Company name: {company}")
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}")


display_info(company="AI BioTech", price=5000)

"""
Company name: AI BioTech
Price: $ 5000
"""