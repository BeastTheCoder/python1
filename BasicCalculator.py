
import random
x = input("What Do You Want As Your First Value? ")
symbol = input("What Math Operation Would You Like? +, -, *, /? ")
y = input("What Do You Want As Your Second Value? ")
if (symbol == "+"):
    print(int(x)+int(y))
elif  (symbol == "-"):
    print(int(x)-int(y))
elif  (symbol == "*"):
    print(int(x)*int(y))
elif (symbol == "/"):
    print(int(x)/int(y))
    