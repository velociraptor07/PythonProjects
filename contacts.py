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
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Contact '{deleted_contact.name}' has been deleted.")
        else:
            print("Invalid index. Contact not found.")

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
        found_contacts = [contact for contact in self.contacts 
                          if keyword.lower() in contact.name.lower() 
                          or keyword in contact.phone 
                          or keyword.lower() in contact.email.lower()]
        if found_contacts:
            print("\nSearch results:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found with keyword '{keyword}'.")

def menu():
    cm = ContactManager()
    while True:
        print("\n*** Contact Manager ***")
        print("1. Add New Contact")
        print("2. Delete Contact")
        print("3. View All Contacts")
        print("4. Search for Contact")
        print("5. Exit")
        print("************************")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            cm.add_contact(name, phone, email)
        elif choice == '2':
            cm.view_contacts()  # Show contacts before deletion
            try:
                index = int(input("Enter the index of the contact to delete: ")) - 1
                cm.delete_contact(index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == '3':
            cm.view_contacts()
        elif choice == '4':
            keyword = input("Enter name, phone number, or email to search: ")
            cm.search_contact(keyword)
        elif choice == '5':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
