# ==============================================================================
# TASK 8: Make the console resilient (Input Validation Functions)
# ==============================================================================

def get_valid_menu_option(max_option=7):
    """
    Validates main menu selections (1 to max_option).
    """
    while True:
        try:
            choice = int(input("Select service: "))
            if 1 <= choice <= max_option:
                return choice
            else:
                print("Error: Select a service from 1 to 8.")
        except ValueError:
            print("Error: Select a service from 1 to 8.")


def get_valid_positive_float(prompt):
    """
    Validates numeric inputs that must be > 0 (distance, weight, capacity).
    """
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            else:
                print("Error: Value must be greater than zero.")
        except ValueError:
            print("Error: Value must be greater than zero.")


def get_valid_service_code():
    """
    Validates service codes (must be S, X, or P).
    """
    while True:
        code = input("Service code: ").strip().upper()
        if code in ["S", "X", "P"]:
            return code
        print("Error: Service code must be S, X or P.")


def get_valid_non_negative_int(prompt):
    """
    Validates integers that must be >= 0 (minutes, damaged parcels).
    """
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            else:
                print("Error: Value must be non-negative.")
        except ValueError:
            print("Error: Value must be non-negative.")


def get_valid_weekly_deliveries():
    """
    Validates weekly delivery inputs: exactly 7 non-negative integers.
    """
    while True:
        raw_input = input("Completed deliveries: ")
        parts = raw_input.split(",")
        
        if len(parts) != 7:
            print("Error: Weekly report requires 7 delivery counts.")
            continue
            
        valid = True
        for p in parts:
            p_str = p.strip()
            if not p_str.isdigit():
                valid = False
                break
                
        if valid:
            return raw_input
        else:
            print("Error: Weekly report requires 7 delivery counts.")


def get_valid_capacity_weights():
    """
    Validates parcel weight lists for capacity checking (all values > 0).
    """
    while True:
        raw_input = input("Parcel weights (kg): ")
        parts = raw_input.split(",")
        valid = True
        
        for p in parts:
            try:
                w = float(p.strip())
                if w <= 0:
                    valid = False
                    break
            except ValueError:
                valid = False
                break
                
        if valid:
            return raw_input
        else:
            print("Error: Value must be greater than zero.")
