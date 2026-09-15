Problem 4:
while True:
    Pin = input("Enter your PIN number: ").strip()


    if not Pin.isdigit():
        print("Enter a valid PIN")
    elif len(Pin) != 4:
        print("Enter a valid PIN")
    else:
        break
   
print(f"Successful {Pin}")    

Problem 5:
Code = input("Enter secret code: ").strip().upper()


first_four = Code[0:4]
last_four = Code[-4:]
middle = len(Code)//2


replace = Code.replace("-", "*")


print(f"First four: {first_four}")
print(f"Last four: {last_four}")
print(f"Middle character: {Code[middle]}")
print(f"Replace: {replace}")

Problem 6:
total = 0
receipt_lines = ""


while True:
    item = input("Enter an item name: ").strip()
   
    if item != "done":
        price = float(input("Enter a price: "))
        total += price
        receipt_lines += f"{item:<20} ${price:>8.2f}\n"
        #print(f"{item:<10} ${price:>.2f}")
    else:
        break


print(receipt_lines, end="")
print(f"Total: ${total:>.2f}")

