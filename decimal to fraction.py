from decimal import Decimal

decimals = [0.25, 0.5, 1.25, 3, 0.6, 0.84]


for d in decimals:
    d = Decimal(str(d))  # Cast as string for proper fraction
    nominator, denominator = d.as_integer_ratio()
    a = nominator
    if denominator == 1:
        print(a)
    else:
        print(nominator, denominator, sep="/")
