import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
            messagebox.showinfo("Order History", f"No orders found for {self.name}.")
        else:
            order_details = f"{self.name}'s Order History:\n"
            for order in self.order_history:
                order_details += f"\nOrder ID: {order.order_id}, Product: {order.product.name}, Quantity: {order.quantity}, Total: ${order.amount:.2f}"
            messagebox.showinfo("Order History", order_details)

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.sales_reports = []  # Store sales reports
    
    def get_user_type(self):
        return "Admin"
    
    def generate_best_seller_report(self, inventory):
        best_selling_product = max(inventory, key=lambda p: p.total_sales)
        messagebox.showinfo("Best Seller Report", f"Best Selling Product: {best_selling_product.name} with ${best_selling_product.total_sales:.2f} in sales.")
    
    def generate_least_seller_report(self, inventory):
        least_selling_product = min(inventory, key=lambda p: p.total_sales)
        messagebox.showinfo("Least Seller Report", f"Least Selling Product: {least_selling_product.name} with ${least_selling_product.total_sales:.2f} in sales.")
    
    def apply_sale(self, inventory, product_name, discount_percent):
        for product in inventory:
            if product.name.lower() == product_name.lower():
                product.apply_sale(discount_percent)
                messagebox.showinfo("Sale Applied", f"Sale applied to {product.name}. New price: ${product.price:.2f}")
                break
        else:
            messagebox.showerror("Error", f"Product {product_name} not found in inventory.")

