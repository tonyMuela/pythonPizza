print("Welcome to Python Pizza!")
bill= 0

size = (input("What size pizza do you want? S, M, or L: ")).upper()
if size == "L":
    bill += 25
    print("A large pizza is $25")
elif size == "M":
    bill += 20
    print("A Medium pizza is $20")
elif size == "S":
    bill += 15
    print("A Small pizza is $15")
else:
    print("You typed the wrong inputs")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if pepperoni == "Y":
    if size == "S":
        bill += 2
        print("Pepperoni is an additional $2")
    else:
        bill += 3
        print("Pepperoni is an additional $3")

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y":
    bill += 1
    print("Extra cheese is an additional $1")

print(f"Your total bill is ${bill}")
