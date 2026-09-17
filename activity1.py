valid_inputs = ["cash", "gcash", "card"]

payment_method = input("Please enter your payment method: ").lower()
if payment_method in valid_inputs:
    print("Valid payment method:", payment_method)
else:
    print("Invalid payment method")