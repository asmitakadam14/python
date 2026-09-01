

product_name=[]



while True:
    print("\n1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Sort")
    print("5. Update")
    print("6. Delete")
    print("7. Exit")

    ch =int(input("Enter choice: "))

    
    if ch == 1:
        name = input("Enter name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product_name.append([name, price, quantity])
        print("Added!")

    
    elif ch == 2:
        for p in product_name:
            print("Name:", p[0], "Price:", p[1], "Quantity:", p[2])

    
    elif ch == 3:
        name = input("Enter name to search: ")

        for p in product_name:
            if p[0].lower() == name.lower():
                print("Found:", p)
                break
        else:
            print("Not found")

    
    elif ch == 4:
          product_name.sort(key=lambda p: p[1])

          print("Sorted by price:")
          for p in product_name:
            print(p)

    
    elif ch == 5:
        name = input("Enter name to update: ")

        for p in product_name:
            if p[0].lower() == name.lower():
                p[1] = int(input("Enter new price: "))
                p[2] = int(input("Enter new quantity: "))
                print("Updated!")
                break
        else:
            print("Not found")

    
    elif ch == 6:
        name = input("Enter name to delete: ")

        for p in product_name:
            if p[0].lower() == name.lower():
                product_name.remove(p)
                print("Deleted!")
                break
        else:
            print("Not found")

    
    elif ch == 7:
        break

    else:
        print("Wrong choice")


        

