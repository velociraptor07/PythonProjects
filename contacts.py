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

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if found_contacts:
            print("Search results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

def menu():
    cm = ContactManager()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu()
