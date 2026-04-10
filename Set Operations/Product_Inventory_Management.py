# Function to input a set of products from the user
def input_products(prompt):
    products = input(prompt).strip()
    # Split by commas and strip extra spaces, ignoring empty entries
    product_set = {product.strip() for product in products.split(",") if product.strip()}
    return product_set

# Get dynamic input from user
available_products = input_products("Enter available products (comma-separated): ")
sold_products = input_products("Enter sold products (comma-separated): ")

# Products still in stock (available but not sold)
in_stock = available_products.difference(sold_products)

# Products sold out (available and sold)
sold_out = available_products.intersection(sold_products)

print("\nProducts still in stock:", in_stock)
print("Products that have been sold out:", sold_out)
