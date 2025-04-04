# Function to calculate the discounted price
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount)

    # Display the result
    if discount >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
