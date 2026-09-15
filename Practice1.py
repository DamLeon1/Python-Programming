Problem 1:
height = int(input("Enter height in inches: "))
age = int(input("Enter age: "))


if height >= 48 and age >= 10:
    print("You are able to ride")
else:
    print("Can't ride, need to be taller and older")

Problem 2:
total = float(input("What is your total purchase amount: "))
vip = input("Do you have a VIP membership card (Yes/NO): ")


if vip == 'No' and total <= 100:
    print(f"No discount final price is {total}")
elif total > 100 and vip == 'Yes':
    sum = total * .8
    print(f"Discount of 20 percent of total purchase {sum}")
elif (total > 100 and vip == 'No') or (vip == 'Yes' and total <= 100):
    sum = total * .9
    print(f"Discount of 10 percent of total purchase {sum}")
else:
    print("Error")

Problem 3:
age = int(input("Enter age: "))
week = input("Is it a weekend (Yes/No): ")


if age < 5 and week == 'Yes':
    price = 0
    print(f"Price = {price}$")
elif age >= 5 and age <= 17 and week == 'Yes':
    price = 11
    print(f"Price = {price}$")
elif age >= 18 and age <= 64 and week == 'Yes':
    price = 15
    print(f"Price = {price}$")
elif age >= 65 and week == 'Yes':
    price = 12
    print(f"Price = {price}$")
elif age < 5:
    price = 0
    print(f"Price = {price}$")
elif age >= 5 and age <= 17:
    price = 8
    print(f"Price = {price}$")
elif age >= 18 and age <= 64:
    price = 12
    print(f"Price = {price}$")
elif age >= 65:
    price = 9
    print(f"Price = {price}$")
else:
    print("Error")


special = "Qualified" if price < 10 else "Not Qualified"
print(f"Matinee Special: {special}")

Cleaner Problem 3: 
age = int(input("Enter age: "))
week = input("Is it a weekend (yes/no): ").strip().lower()

if age < 5:
    price = 0
elif age <= 17:  # No need for age >= 5 because the 'if' caught anything under 5!
    price = 8
elif age <= 64:  # No need for age >= 18 because the previous block caught them
    price = 12
else:
    price = 9

# Step 2: Add weekend surcharge if applicable
if week == 'yes' and price > 0:
    price += 3  # This is the same as: price = price + 3

print(f"Price = {price}$")

special = "Qualified" if price < 10 else "Not Qualified"
print(f"Matinee Special: {special}")
