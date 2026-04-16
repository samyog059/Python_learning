product = input("Enter the name of the product: ")
quantity = int(input("Enter the quantity: "))
price_per_unit = float(input("Enter the price per unit: "))
total_cost = quantity * price_per_unit
print(f"The total cost of {quantity} {product}(s) is: ${total_cost:.2f}")