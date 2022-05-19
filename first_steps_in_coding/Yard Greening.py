broikvmetur = float(input())
cenakvmetri = broikvmetur * 7.61
discount = cenakvmetri * 0.18
discountsum = cenakvmetri - discount

print(f"The final price is: {discountsum} lv.")
print(f"The discount is: {discount} lv.")