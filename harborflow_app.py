# Started Task 5 ( Checling Van Capacity )

# Created a function named Check Van Capacity

def check_van_capacity():
    capacity = float(input("What is Van Capacity in KG: "))
    weights = input("Enter parcel weights in KG: ").split(",")

    remaining_capacity = capacity
    accepted_count = 0
    loaded_weight = 0

    # Used For Lopp and If-Else statement

    for i in range(len(weights)):
        weight = float(weights[i])

        if weight <= remaining_capacity:
            print(f"Parcel {i + 1}: Accepted")
            accepted_count = accepted_count + 1
            loaded_weight = loaded_weight + weight
            remaining_capacity = remaining_capacity - weight
        else:
            print(f"Parcel {i + 1}: Rejected")

    print(f"Accepted Parcels: {accepted_count}")
    print(f"Loaded Weight: {loaded_weight:.2f} KG")
    print(f"Remaining Capacity: {remaining_capacity:.2f} KG")


check_van_capacity()

# Started Task 6 ( Classify Service Performance )

# Created a function named Classify Performance

def classify_performance(promised, actual, damaged):
    delay = actual - promised

# Using If-Else Statements 

    if damaged > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    return delay, status

# Created another function named Service Performance 

def service_performance():
    promised = int(input("Promised minutes: "))
    actual = int(input("Actual minutes: "))
    damaged = int(input("Damaged parcels: "))

    delay, status = classify_performance(promised, actual, damaged)

    print(f"Delay: {delay} minutes")
    print(f"Service status: {status}")

service_performance()









    




















"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
    """Run the HarborFlow Dispatch Console."""
    # TODO: implement the persistent menu and dispatch to task functions.
    pass


if __name__ == "__main__":
    main()
