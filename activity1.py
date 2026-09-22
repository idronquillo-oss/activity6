valid_inputs = ["cash", "gcash", "card"]

payment_method = input("Enter payment method: ").lower()

if payment_method in valid_inputs:
    print("Valid payment method.")
else:
    print("Invalid payment method.")