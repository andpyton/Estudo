# Product Inventory Summary

# You are helping a small e-commerce system.
# Each product has information about stock quantity and unit price.
# The data is stored in a dictionary.

# Data

inventory = {
    
        "keyboard":{"quantity": 25, "price": 150.0},     
        "mouse":{"quantity": 60, "price":80.0},
        "monitor":{"quantity":10, "price": 1200.0},
        "headset":{"quantity":8, "price": 300.0}
}

def inventory_summarry():

  low_stock = []

  for key, value in inventory.items():

    print(5*"----")

    total_value = value["quantity"] * value["price"]

    quantity = value["quantity"]

    if quantity<10:

      low_stock.append(key)

    price = value["price"]

    print(f'Products: {key}')
    print(f'Quantity: {quantity}')
    print(f'Price: {price}')
    print(f'Total value: {total_value:.2f}')

  print(4*"-----")

  print("Low stock products: ")

  for item in low_stock:

    print(item)

  
inventory_summarry()



