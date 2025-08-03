# Advanced calculator with error handling and continuous input

while True:
    # 1: input in a natural format
    user_input = input("Enter calculation or type 'exit' to quit: ")


    # 2: Exit condition
    if user_input.lower() == 'exit':
        print("Calculator closed.")
        break

    try:
        # 3: Split input into parts
        parts = user_input.split()
        if len(parts) != 3:
            raise ValueError("Input must be in the format: number operator number (e.g., 3 * 4)")

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        # 4: Perform the operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator. Use +, -, *, or /.")

        # 5: Display and save the result
        output = f"{num1} {operator} {num2} = {result}"
        print("Result:", output)

        # save result to file
        with open("calc_results.txt", "a") as file:
            file.write(output + "\n")

    except Exception as e:
        print("Error:", e)
