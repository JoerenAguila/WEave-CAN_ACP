import random

# user class and subclasses represent different user types, e.g., Weaver
class User:
    def __init__(self, name):
        self.name = name
    
    def get_user_name(self):
        return self.name

class Weaver(User):
    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id
        self.order_history = []  # store orders for history tracking
    
    def get_user_type(self):
        return "Weaver"
    
    def view_order_history(self):
        if not self.order_history:
            print(f"No orders found for {self.name}.")
        else:
            print(f"\n{self.name}'s Order History:")
            for order in self.order_history:
                order.display_order()

    def cancel_order(self, order_id):
        for order in self.order_history:
            if order.order_id == order_id and order.status == "Pending":
                order.status = "Cancelled"
                print(f"Order {order_id} has been cancelled.")
                break
        else:
            print("Order not found or already processed.")

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.sales_reports = []  #store sales reports
    
    def get_user_type(self):
        return "Admin"
    
    def generate_best_seller_report(self, inventory):
        best_selling_product = max(inventory, key=lambda p: p.total_sales)
        print(f"\nBest Selling Product: {best_selling_product.name} with ${best_selling_product.total_sales:.2f} in sales.")
    
    def generate_least_seller_report(self, inventory):
        least_selling_product = min(inventory, key=lambda p: p.total_sales)
        print(f"\nLeast Selling Product: {least_selling_product.name} with ${least_selling_product.total_sales:.2f} in sales.")
    
    def apply_sale(self, inventory, product_name, discount_percent):
        for product in inventory:
            if product.name.lower() == product_name.lower():
                product.apply_sale(discount_percent)
                print(f"Sale applied to {product.name}. New price: ${product.price:.2f}")
                break
        else:
            print(f"Product {product_name} not found in inventory.")

