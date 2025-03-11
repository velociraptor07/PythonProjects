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

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            print("\n--- Contact List ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
            print("--------------------")

def menu():
    cm = ContactManager()
    while True:
        print("\n*** Contact Manager ***")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for Contact")
        print("4. Exit")
        print("************************")
        choice = input("Choose an option (1-4): ")

        if choice == '1':

        elif choice == '2':
            cm.view_contacts()
        elif choice == '4':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
