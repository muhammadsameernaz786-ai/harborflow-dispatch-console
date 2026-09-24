def task_2_function():
    handle_validate_reference()


def task_3_mission():
    # Placeholder for task 3
    print("Running: Calculate delivery quote")


def task_4_function():
    # Placeholder for task 4
    print("Running: Consolidate parcel labels")


def task_5_function():
    # Placeholder for task 5
    print("Running: Check van capacity")


def task_6_function():
    # Placeholder for task 6
    print("Running: Classify service performance")


def task_7_function():
    # Placeholder for task 7
    print("Running: Produce weekly dispatch report")


def main():
    # Task 1: Build the dispatch menu
    while True:
        print("HARBORFLOW DISPATCH CONSOLE")
        print("1. Close console")
        print("2. Validate booking reference")
        print("3. Calculate delivery quote")
        print("4. Consolidate parcel labels")
        print("5. Check van capacity")
        print("6. Classify service performance")
        print("7. Produce weekly dispatch report")
        choice = int(input("Select service: "))

        if choice == 1:
            print("Console closed. Dispatch data remains safe.")
            break  # Ends the while loop, which ends the program
        elif choice == 2:
            task_2_function()
        elif choice == 3:
            task_3_mission()
        elif choice == 4:
            task_4_function()
        elif choice == 5:
            task_5_function()
        elif choice == 6:
            task_6_function()
        elif choice == 7:
            task_7_function()
        else:
            print("Error - Select a service from 1 to 8.")
