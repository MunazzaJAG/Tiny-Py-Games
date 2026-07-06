import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide}

def calculator():
    print(art.calculator_logo)
    no1= eval(input("What's the first number?: "))
    go_on= True

    while go_on:
        for symbol in operations:
            print(symbol)
        choice= input("Pick an operation: ")
        no2= eval(input("What's the second number?: "))

        result= operations[choice](no1, no2)
        print(f"{no1} {choice} {no2} = {result}")

        finish= input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if finish == "y":
            no1= result
        elif finish == "n":
            go_on=False
            print("\n"*20)
            calculator()

calculator()