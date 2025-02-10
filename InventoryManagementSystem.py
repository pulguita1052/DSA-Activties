class Inventory:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def get_categories(self):
        return self.categories

    def find_category(self, name):
        for category in self.categories:
            if category.name == name:
                return category
        return None


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def remove_product(self, product):
        self.products.remove(product)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name= {self.name}, price= ${self.price}, quantity= {self.quantity})"


def create_inventory():
    return Inventory()


def print_inventory(inventory):
    for category in inventory.get_categories():
        print(f"Category: {category.name}")
        for product in category.get_products():
            print(f"  {product}")


def menu():
    inventory = create_inventory()
    while True:
        print("\nMenu:")
        print("1. Add Category")
        print("2. Add Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Show Inventory")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter the category name: ")
            category = Category(category_name)
            inventory.add_category(category)

        elif choice == "2":
            category_name = input("Enter the category name: ")
            category = inventory.find_category(category_name)
            if category:
                product_name = input("Enter the product name: ")
                price = float(input(f"Enter the price for '{product_name}': "))
                quantity = int(input(f"Enter the quantity for '{product_name}': "))
                product = Product(product_name, price, quantity)
                category.add_product(product)
            else:
                print("Category not found.")

        elif choice == "3":
            category_name = input("Enter the category name: ")
            category = inventory.find_category(category_name)
            if category:
                product_name = input("Enter the product name: ")
                product = category.find_product(product_name)
                if product:
                    new_price = float(input(f"Enter the new price for '{product_name}': "))
                    new_quantity = int(input(f"Enter the new quantity for '{product_name}': "))
                    product.price = new_price
                    product.quantity = new_quantity
                else:
                    print("Product not found.")
            else:
                print("Category not found.")

        elif choice == "4":
            category_name = input("Enter the category name: ")
            category = inventory.find_category(category_name)
            if category:
                product_name = input("Enter the product name: ")
                product = category.find_product(product_name)
                if product:
                    category.remove_product(product)
                    print(f"Product '{product_name}' removed.")
                else:
                    print("Product not found.")
            else:
                print("Category not found.")

        elif choice == "5":
            print_inventory(inventory)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
