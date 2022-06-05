# exercise 57: Cell Phone Bill

minutes = int(input('enter number of minutes: '))
messages = int(input('enter number of text messages: '))

if minutes > 50:
    extra_mins = minutes - 50
else:
    extra_mins = 0
if messages > 50:
    extra_text = messages - 50
else:
    extra_text = 0

base_charge = 15
included_mins = 50
included_text = 50
cost_of_extra_mins = 0.25
cost_of_extra_text = 0.15
additional_charge = 0.44
tax_rate = 0.05
total_charge = (base_charge + additional_charge) + (extra_mins * cost_of_extra_mins) + (extra_text * cost_of_extra_text)
tax_amount = tax_rate * total_charge
final_bill = total_charge + tax_amount

print()
print("base charge: $%.2f" % base_charge)
print("911 fee: $%.2f" % additional_charge)
print("taxes: $%.2f" % tax_amount)

if extra_mins:
    print("%d extra minutes cost: $%.2f" % (extra_mins, extra_mins * cost_of_extra_mins))
if extra_text:
    print("%d extra messages cost: $%.2f" % (extra_text, extra_text * cost_of_extra_text))
print("FINAL BILL: $%.2f" % final_bill)

