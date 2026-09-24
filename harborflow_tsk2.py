def validate_reference(reference):
    normalized = reference.strip().upper()

    # Rule 1: must be exactly 12 characters
    if len(normalized) != 12:
        return ""

    # Rule 2: hyphens must be in the right spots
    if normalized[3] != "-" or normalized[7] != "-":
        return ""

    prefix = normalized[0:3]
    customer_code = normalized[4:7]
    shipment_number = normalized[8:12]

    # Rule 3: prefix must be HFL
    if prefix != "HFL":
        return ""

    # Rule 4: customer code must be 3 letters
    if not customer_code.isalpha():
        return ""

    # Rule 5: shipment number must be 4 digits
    if not shipment_number.isdigit():
        return ""

    return normalized


def handle_validate_reference():
    reference = input("Booking reference: ")
    result = validate_reference(reference)

    if result != "":
        print("Valid reference:", result)
    else:
        print("Invalid booking reference.") 
if __name__ == "__main__":
    main_task()
