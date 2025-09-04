num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user which operation to perform
print("Choose operation: +  -  *  /")
operation = input("Enter your choice: ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Show the result
print("Result:", result)