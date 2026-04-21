import requests

BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("\n--- INVENTORY CLI ---")
    print("1. View all items")
    print("2. Add item")
    print("3. View item by ID")
    print("4. Update item")
    print("5. Delete item")
    print("6. Search product (API)")
    print("0. Exit")


def get_all():
    res = requests.get(f"{BASE_URL}/inventory")
    print(res.json())


def add_item():
    name = input("Product name: ")
    brand = input("Brand: ")
    price = input("Price: ")
    stock = input("Stock: ")

    data = {
        "product_name": name,
        "brand": brand,
        "price": price,
        "stock": stock
    }

    res = requests.post(f"{BASE_URL}/inventory", json=data)
    print(res.json())


def get_one():
    item_id = input("Enter ID: ")
    res = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(res.json())


def update_item():
    item_id = input("Enter ID: ")

    name = input("New name (or press enter): ")
    brand = input("New brand (or press enter): ")
    price = input("New price (or press enter): ")
    stock = input("New stock (or press enter): ")

    data = {}

    if name: data["product_name"] = name
    if brand: data["brand"] = brand
    if price: data["price"] = price
    if stock: data["stock"] = stock

    res = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=data)
    print(res.json())


def delete_item():
    item_id = input("Enter ID: ")
    res = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(res.json())


def search():
    name = input("Enter product name: ")
    res = requests.get(f"{BASE_URL}/search/{name}")
    print(res.json())


while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        get_all()
    elif choice == "2":
        add_item()
    elif choice == "3":
        get_one()
    elif choice == "4":
        update_item()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        search()
    elif choice == "0":
        break
    else:
        print("Invalid choice")