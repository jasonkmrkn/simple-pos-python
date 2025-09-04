from transaction import *
from utilities import *

is_first_time = True

while (True):
    if is_first_time:
        is_first_time = False
        name = input("Input customer name: ")
        trs = Transaction(name)
    
    clear_screen()
    print("===WELCOME TO PACMANN SUPERMARKET===")
    print("\n\nThis Supermarket implements a self-service system. Choose from the menu below.")
    print("\n 1. Items List")
    print(" 2. Add Item")
    print(" 3. Edit Items List")
    print(" 4. Check Transaction")
    print(" 5. Pay Transaction")
    print(" 6. Exit")

    try:
        choice = int(input("\nMenu: "))
    except ValueError:
        clear_screen()
        print("Your item choice is invalid!")
        input("Press enter to continue...")
        continue

    match choice:
        case 1:
            clear_screen()
            print("Below are items that you can purchase.\n")
            print("Press enter to go back to home menu!\n")
            trs.show_items_list()
            input()

        case 2:
            clear_screen()
            trs.show_items_list()
            item_index = input("Choose item that you want to purchase (write \"X\"/ uppercase x to cancel). ")

            if item_index == 'X':
                continue

            try:
                item_index = int(item_index)
                item_to_buy = list(Item)[item_index]
            except IndexError:
                clear_screen()
                print("Your item choice is invalid!")
                input("Press enter to continue...")
                continue

            qty = int(input("Input the quantity that you want to purchase: "))
            trs.add_item(item_to_buy, qty)

        case 3:
            clear_screen()
            print("Here are the items that you want to purchase:")
            trs.check_transactions()

            print("\n1. Change Item Quantity")
            print("2. Change Item")
            print("3. Delete Item")
            print("4. Reset Transaction")
            print("5. Back to home")
            action_idx = int(input("Choose action:"))

            if (action_idx > 5 or action_idx < 1):
                clear_screen()
                print("Your action input is invalid!")
                input("press enter to continue!")
                continue

            if action_idx == 5:
                continue
            
            try:
                if action_idx != 4:
                    item_idx = int(input("Input item number! "))
                    item_to_be_search = trs.item_lists_with_total_price[item_idx][0]
            except IndexError:
                clear_screen()
                print("Your item choice is invalid!")
                input("Press enter to continue...")
                continue
            
            match action_idx:
                case 1:
                    new_qty = int(input("input new quantity: "))
                    trs.update_item_qty(item_to_be_search, new_qty)
                case 2:
                    clear_screen()
                    trs.show_items_list()
                    new_item_idx = int(input("Input new item number! "))
                    new_item = list(Item)[new_item_idx]
                    trs.change_item(item_to_be_search, new_item)
                case 3:
                    trs.delete_item(item_to_be_search)
                case 4:
                    trs.reset_transaction()
            
            clear_screen()
            print("Action done!")
            input("press enter to continue!")

        case 4:
            clear_screen()
            trs.check_transactions()
            print("Press enter to continue...")
            input()

        case 5:
            clear_screen()
            print("Here are the items that you want to purchase: ")
            trs.check_transactions()
            trs.check_discount()
            input("press enter to continue!")

        case 6:
            exit()
        case _:
            clear_screen()
            print("Invalid Input! press enter to continue...")
            input()
