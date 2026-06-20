from datetime import datetime, timedelta
from database import insert_values, create_table, view_history, delete_history
from qr_generator import generate_qr
from layout import create_layout, create_sheet, create_layout_nosize

create_table()
delete_history()

while True:

    print("QR code generator:")   
    print("1. Generate new tag")
    print("2. View History")
    print("3. Exit")
    
    try:
        option = int(input("Enter choice: "))
    except ValueError:
        print("Enter a number!")
        continue

    if option not in [1, 2, 3]:
        print("Invalid Choice!")
        continue

    elif option == 1:
        code = input("Enter product code: ")

        if not code.isdigit():
            print("Product code must contain only digits.")
            continue


        try:
            price = int(input("Enter price of product: "))
        except ValueError:
            print("Price can only be numerical!")
            continue

        if price < 0:
            print("Price cannot be negative!")
            continue

        name = input("Enter name of product: ").strip()
        if name == "":
            print("Name cannot be blank!")
            continue

        try:
            sizes_option = int(input("Include one size?(1. Yes   2. No): "))
        except ValueError:
            print("Enter 1 or 2!")
            continue

        if sizes_option not in [1, 2]:
            print("Invalid Choice!")

        elif sizes_option == 1:
            size = input("Size: ").upper()

            qr_path = generate_qr(code)
            tag_path = create_layout(qr_path, code, price, name, size)
            sheet_path = create_sheet(tag_path)

            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            insert_values(code, name, price, created_at, size)

            print("Sheet created:", sheet_path)

        elif sizes_option == 2:
            qr_path = generate_qr(code)
            tag_path = create_layout_nosize(qr_path, code, price, name)
            sheet_path = create_sheet(tag_path)

            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            insert_values(code, name, price, created_at)

            print("Sheet created:", sheet_path)

    
    elif option == 2:
        rows = view_history()
        for index, row in enumerate(rows):
            code, name, price, size = row
            print(f"{index + 1}. {code} {name}")

        try:
            reprint = int(input("Select item to reprint: "))
        except ValueError:
            print("Invalid option!")
            continue

        if reprint < 1 or reprint > len(rows):
            print("Invalid number!")
            continue

        row = rows[reprint - 1]
        code, name, price, size = row

        qr_path = generate_qr(code)

        if size == "":
            tag_path = create_layout_nosize(qr_path, code, price, name)
            sheet_path = create_sheet(tag_path)
        
        else:
            tag_path = create_layout(qr_path, code, price, name, size)
            sheet_path = create_sheet(tag_path)   


    elif option == 3:
        print("Exiting...")
        break