# Display calculator title
print("=" * 45)
print("ANKUR SMART CALCULATOR v1.0")
print("=" * 45)

# Variable to control repeated calculations
continue_calculation = "yes"

# Main loop for running calculator multiple times
while continue_calculation.lower() == "yes":

    # Display available operations
    print("\nChoose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y)")
    print("7. Exit")

    # Take user's menu choice
    user_choice = input("\nEnter your choice (1-7): ")

    # Exit the calculator
    if user_choice == "7":
        print("\nThank you for using ANKUR SMART CALCULATOR.")
        break

    # Check whether the selected option is valid
    if user_choice in ["1", "2", "3", "4", "5", "6"]:

        # Take two numbers as input
        first_value = float(input("Enter First Number : "))
        second_value = float(input("Enter Second Number: "))

        # Perform Addition
        if user_choice == "1":
            final_result = first_value + second_value
            operation = "+"

        # Perform Subtraction
        elif user_choice == "2":
            final_result = first_value - second_value
            operation = "-"

        # Perform Multiplication
        elif user_choice == "3":
            final_result = first_value * second_value
            operation = "*"

        # Perform Division
        elif user_choice == "4":

            # Prevent division by zero
            if second_value == 0:
                print("\nError : Division by zero is not allowed.")
                continue

            final_result = first_value / second_value
            operation = "/"

        # Perform Modulus
        elif user_choice == "5":

            # Prevent modulus by zero
            if second_value == 0:
                print("\nError : Modulus by zero is not allowed.")
                continue

            final_result = first_value % second_value
            operation = "%"

        # Perform Power calculation
        elif user_choice == "6":
            final_result = first_value ** second_value
            operation = "^"

        # Display the final result
        print("\n-------------------------------")
        print("Calculation Completed Successfully")
        print("-------------------------------")
        print(f"{first_value} {operation} {second_value} = {final_result}")

    else:
        print("\nInvalid Choice! Please select between 1 and 7.")

    # Ask the user whether to continue
    continue_calculation = input("\nDo you want another calculation? (yes/no): ")

# Program finished
print("\nProgram Closed Successfully.")
