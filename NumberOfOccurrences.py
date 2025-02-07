"""Flowchart to find the number of occurrences of each digit in numbers entered from the screen, with
a maximum of 8 digits."""

number=input("Enter Numbers max of 8 digits:")
if not number.isdigit() or len(number)>8:
    print("Invalid login.Please enter a positive integer of up to 8 digits.")
    return
digit_counter={str(i): 0 for i in range(10)}
for digit in number:
    digit_counter[digit] += 1
print("Amount of digits: ")
for digit,amount in digit_counter.items():
    if amount>0:
        print(f"{digit}:{amount} amount")