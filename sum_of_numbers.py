numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("Sum:", total)

values = input("Enter numbers separated by space: ")
numbers = [int(n) for n in values.split()]
print("Sum:", sum(numbers))
