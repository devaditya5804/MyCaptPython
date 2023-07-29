
num_list = [int(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
positive_numbers = [num for num in num_list if num > 0]

if not positive_numbers:
   print("No positive numbers found in the list.")
else:
   print("Positive numbers in the list:", positive_numbers)

