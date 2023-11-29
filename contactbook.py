class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts in the book.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No contacts found.")

    def update_contact(self, contact_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name == contact_name:
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {contact_name} updated successfully.")
                return
        print(f"Contact {contact_name} not found.")

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name == contact_name:
                self.contacts.remove(contact)
                print(f"Contact {contact_name} deleted successfully.")
                return
        print(f"Contact {contact_name} not found.")

contact_book = ContactBook()

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        contact_book.add_contact(new_contact)

    elif choice == "2":
        contact_book.view_contact_list()

    elif choice == "3":
        keyword = input("Enter name or phone number to search: ")
        contact_book.search_contact(keyword)

    elif choice == "4":
        contact_name = input("Enter name of the contact to update: ")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        contact_book.update_contact(contact_name, new_phone, new_email, new_address)

    elif choice == "5":
        contact_name = input("Enter name of the contact to delete: ")
        contact_book.delete_contact(contact_name)

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")