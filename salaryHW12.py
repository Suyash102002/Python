salary = 800000
if salary <= 500000:
    tax_rate = 0.05
    tax = salary*tax_rate
    print(f"The tax rate is 0.05%. Tax amount is {tax}")
elif salary <= 1000000:
    tax_rate = 0.10
    tax = salary*tax_rate
    print(f"The tax rate is 0.10%. Tax amount is {tax}")
else:
    tax_rate = 0.20
    tax = salary*tax_rate
    print(f"The tax rate is 0.20%. Tax amount is {tax}")