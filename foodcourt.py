import tkinter as tk
from tkinter import messagebox

class Restaurant:
    def __init__(self, name):
        self.name = name

class Admin:
    def __init__(self):
        self.items_list = []

    def login(self, username, password):
        return username == "admin" and password == "admin"

    def add_item(self, recipe, price):
        self.items_list.append({"recipe": recipe, "price": price})
        messagebox.showinfo("Success", f"Item '{recipe}' added successfully!")

    def delete_item(self, recipe):
        for item in self.items_list:
            if item["recipe"] == recipe:
                self.items_list.remove(item)
                messagebox.showinfo("Success", f"Item '{recipe}' deleted successfully!")
                return
        messagebox.showerror("Error", f"Item '{recipe}' not found!")

class Customer:
    def __init__(self, shared_items_list):
        self.order_items = []
        self.items_list = shared_items_list

    def login(self, username, password):
        return username == "customer" and password == "customer"

    def add_order(self, item):
        self.order_items.append(item)
        messagebox.showinfo("Success", f"'{item['recipe']}' added to your order!")

    def calculate_bill(self):
        total_price = sum(item['price'] for item in self.order_items)
        return total_price

    def checkout(self):
        if not self.order_items:
            messagebox.showinfo("Info", "No items to checkout!")
            return

        total_price = self.calculate_bill()
        self.order_items.clear()
        messagebox.showinfo("Checkout", f"Thank you for your purchase! Total: ${total_price}")

