# CLI Calculator
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero not allowed"
    return x / y

print("==== Basic Calculator ====")

while True:
    print("\nChoose operation:")
    print("1 -> Add")
    print("2 -> Subtract")
    print("3 -> Multiply")
    print("4 -> Divide")
    print("0 -> Exit")

    option = input("Enter option: ")

    if option == "0":
        print("Closing calculator... Done 👍")
        break

    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except:
        print("Invalid number entered. Try again.")
        continue

    if option == "1":
        print("Answer =", addition(num1, num2))

    elif option == "2":
        print("Answer =", subtraction(num1, num2))

    elif option == "3":
        print("Answer =", multiplication(num1, num2))

    elif option == "4":
        print("Answer =", division(num1, num2))

    else:
        print("Wrong option selected!")
