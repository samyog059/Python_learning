# Bill split program to 4 friends
# Get the total bill amount from the user
total_bill = float(input("Enter the total bill amount: "))
# Calculate the amount each friend has to pay
amount_per_friend = total_bill / 4
# Display the amount each friend has to pay
print("Each friend has to pay: $" + str(round(amount_per_friend, 2)))
