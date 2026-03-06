# Problem 10: Find the sum of all numbers in a list
def sum_of_numbers(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum
# Example usage
numbers_list = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers_list)
print("The sum of the numbers is:", result)