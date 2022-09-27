# ASSIGNMENT 2 FILE HANDLING #
# -------------------- w+ in FILE HANDLING ------------------- #
# w+ adds reading file to the existing w mode
with open("command1.txt", 'w+') as hello_w:
    hello_w.write("Hello I'm shyam")
    hello_w.seek(0)
    contents = hello_w.read()
    print(contents)

# ---------------------- r+ in FILE HANDLING -------------------- #
# r+ adds writing to the existing r mode it appends what it writes
with open("command1.txt", 'r+') as hello_w:
    contents = hello_w.read()
    print(contents)
    hello_w.write("\nHello I'm srithi")
    hello_w.seek(0)
    contents = hello_w.read()
    print(contents)
    hello_w.write("\nI'm ok")

# ------------------------- a+ ----------------------- #
# a+ adds the read and write to the existing a mode
with open("command1.txt", 'a+') as hello_w:
    hello_w.write("\nI,m invincible")
    hello_w.seek(0)
    contents = hello_w.read()
    print(contents)
    hello_w.write("\nHello I'm srithi")
    hello_w.seek(0)
    contents = hello_w.read()
    print(contents)
    hello_w.write("\nI'm ok")


# ASSIGNMENT 3 SIMPLE CALCULATOR #

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def squ(n1, n2):
    return n1 ** n2


def file(n1, n2, oper, sol):
    with open("history.txt", "a") as History:
        History.write(f"{n1} {oper} {n2} = {sol}\n")


is_on = True
while is_on:
    on_off = input("do you want to enter the calculator enter 'y' to enter and 'n' to to get out : ").lower()
    if on_off == "y":
        num1 = int(input("enter the first number : "))
        num2 = int(input("enter the second/power number : "))
        operator = input("enter the operator +\\-\\*\\/\\** : ")
        if operator == "+":
            ans = add(num1, num2)
            file(num1, num2, operator, ans)
            print(ans)
        elif operator == "-":
            ans = sub(num1, num2)
            file(num1, num2, operator, ans)
            print(ans)
        elif operator == '*':
            ans = mul(num1, num2)
            file(num1, num2, operator, ans)
            print(ans)
        elif operator == "/":
            ans = div(num1, num2)
            file(num1, num2, operator, ans)
            print(ans)
        elif operator == "**":
            ans = squ(num1, num2)
            file(num1, num2, operator, ans)
            print(ans)
        else:
            print("you have enter a unknown operator pleas enter a valid operator ")
    elif on_off == "n":
        is_on = False
    else:
        print("you have neither switched on or off")
