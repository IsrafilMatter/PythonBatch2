# Prog07: Print how many of the 10 input numbers are even

numbers = []
for i in range(10):
    num = float(input(f'Enter number {i + 1}: '))
    numbers.append(num)

even_count = sum(1 for num in numbers if num % 2 == 0)

print('Number of even numbers:', even_count)
