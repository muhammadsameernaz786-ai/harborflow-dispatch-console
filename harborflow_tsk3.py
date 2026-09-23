def calculate_quote(distance, weight, service_code):
    #Basic components for the quote and subtotal
    base_charge = 45.00
    distance = float(distance)
    weight = float(weight)
    service_code = service_code.upper()
    
    # Conditions for the service code
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.6
    else:
        print("Invalid service code. Please enter S, X, or P.")
        return None

    # Calculation for subtotal and delivery quote
    subtotal = base_charge + (distance * 6.5) + (weight * 4)
    quote = subtotal * service_multiplier
    return quote

# Printing values for the quote and subtotal
distance = float(input("Distance (km): "))
weight = float(input("Weight (kg): "))
service_code = input("Service code: ")

quote = calculate_quote(distance, weight, service_code)
if quote is not None:
    print(f"Delivery quote: {quote:.2f} SEK")
    





