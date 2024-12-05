import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to the database (replace with your actual database credentials)
db = mysql.connector.connect(user="root", passwd="root", host="localhost", database='Shop')
my_cursor = db.cursor()

# ... (Previous code for database setup)

# GUI setup
root = tk.Tk()
root.title("Sweet Shop Management")

# Create labels and entry fields
cust_name_label = ttk.Label(root, text="Customer Name:")
cust_name_entry = ttk.Entry(root, width=30)
prod_name_label = ttk.Label(root, text="Product Name:")
prod_name_entry = ttk.Entry(root, width=30)
qty_label = ttk.Label(root, text="Quantity:")
qty_entry = ttk.Entry(root, width=10)

# Create buttons
add_button = ttk.Button(root, text="Add Product", command=add_product)
delete_button = ttk.Button(root, text="Delete Product", command=delete_product)
view_button = ttk.Button(root, text="View Products", command=view_products)
invoice_button = ttk.Button(root, text="Create Invoice", command=create_invoice)

# Arrange widgets using grid layout
cust_name_label.grid(row=0, column=0, padx=10, pady=5)
cust_name_entry.grid(row=0, column=1, padx=10, pady=5)
prod_name_label.grid(row=1, column=0, padx=10, pady=5)
prod_name_entry.grid(row=1, column=1, padx=10, pady=5)
qty_label.grid(row=2, column=0, padx=10, pady=5)
qty_entry.grid(row=2, column=1, padx=10, pady=5)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
invoice_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
