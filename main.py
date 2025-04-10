def calculate(text_input):
    # We first of all extract the indices of two numbers and the operator from the user
    number1 = int(text_input[0]) # index of the first digit
    number2 = int(text_input[2]) # index of the second digit
    operator = text_input[1]     # index of the operator

    # We then perform the calculation depending on the operator the user inputs and return the result
    if operator == "+":
        return number1 + number2
    elif operator == "*":
        return number1 * number2
    elif operator == "-":
        return number1 - number2
    elif operator == "/":
        return number1 / number2
    elif operator == "~":
        quotient = number1 // number2 # To get the integer division
        remainder = number1 % number2 # To get the remainder after the division
        return f"{quotient}\nThe remainder is {remainder}" # In order not to prepend the string "The answer is" to the print statement in the main function, we return just {quotient}. We add \n to get a new line for the value of remainder

# Here we define the main function and ask the user how many calculations they want to perform
def main():
    print("Welcome to the Python calculator!")
    number_of_calculations = int(input("How many calculations do you want to do? "))

    # We loop through the calculation a specific number of times based on the user input
    for i in range(number_of_calculations):
        user_input = input("What do you want to calculate? ")
        # we call the calculate function and display the result in a formatted print statement
        result = calculate(user_input)
        print(f"The answer is {result}")

if __name__ == "__main__":
    main()