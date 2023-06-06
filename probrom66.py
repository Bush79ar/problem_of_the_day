bill = int(input("Enter bill amount:"))
discount = int(input("Enter discount percentage:"))
output = bill - (bill * discount / 100)
print("The price after the discount is ", output)