class RestaurantApp:
    def __init__(self, root):
        self.restaurant = Restaurant("Boykot")
        self.shared_items_list = []
        self.admin = Admin()
        self.admin.items_list = self.shared_items_list
        self.customer = Customer(self.shared_items_list)

        self.root = root
        self.root.title(self.restaurant.name)
        self.root.geometry("500x500")

        self.main_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text=f"Welcome to {self.restaurant.name}!", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Admin Login", command=self.admin_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Customer Login", command=self.customer_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20, font=("Arial", 14)).pack(pady=10)

    def admin_login(self):
        self.clear_frame()

        tk.Label(self.root, text="Admin Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 14)).pack()
        username_entry = tk.Entry(self.root, font=("Arial", 14))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 14)).pack()
        password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        password_entry.pack()

        def handle_login():
            if self.admin.login(username_entry.get(), password_entry.get()):
                self.admin_dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials!")

        tk.Button(self.root, text="Login", command=handle_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def admin_dashboard(self):
        self.clear_frame()

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Add Item", command=self.add_item, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Delete Item", command=self.delete_item, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="View Items", command=self.view_items, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def add_item(self):
        self.clear_frame()

        tk.Label(self.root, text="Add Item", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Recipe Name:", font=("Arial", 14)).pack()
        recipe_entry = tk.Entry(self.root, font=("Arial", 14))
        recipe_entry.pack()

        tk.Label(self.root, text="Price:", font=("Arial", 14)).pack()
        price_entry = tk.Entry(self.root, font=("Arial", 14))
        price_entry.pack()

        def handle_add():
            recipe = recipe_entry.get()
            try:
                price = float(price_entry.get())
                self.admin.add_item(recipe, price)
                self.admin_dashboard()
            except ValueError:
                messagebox.showerror("Error", "Invalid price!")

        tk.Button(self.root, text="Add", command=handle_add, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.admin_dashboard, width=20, font=("Arial", 14)).pack()

    def delete_item(self):
        self.clear_frame()

        tk.Label(self.root, text="Delete Item", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Recipe Name:", font=("Arial", 14)).pack()
        recipe_entry = tk.Entry(self.root, font=("Arial", 14))
        recipe_entry.pack()

        def handle_delete():
            recipe = recipe_entry.get()
            self.admin.delete_item(recipe)
            self.admin_dashboard()

        tk.Button(self.root, text="Delete", command=handle_delete, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.admin_dashboard, width=20, font=("Arial", 14)).pack()

    def view_items(self):
        self.clear_frame()

        tk.Label(self.root, text="Items List", font=("Arial", 18)).pack(pady=20)

        for item in self.shared_items_list:
            tk.Label(self.root, text=f"{item['recipe']} - ${item['price']}", font=("Arial", 14)).pack()

        tk.Button(self.root, text="Back", command=self.admin_dashboard, width=20, font=("Arial", 14)).pack(pady=10)

    def customer_login(self):
        self.clear_frame()

        tk.Label(self.root, text="Customer Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Username:", font=("Arial", 14)).pack()
        username_entry = tk.Entry(self.root, font=("Arial", 14))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 14)).pack()
        password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        password_entry.pack()

        def handle_login():
            if self.customer.login(username_entry.get(), password_entry.get()):
                self.customer_dashboard()
            else:
                messagebox.showerror("Error", "Invalid credentials!")

        tk.Button(self.root, text="Login", command=handle_login, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def customer_dashboard(self):
        self.clear_frame()

        tk.Label(self.root, text="Customer Dashboard", font=("Arial", 18)).pack(pady=20)

        for item in self.shared_items_list:
            tk.Button(self.root, text=f"{item['recipe']} - ${item['price']}",
                      command=lambda i=item: self.customer.add_order(i),
                      width=30, font=("Arial", 14)).pack(pady=5)

        tk.Button(self.root, text="View Bill", command=self.view_bill, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Checkout", command=self.customer.checkout, width=20, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu, width=20, font=("Arial", 14)).pack()

    def view_bill(self):
        self.clear_frame()

        tk.Label(self.root, text="Your Bill", font=("Arial", 18)).pack(pady=20)

        total_price = 0
        for item in self.customer.order_items:
            tk.Label(self.root, text=f"{item['recipe']} - ${item['price']}", font=("Arial", 14)).pack()
            total_price += item['price']

        tk.Label(self.root, text=f"Total: ${total_price}", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Back", command=self.customer_dashboard, width=20, font=("Arial", 14)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()



#------------------------- My Code without GUI ---------------------------------


# import os
# import time

# class FoodCourt:
#     def __init__(self,name):
#         self.name=name
    
#     def details(self):
#         return f"===========================  Welcome to {self.name} !  ===========================\n1. Admin Login\n2. Customer Login\n3. Exit"

#     def __str__(self):
#         return self.name

# class Admin(FoodCourt):
#     itemsList=[]
#     def __init__(self,name):
#         super().__init__(name)
    
#     def login(self,username,password):
#         if username=="admin" and password=="admin":
#             return "getAccess"
#         else:
#             return "Invalid"
    
#     def addItems(self,recipe,price):
#         self.itemsList.append({"recipe": recipe,"price":price})
#         print()
#         print(f"Item: '{recipe}' added Successfully...")
    
#     def deleteItems(self,recipe):
#         for item in self.itemsList:
#             if item["recipe"]==recipe:
#                 self.itemsList.remove(item)
#                 print()
#                 print(f"Item: '{recipe}' deleted Successfully...")
#                 break
#             else:
#                 print()
#                 print(f"Item: '{recipe}' not found...!")
#                 break
    
#     def getItems(self):
#         for ind,item in enumerate(self.itemsList):
#             print(f"{ind+1}. {item['recipe']} - ${item['price']}")
    
#     def details(self):
#         print("1. Add Item\n2. Remove Item\n3. Items List\n4. Back")
        
# class Customer(Admin):
#     orderItems=[]
#     def __init__(self,name):
#         super().__init__(name)

#     def login(self,username,password):
#         if username=="customer" and password=="customer":
#             return "getAccess"
#         else:
#             return "Invalid"
    
#     def menu(self):
#         for ind,item in enumerate(self.itemsList):
#             print(f"{ind+1}. {item['recipe']} - ${item['price']}")
    
#     def orders(self,item):
#         self.orderItems.append(item)

#     def clearOrders(self):
#         self.orderItems.clear()
    
#     def bill(self):
#         items=[]
#         price=0
#         for item in self.orderItems:
#             items.append(item['recipe'])
#             price+=item['price']
#         print(f"Items ordered: {items}\nTotal Bill: {price}")
#         print()
#         return price

# restaurent=FoodCourt("Boykot")

# while True:
#     os.system("cls")
#     print(restaurent.details())
#     try:
#         choice=int(input("Please select to login: "))
#         if choice==1:
#             os.system("cls")
#             print("========================  Please Enter Admin Credentials  ========================")
#             username=input("Enter your username: ")
#             password=input("Enter your password: ")
#             admin=Admin(restaurent)
#             if admin.login(username,password)=="getAccess":
#                 os.system("cls")
#                 while True:
#                     print("=====================  Welcome to Admin Dashboard  =====================")
#                     admin.details()
#                     try:
#                         select=int(input("Select an Option: "))
#                         if select==1:
#                             recipe=input("Enter a recipe: ")
#                             price=float(input("Enter a price: "))
#                             admin.addItems(recipe,price)
#                             print()
#                             print("Please wait 1 seconds to exit the dashboard...")
#                             time.sleep(1)
#                             os.system("cls")
#                         elif select==2:
#                             recipe=input("Enter a recipe: ")
#                             admin.deleteItems(recipe)
#                             print()
#                             print("Please wait 1 seconds to exit the dashboard...")
#                             time.sleep(1)
#                             os.system("cls")
#                         elif select==3:
#                             os.system("cls")
#                             print("========================  Items List  ========================")
#                             admin.getItems()
#                             print()
#                         elif select==4:
#                             break
#                         else:
#                             print()
#                             print("Invalid Option")
#                             print()
#                             print("Please wait 1 second to get back...")
#                             time.sleep(1)
#                             os.system("cls")
#                     except:
#                         print()
#                         print("Invalid Input...")
#                         print()
#                         print("Please wait 1 second to go back....")
#                         time.sleep(1)
#                         os.system("cls")
#             else:
#                 print()
#                 print("Invalid Login Credentials...!")
#                 print()
#                 print("Please wait 1 second to Login...")
#                 time.sleep(1)
#         elif choice==2:
#             os.system("cls")
#             print("======================  Please Enter Customer Credentials  ======================")
#             username=input("Enter your username: ")
#             password=input("Enter your password: ")
#             customer=Customer(restaurent)
#             if customer.login(username,password)=="getAccess":
#                 while True:
#                     os.system("cls")
#                     print("=====================  Welcome to Customer Dashboard  =====================")
#                     customer.menu()
#                     print()
#                     customer.bill()
#                     print("Enter 0 to Bill out the Orders....!")
#                     try:
#                         order=int(input("Enter order number: "))
#                         if order<len(customer.itemsList)+1 and order>0:
#                             for ind,item in enumerate(customer.itemsList):
#                                 if ind+1==order:
#                                     customer.orders(item)
#                                     break
#                         else:
#                             print()
#                             print(f"Thank you for your orders - Bill: ${customer.bill()}")
#                             print()
#                             customer.clearOrders()
#                             print("Please wait 2 seconds to exit the dashboard...")
#                             time.sleep(2)
#                             break
#                     except:
#                         print()
#                         print("Invalid Input...")
#                         print()
#                         print("Please wait 1 second to go back....")
#                         time.sleep(1)
#                         os.system("cls")
#             else:
#                 print()
#                 print("Invalid Login Credentials...!")
#                 print()
#                 print("Please wait 1 second to Login...")
#                 time.sleep(1)
#         elif choice==3:
#             print()
#             print("Thank you for Visit...!")
#             print()
#             break
#         else:
#             print()
#             print("Select valid option...?")
#             print()
#             print("Please wait 1 second to login....")
#             time.sleep(1)
#     except:
#         print()
#         print("Invalid Input...")
#         print()
#         print("Please wait 1 second to login....")
#         time.sleep(1)