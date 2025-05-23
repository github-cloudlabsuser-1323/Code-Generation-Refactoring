def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide, quit")
    while True:
        op = input("Enter operation: ").strip().lower()
        if op == "quit":
            print("Exiting calculator.")
            break
        if op not in ("add", "subtract", "multiply", "divide"):
            print("Invalid operation.")
            continue
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if op == "add":
            result = add(x, y)
        elif op == "subtract":
            result = subtract(x, y)
        elif op == "multiply":
            result = multiply(x, y)
        elif op == "divide":
            result = divide(x, y)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()