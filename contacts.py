class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    # Function to add a new contact
    def add_contact(self, name, phone, email):
        if any(contact.phone == phone for contact in self.contacts):
            print(f"A contact with the phone number '{phone}' already exists.")
            return
        confirm = input(f"Are you sure you want to add '{name}'? (y/n): ").lower()
        if confirm == 'y':
            new_contact = Contact(name, phone, email)
            self.contacts.append(new_contact)
            print(f"Contact '{name}' added successfully.")
        else:
            print("Contact addition canceled.")

    # Function to view all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
            print("--------------------")
    
    # Function to search for a contact by name or phone number
    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if found_contacts:
            print("\nSearch results:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found with keyword '{keyword}'.")

    # Function to delete a contact by index
    def delete_contact(self):
        if not self.contacts:
            print("No contacts to delete.")
            return

        self.view_contacts()
        try:
            index = int(input("Enter the contact number to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                confirm = input(f"Are you sure you want to delete '{self.contacts[index].name}'? (y/n): ").lower()
                if confirm == 'y':
                    deleted_contact = self.contacts.pop(index)
                    print(f"Contact '{deleted_contact.name}' has been deleted.")
                else:
                    print("Deletion canceled.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    cm = ContactManager()
    while True:
        print("\n*** Contact Manager ***")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for Contact")
        print("4. Delete a Contact")
        print("5. Exit")
        print("************************")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            cm.add_contact(name, phone, email)
        elif choice == '2':
            cm.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            cm.search_contact(keyword)
        elif choice == '4':
            cm.delete_contact()
        elif choice == '5':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