class Product:
    VALID_MATERIALS = {"cotton", "abaca", "fibres", "pineapple"}
    VALID_PATTERNS = {"bayawak", "binakul", "binituwon", "bunga-sama", "palipattang", "tinaggu"}

    def __init__(self, name, price, stock, material, pattern):
        if (material := material.lower()) not in self.VALID_MATERIALS:
            raise ValueError(f"Invalid material '{material}'. Choose from {self.VALID_MATERIALS}.")
        if (pattern := pattern.lower()) not in self.VALID_PATTERNS:
            raise ValueError(f"Invalid pattern '{pattern}'. Choose from {self.VALID_PATTERNS}.")
        
        self.name = name
        self.price = price
        self.stock = stock
        self.material = material.capitalize()
        self.pattern = pattern.capitalize()
        self.total_sales = 0  # Track total sales for this product
    
    def apply_sale(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        self.price -= discount_amount

    def update_sales(self, quantity):
        self.total_sales += self.price * quantity

class Order:
    def __init__(self, product, quantity, customer_name, customer_id, contact_number):
        self.product = product
        self.quantity = quantity
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.contact_number = contact_number
        self.status = "Pending"
        self.amount = product.price * quantity
        self.order_id = random.randint(1000, 9999)

    def display_order(self):
        return f"Order ID: {self.order_id}, Product: {self.product.name}, Quantity: {self.quantity}, Total: ${self.amount:.2f}"

def create_order(inventory, orders, customer):
    def submit_order():
        try:
            product_number = int(product_number_entry.get()) - 1
            if product_number not in range(len(inventory)):
                messagebox.showerror("Error", "Invalid product number.")
                return
            product = inventory[product_number]
            quantity = int(quantity_entry.get())
            
            if quantity > product.stock:
                messagebox.showerror("Error", "Insufficient stock!")
                return
            
            customer_name = customer_name_entry.get()
            customer_id = int(customer_id_entry.get())
            contact_number = contact_number_entry.get()

            new_order = Order(product, quantity, customer_name, customer_id, contact_number)
            orders.append(new_order)
            customer.order_history.append(new_order)
            product.stock -= quantity
            product.update_sales(quantity)
            messagebox.showinfo("Order Created", f"Order created successfully! Order ID: {new_order.order_id}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    create_order_window = tk.Toplevel()
    create_order_window.title("Create Order")

    # Table to display products
    tree = ttk.Treeview(create_order_window, columns=("No.", "Product", "Price", "Stock", "Material", "Pattern"), show="headings")
    tree.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    tree.heading("No.", text="No.")
    tree.heading("Product", text="Product")
    tree.heading("Price", text="Price")
    tree.heading("Stock", text="Stock")
    tree.heading("Material", text="Material")
    tree.heading("Pattern", text="Pattern")

    for i, product in enumerate(inventory, start=1):
        tree.insert("", "end", values=(i, product.name, f"${product.price:.2f}", product.stock, product.material, product.pattern))

    tk.Label(create_order_window, text="Select Product Number:").grid(row=1, column=0, pady=5)
    product_number_entry = tk.Entry(create_order_window)
    product_number_entry.grid(row=1, column=1, pady=5)

    tk.Label(create_order_window, text="Enter Quantity:").grid(row=2, column=0, pady=5)
    quantity_entry = tk.Entry(create_order_window)
    quantity_entry.grid(row=2, column=1, pady=5)

    tk.Label(create_order_window, text="Customer Name:").grid(row=3, column=0, pady=5)
    customer_name_entry = tk.Entry(create_order_window)
    customer_name_entry.grid(row=3, column=1, pady=5)

    tk.Label(create_order_window, text="Customer ID:").grid(row=4, column=0, pady=5)
    customer_id_entry = tk.Entry(create_order_window)
    customer_id_entry.grid(row=4, column=1, pady=5)

    tk.Label(create_order_window, text="Contact Number:").grid(row=5, column=0, pady=5)
    contact_number_entry = tk.Entry(create_order_window)
    contact_number_entry.grid(row=5, column=1, pady=5)

    submit_button = tk.Button(create_order_window, text="Submit Order", command=submit_order)
    submit_button.grid(row=6, columnspan=2, pady=10)

def show_inventory(inventory):
    inventory_window = tk.Toplevel()
    inventory_window.title("Inventory")

    tree = ttk.Treeview(inventory_window, columns=("No.", "Product", "Price", "Stock", "Material", "Pattern"), show="headings")
    tree.grid(row=0, column=0, pady=10, padx=10)

    tree.heading("No.", text="No.")
    tree.heading("Product", text="Product")
    tree.heading("Price", text="Price")
    tree.heading("Stock", text="Stock")
    tree.heading("Material", text="Material")
    tree.heading("Pattern", text="Pattern")

    for i, product in enumerate(inventory, start=1):
        tree.insert("", "end", values=(i, product.name, f"${product.price:.2f}", product.stock, product.material, product.pattern))

def show_orders(orders):
    order_window = tk.Toplevel()
    order_window.title("Order List")
    
    tree = ttk.Treeview(order_window, columns=("Order ID", "Product", "Quantity", "Customer Name", "Customer ID", "Contact", "Total", "Status"), show="headings")
    tree.grid(row=0, column=0, pady=10, padx=10)
    
    tree.heading("Order ID", text="Order ID")
    tree.heading("Product", text="Product")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Customer Name", text="Customer Name")
    tree.heading("Customer ID", text="Customer ID")
    tree.heading("Contact", text="Contact")
    tree.heading("Total", text="Total")
    tree.heading("Status", text="Status")
    
    for order in orders:
        tree.insert("", "end", values=(
            order.order_id, order.product.name, order.quantity, 
            order.customer_name, order.customer_id, 
            order.contact_number, f"${order.amount:.2f}", order.status
        ))

    tk.Button(order_window, text="Close", command=order_window.destroy).grid(row=1, column=0, pady=10)

def admin_panel(inventory, orders, customers):
    admin = customers[1]
    admin_window = tk.Toplevel()
    admin_window.title("Admin Panel")

    tk.Button(admin_window, text="Generate Best Seller Report", command=lambda: admin.generate_best_seller_report(inventory)).grid(row=0, pady=10)
    tk.Button(admin_window, text="Generate Least Seller Report", command=lambda: admin.generate_least_seller_report(inventory)).grid(row=1, pady=10)
    tk.Button(admin_window, text="Apply Sale", command=lambda: admin.apply_sale(inventory, "Shawl", 10)).grid(row=2, pady=10)

def main():
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
    admin = customers[1]

    root = tk.Tk()
    root.title("WEave CAN - Inventory and Order Management System")
    root.geometry("600x500")

    tk.Label(root, text="Welcome to WEave CAN", font=("Helvetica", 18)).pack(pady=20)
    tk.Label(root, text="Weave got it all for you", font=("Helvetica", 12)).pack(pady=5)

    def show_inventory_gui():
        show_inventory(inventory)

    def create_order_gui():
        create_order(inventory, orders, customers[0])

    def admin_panel_gui():
        admin_panel(inventory, orders, customers)

    tk.Button(root, text="View Inventory", width=20, command=show_inventory_gui).pack(pady=10)
    tk.Button(root, text="Create Order", width=20, command=create_order_gui).pack(pady=10)
    tk.Button(root, text="View Orders", width=20, command=lambda: show_orders(orders)).pack(pady=10)
    tk.Button(root, text="Admin Panel", width=20, command=admin_panel_gui).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
