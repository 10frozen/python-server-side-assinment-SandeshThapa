# Parse a JSON file representing product details (name, price, quantity) and display the details in tabular format.
import json
data = []
number_of_products = int(input("Enter the number of products: "))
print("\n")

print("Enter Product Details: \n")
for i in range(1, number_of_products+1):
    name = input(f"Enter Product Name {i}: ")
    price = float(input(f"Enter Price of the Product {i}: "))
    quantity = int(input(f"Enter Quantity of the Product {i}: "))
    print("\n")
    
    product ={
    "name": name,
    "price": price,
    "quantity": quantity
    }
    data.append(product)

with open("products.json", "w") as file:
    json.dump(data, file, indent =4)

print("Data written successfully.")

with open("products.json", "r") as file:
    product_data = json.load(file)

if not product_data:
    print("No product data found.")

print(f"{'Product Name':<15}{'Price':<10}{'Quantity':10}")
print("-" * 35)

for data in product_data:
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    print(f"{name:<15}{price:<10}{quantity:<10}")