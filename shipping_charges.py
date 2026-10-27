#Austin Hastings
#CMP 131 86520
#Week 7
#Lab 1
#Shipping Charges
#27 OCT 2026
print("-----------------")
print("Fast Freight Shipping")

weight = float(input("Enter the package weight in kilograms: "))

while weight <= 0 or weight >20:
    print("Invalid weight.")
    weight = float(input("Enter the package weight in kilograms: "))

distance = int(input("Enter the shipping distance in miles: "))

while distance <10 or distance > 3000:
    print("Invalid Distance.")
    distance = int(input("Enter the shipping distance in miles: "))

if weight <=2:
    rate = 1.10
elif weight <=6:
    rate = 2.20
elif weight <=10:
    rate = 3.70
else:
    rate = 4.00

shipping = rate * (distance / 500)

print()
print("Shipping Summary")
print("----------------")
print("Package weight: ", weight, "kg")
print("Shipping Distance: ", distance, "miles")
print(f"Rate per 500 miles: ${rate:.2f}")
print(f"Total Shipping Charge: ${shipping:.2f}")