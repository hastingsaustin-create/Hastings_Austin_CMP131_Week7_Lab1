#Austin Hastings
#CMP 131 86520
#Week 7
#Lab 1
#Sum of Numbers
#27 OCT 2026

number = int(input("Enter a positive integar: "))

while number <=0:
    print("Invalid number. Number must be greater than zero")
    number = int(input("Enter a positive integer: "))

total = 0

for num in range(1, number + 1):
    total = total + num

print("The sum of the numbers from 1 to", number, "is", total)