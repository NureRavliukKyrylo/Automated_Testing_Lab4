from calculator import Calculator

def main():
    calculator = Calculator()

    while True:
        print("\nAvailable operations:")
        print("+, -, *, /")
        print("Type 'exit' to quit")
        
        operation = input("Enter operation: ").strip()
        if operation.lower() == 'exit':
            print("Exiting calculator")
            break

        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please enter one of (+, -, *, /)")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
            
        try:
            if operation == '+':
                result = calculator.add(num1, num2)
            elif operation == '-':
                result = calculator.subtract(num1, num2)
            elif operation == '*':
                result = calculator.multiply(num1, num2)
            elif operation == '/':
                result = calculator.divide(num1, num2)
            print(f"Result: {num1} {operation} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
