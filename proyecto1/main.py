import os

products = [
  {"name": "Diamond ring", "price": 1000, "quantity": 5},
  {"name": "Quartz ring", "price": 50, "quantity": 8},
  {"name": "Gold ring", "price": 600, "quantity": 12},
  {"name": "Silver ring", "price": 400, "quantity": 5}
]
cart = []

def clear_screen():
    os.system('clear')  
        

def show_products():
  clear_screen()
  print(" --------------------- Menu (products) ------------------------")
  for i, product in enumerate(products):
    print(f"{i+1}. {product["name"]} - price ${product["price"]} - quantity {product["quantity"]}")
  

def add_to_cart():
  clear_screen()
  show_products()
  try:
    option = int(input("Enter the product number you wish to add to the cart: "))
    if 1 <= option <= len (products):
      quantity = int(input("Enter the quantity of products you wish to buy: "))
      product = products[option - 1]
      if quantity > product ["quantity"]:
        print("Not enough stock available")
      else:
        products[option - 1]['quantity'] -= quantity
        cart.append({"name": product["name"], "price": product['price'], "quantity": quantity})
        print(f"Congratulations, you have successfully added {quantity} {product["name"]}(s)")
  except Exception as e:
    print("An error has occurred", e)

def show_cart():
  clear_screen()
  if cart:
    print("Shopping Cart.")
    for i, item in enumerate(cart,1):
      print(f"{i}. product: {item['name']} - ${item['price']} - quantity: {item['quantity']}")
  else:
    print("The cart is empty")

def calcular_total():
  total = sum(item["price"] * item["quantity"] for item in cart)
  print(f"he total amount to pay is = ${total}")

def checkout():
  clear_screen()
  show_cart()
  if cart:
    calcular_total()
    confirmar = input("Would you like to finalize the purchase? (y/n): ")

    if confirmar.lower() == "y":
        cart.clear()
        print("Purchase completed successfully")
    else:
        print("Purchase canceled")
  else:
      print("No items in the cart")

def main():
  while True: 
    clear_screen()
    print(" ------------------ Menu (jewelry) ----------------------")
    print("1. Show available products")
    print("2. Add products to cart")
    print("3. Show cart")
    print("4. Checkout")
    print("5. Exit")
    
    try:
      options = {
        1: show_products,
        2: add_to_cart,
        3: show_cart,
        4: checkout,
      }

      selecion = int(input("Enter option:"))

      if selecion in options:
        options[selecion]()
        input("Press Enter to continue...")
      elif selecion == 5:
        break

    except ValueError:
      print("Invalid input, please enter a number ")
      input("Press Enter to continue...")
    except Exception:
      print("An error has occurred")
      input("Press Enter to continue...")


main()