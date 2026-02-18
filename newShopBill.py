stationary_items = {"Pensil" : 5, "Register" : 50, "Pen" : 20, "Scale" : 10}

def inventory_management(items):
    # print(items)
    # print("Inventory management selected")
    while True:
        update_items = input("Please enter 'add' to add items in list, 'remove' to remove items from list or enter 'exit'to save: ").strip().lower()
        
        if update_items == "add":
            new_items = input("Enter new_item: ").strip().capitalize()
            while True:
                try:
                    base_price = int(input(f"Enter the base price for new {new_items}: "))
                    if base_price <= 0 :
                        print(f"You have entered {base_price} which is wrong. Please enter correct amount")
                    else:
                        items[new_items] = base_price
                        break
                except ValueError:
                    print("Enter only valid number, no string or spaces allowed")
            
        elif update_items == "remove":
            print(f"Select from these items to remove {items}")
            existing_item = input("Enter the item to remove it: ").strip().capitalize()
            if existing_item in items:
                del items[existing_item]
                print(f"The item that has been removed is: {existing_item}")
            else:
                print(f"You have selected {existing_item} that is not in the stock or wrong item. Select again to remove")
        
        elif update_items == "exit":
            break
        else:
            print("Invalid command. Enter again")
            
    
def generate_bill(items):
    user_cart = {}
    final_bill = 0
    while True:
        product_input = input("Please enter an item or type 'exit' : ").strip().capitalize()
        if product_input == "Exit":
            break
        elif product_input in items:
            while True:
                try:
                    quantity = int(input(f"Please enter the quantity for {product_input}: ")) 
                    if quantity <= 0:
                        print(f"You have entered wrong {quantity}. Please enter correct quantity")
                    else:
                        if product_input not in user_cart:
                            user_cart[product_input] = quantity
                        else: 
                            user_cart[product_input] += quantity
                        break
                except ValueError:
                        print("Enter only valid number, no string or spaces allowed")
        else:
            print("You have entered wrong item, Enter item again")

    if user_cart == {}:
        print("Nothing to print bill. User didn't purchase anything") 
    else:
        print("-" * 75)
        print(f"{'Product Name':<20}{'Quantity':>12}{'Unit Price':>18}{'Line Total':>18}")
        print("-" * 75)
        for product, quantity in user_cart.items():
                unit_price = items[product]
                # quantity = user_cart[product]
                line_total = unit_price * quantity  
                final_bill += line_total
                print(f"{product:<20}{quantity:>12}{'₹ ' + format(unit_price, '.2f'):>18}{'₹ ' + format(line_total, '.2f'):>18}")
        print("-" * 75)
        print(f"{'Total Amount':<50}{'₹ ' + format(final_bill, '.2f'):>18}")
        print("-" * 75)

def calculator():
    while True:
        # use_cal = input("Do you want to use calculator? Type 'yes' or 'no': ").strip().capitalize()
        user_input = input("Enter first number (or type 'exit'):")

        if user_input.strip().capitalize() == "Exit":
            print("Calculator closed.")
            break
        
        try:
            num1 = float(user_input)
             # num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, %): ").strip()
            num2 = float(input("Enter second number: "))
            
            match operator:
                case "+":
                    print("Result:", num1 + num2)

                case "-":
                    print("Result:", num1 - num2)

                case "*":
                    print("Result:", num1 * num2)

                case "/":
                    if num2 != 0:
                        print("Result:", num1 / num2)
                    else:
                        print("Error! Cannot divide by zero.")

                case "%":
                    if num2 != 0:
                        print("Result:", num1 % num2)
                    else:
                        print("Error! Cannot modulo by zero.")

                case _:
                    print("Invalid operator.")

        except ValueError:
            print("Invalid number entered!")
            
            
def main(items): 
    while True: 
        print(f"The current items in the stock are: {items}") 
        try: 
            user_choice = int(input("Please enter 1. To add to remove item \nPlease enter 2. To make bill \nPlease enter 3. To use calculator:\nOr enter 0 to Exit: \n")) 
            
            if user_choice not in [0,1,2,3]: 
                print("You have entered wrong number please select from given number only") 
                continue 
        
            if user_choice == 1: 
                inventory_management(items) 
            elif user_choice == 2: 
                generate_bill(items) 
            elif user_choice == 3: 
                calculator() 
            else: 
                print(f"{user_choice} Selected. Exiting the app")
                break 
            
        except ValueError: 
            print("Enter only valid number, no string") 
            
            
main(stationary_items)