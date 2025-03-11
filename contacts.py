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

    def add_contact(self, name, phone, email):
        # Email validation
        if '@' not in email or '.' not in email:
            print("Invalid email address. Please provide a valid email.")
            return
        # Phone number validation
        if not phone.isdigit():
            print("Phone number must contain only digits.")
            return
        # Duplicate phone check
        if any(contact.phone == phone for contact in self.contacts):
            print(f"A contact with the phone number '{phone}' already exists.")
            return
        # Ask for confirmation
        confirm = input(f"Are you sure you want to add '{name}'? (y/n): ").lower()
        if confirm == 'y':
            new_contact = Contact(name, phone, email)
            self.contacts.append(new_contact)
            print(f"Contact '{name}' added successfully.")
        else:
            print("Contact addition canceled.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
            print("--------------------")
            print(f"Total Contacts: {len(self.contacts)}")

    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if found_contacts:
            print("\nSearch results:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found with keyword '{keyword}'.")

    def remove_contact(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' removed successfully.")
                return
        print(f"No contact found with phone number '{phone}'.")

def menu():
    cm = ContactManager()
    while True:
        print("\n+++ Contact Management Menu +++")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("+++++++++++++++++++++++++++++++")
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
            phone = input("Enter the phone number of the contact to remove: ")
            cm.remove_contact(phone)
        elif choice == '5':
            print("Thank you for using the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    menu()
