#CustomerOrderProcessing

orders = [("Alice", "Laptop", 1), ("Bob", "Camera", 2)]

def process_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"Order: {customer_name} ordered {quantity} {product}(s).")

# Example usage:
process_orders(orders)