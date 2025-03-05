# Prog10: Print all the numbers between two user-input numbers
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

start = min(num1, num2)
end = max(num1, num2)

for num in range(start + 1, end):
    print(num)