# product class and subclasses define products with price, stock, material, and pattern
class Product:
    VALID_MATERIALS = {"cotton", "abaca", "fibres", "pineapple"}
    VALID_PATTERNS = {"bayawak", "binakul", "binituwon", "bunga-sama", "palipattang", "tinaggu"}

    def __init__(self, name, price, stock, material, pattern):
        # validate material and pattern, convert to lowercase for consistent checks
        if (material := material.lower()) not in self.VALID_MATERIALS:
            raise ValueError(f"Invalid material '{material}'. Choose from {self.VALID_MATERIALS}.")
        if (pattern := pattern.lower()) not in self.VALID_PATTERNS:
            raise ValueError(f"Invalid pattern '{pattern}'. Choose from {self.VALID_PATTERNS}.")
        
        self.name = name
        self.price = price
        self.stock = stock
        self.material = material.capitalize()
        self.pattern = pattern.capitalize()
        self.total_sales = 0  # track total sales for this product
    
    def display_details(self, product_number):
        print(f"{product_number:<3} {self.name:<15} ${self.price:<8.2f} {self.stock:<6} {self.material:<10} {self.pattern:<12}")

    def apply_sale(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        self.price -= discount_amount  # apply discount to the price

    def update_sales(self, quantity):
        self.total_sales += self.price * quantity  # update the total sales with this order's value

class Order:
    def __init__(self, product, quantity, customer_name, customer_id, contact_number):
        self.product = product
        self.quantity = quantity
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.contact_number = contact_number
        self.status = "Pending"
        self.amount = product.price * quantity
        self.order_id = random.randint(1000, 9999)  # random order ID
    
    def display_order(self):
        print("\nOrder Details:")
        print(f"Order ID     : {self.order_id}")
        print(f"Product      : {self.product.name} ({self.product.material}, {self.product.pattern})")
        print(f"Quantity     : {self.quantity}")
        print(f"Total Amount : ${self.amount:.2f}")
        print(f"Customer     : {self.customer_name}")
        print(f"Customer ID  : {self.customer_id}")
        print(f"Contact      : {self.contact_number}")
        print(f"Status       : {self.status}")

# inventory management and order history
def view_inventory(inventory):
    print("\nInventory:")
    print(f"{'No.':<3} {'Product':<15} {'Price':<10} {'Stock':<6} {'Material':<10} {'Pattern':<12}")
    print("-" * 55)
    for i, product in enumerate(inventory, start=1):
        product.display_details(i)
    print("-" * 55)

def create_order(inventory, orders, customer):
    print("\nEnter the number of the product to order:")
    view_inventory(inventory)
    
    try:
        product_number = int(input("\nSelect product number: ")) - 1
        if product_number not in range(len(inventory)):
            print("Invalid product number.")
            return

        product = inventory[product_number]
        quantity = int(input("Enter quantity: "))
        
        if quantity > product.stock:
            print("Insufficient stock!")
            return
        
        customer_name = input("Enter customer name: ")
        customer_id = int(input("Enter customer ID: "))
        contact_number = input("Enter contact number: ")

        new_order = Order(product, quantity, customer_name, customer_id, contact_number)
        orders.append(new_order)
        customer.order_history.append(new_order)  # add to the customer's order history
        product.stock -= quantity
        product.update_sales(quantity)  # update product sales
        print("\nOrder created successfully!")

    except ValueError:
        print("Invalid input. Please enter valid numbers for product selection and quantity.")

def admin_panel(inventory, orders, customers):
    print("\nAdmin Panel:")
    print("1. View Inventory\n2. View Orders\n3. Add New Product\n4. Generate Best Seller Report\n5. Generate Least Seller Report\n6. Apply Sale to Product\n7. Back to Main Menu")
    admin_choice = input("Choose an option: ")
    
    if admin_choice == '1':
        view_inventory(inventory)
    elif admin_choice == '2':
        view_orders(orders)
    elif admin_choice == '3':
        add_product(inventory)
    elif admin_choice == '4':
        admin.generate_best_seller_report(inventory)
    elif admin_choice == '5':
        admin.generate_least_seller_report(inventory)
    elif admin_choice == '6':
        product_name = input("Enter product name: ")
        discount_percent = float(input("Enter discount percentage: "))
        admin.apply_sale(inventory, product_name, discount_percent)
    elif admin_choice == '7':
        return
    else:
        print("Invalid choice, please try again.")

def add_product(inventory):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    material = input("Enter material: ")
    pattern = input("Enter pattern: ")
    
    new_product = Product(name, price, stock, material, pattern)
    inventory.append(new_product)
    print(f"\n{new_product.name} added successfully!")  # fixed missing closing quote

#main function
def main():
    # sample inventory with various products
    inventory = [
        Product("Shawl", 30.0, 10, "Cotton", "Bayawak"),
        Product("Bag", 20.0, 20, "Abaca", "Binakul"),
        Product("Shawl", 35.0, 15, "Pineapple", "Bunga-sama"),
        Product("Bag", 25.0, 25, "Fibres", "Palipattang"),
        Product("Face Mask", 5.0, 50, "Cotton", "Binituwon"),
        Product("Hairband", 8.0, 30, "Fibres", "Tinaggu"),
        Product("Pants", 40.0, 12, "Cotton", "Bayawak"),
        Product("Skirt", 45.0, 18, "Abaca", "Binakul"),
        Product("Shirt", 25.0, 22, "Pineapple", "Binituwon"),
    ]
    
    orders = []
    customers = [Weaver("Alice", 1), Admin("Bob")]
    global admin
    admin = customers[1]  #assign the admin object
    
    while True:
        print("\nWelcome to WEave CAN - Inventory and Order Management System for Filipino Weavers")
        print("\nWeave got it all for you!")
        print("1. View Inventory\n2. Create Order\n3. View Orders\n4. Admin Panel\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_inventory(inventory)
        elif choice == '2':
            create_order(inventory, orders, customers[0])  # example using the first customer
        elif choice == '3':
            customers[0].view_order_history()
        elif choice == '4':
            admin_panel(inventory, orders, customers)
        elif choice == '5':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
