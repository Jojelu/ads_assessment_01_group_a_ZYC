"""
PowerOfTen
"""
while True:
    number = int(input("Please enter a max 3 digit number: \n"))
    if number > 0 and len(str(number)) <= 3:
        break
    if number < 0:
        print("number cannot be negative.")
    else:
        print("number has more than 3 digits.")

if len(str(number)) < 2:
    print(f"{number} = {number} * 1")
elif len(str(number)) == 2:
    print(f"{number} = {number // 10} * 10 + {number % 10} * 1")
else:
    print(f"{number} = {number // 100} * 100 + {number // 10 % 10} * 10 + {number % 10} * 1")




"""
Cash Box
"""
while True:
    to_pay = int(input("Please enter the amount to pay: \n"))
    if to_pay >= 0:
        break                                   #the loop runs until the amount to pay is greater than null
    print("Negative payment is invalid.\n")     #as long as the loop runs, print message

while True:
    received = int(input("Please enter the amount received: \n"))
    if received >= to_pay:    #the loop runs until the received is greater than payment
        break
    if received < 0:          #two cases breaks the loop, received amount negative or less than payment
        print("Negative payment is invalid.\n")
    else:
        print("You did not pay enough.")
if received == to_pay:
    print("Your payment was exact.")
else:
    print("Your change is:", (received - to_pay))