library = {
    "101": {
        "title": "Python Basics",
        "author": "John Smith",
        "year": "2024"
    },
    "102": {
        "title": "Data Structures",
        "author": "Alice Brown",
        "year": "2023"
    }
}

rating = True

while rating:
    print("\n--- LIBRARY RECORD SYSTEM ---")
    print("1. View Books")
    print("2. Add Book")
    print("3. Update Book")
    print("4. Search Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- BOOK DETAILS ---")

        for book_id, details in library.items():
            print("Book ID:", book_id)
            print("Title:", details["title"])
            print("Author:", details["author"])
            print("Year:", details["year"])
            print("-------------------")

    elif choice == "2":
        book_id = input("Enter Book ID: ")

        if book_id in library:
            print("Book ID already exists!")
        else:
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")

            library[book_id] = {
                "title": title,
                "author": author,
                "year": year
            }

            print("Book added successfully!")

    elif choice == "3":
        book_id = input("Enter Book ID to update: ")

        if book_id in library:
            library[book_id]["title"] = input("Enter new title: ")
            library[book_id]["author"] = input("Enter new author: ")
            library[book_id]["year"] = input("Enter new year: ")

            print("Book updated successfully!")
        else:
            print("Book not found!")

    elif choice == "4":
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            print("\nBook ID:", book_id)
            print("Title:", library[book_id]["title"])
            print("Author:", library[book_id]["author"])
            print("Year:", library[book_id]["year"])
        else:
            print("Book not found!")

    elif choice == "5":
        book_id = input("Enter Book ID to delete: ")

        if book_id in library:
            del library[book_id]
            print("Book deleted successfully!")
        else:
            print("Book not found!")

    elif choice == "6":
        rating = False
        print("Thank you for using the Library Record System!")

    else:
        print("Invalid choice!")
