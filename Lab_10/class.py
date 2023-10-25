# Create a menu driven program that will 
# create new orders and update the inventory accordingly
# Export the final data to the field


class SportsMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createOrder(self, OrderId, ItemName, Quantity, Price):
        temp = {
            "orderID": OrderId,
            "ItemName": ItemName,
            "Quantity": Quantity,
            "Price": Price,
        }
        self.orders[OrderId] = temp

    def createInventoryItem(self, ProductID, ProductName, Quantity, Price):
        temp = {
            "Product ID": ProductID,
            "Product Name": ProductName,
            "Quantity": Quantity,
            "Price": Price,
        }
        self.inventory[ProductID] = temp

    def printOrders(self):
        print("Orders:")
        for order in self.orders.values():
            print(order)

    def printInventory(self):
        print("Inventory:")
        for item in self.inventory.values():
            print(item)

    def exportData(self, filename="exported_data.csv"):
        with open(filename, "w") as file:
            file.write("Orders:\n")
            for order in self.orders.values():
                file.write(f"{order['orderID']},{order['ItemName']},{order['Quantity']},{order['Price']}\n")

            file.write("\nInventory:\n")
            for item in self.inventory.values():
                file.write(f"{item['Product ID']},{item['Product Name']},{item['Quantity']},{item['Price']}\n")

def main():
    trinity = SportsMart()

    while True:
        print("\nMenu:")
        print("1. Create Order")
        print("2. Create Inventory Item")
        print("3. Print Orders")
        print("4. Print Inventory")
        print("5. Export Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            OrderId = input("Enter Order ID: ")
            ItemName = input("Enter Item Name: ")
            Quantity = input("Enter Quantity: ")
            Price = input("Enter Price: ")
            trinity.createOrder(OrderId, ItemName, Quantity, Price)

        elif choice == "2":
            ProductID = input("Enter Product ID: ")
            ProductName = input("Enter Product Name: ")
            Quantity = input("Enter Quantity: ")
            Price = input("Enter Price: ")
            trinity.createInventoryItem(ProductID, ProductName, Quantity, Price)

        elif choice == "3":
            trinity.printOrders()

        elif choice == "4":
            trinity.printInventory()

        elif choice == "5":
            filename = input("Enter filename to export data (default: exported_data.csv): ").strip()
            if not filename:
                filename = "exported_data.csv"
            trinity.exportData(filename)
            print(f"Data exported to {filename}")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
