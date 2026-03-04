print("Welcome to the Voting Eligibility Checker!")
name = input('Enter your name:')
age = int (input("Enter your age:"))
if age>=18:
    print(f"You are eligible to vote. Mr. {name}")
else:
    print(f"Hey {name}, you are not eligible to vote yet. Please wait until you turn 18.")
    print("Thank you for using the voting eligibility checker.")