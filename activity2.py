import csv

# Function to load contacts from CSV file
def load_contacts(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found. Creating a new one.")
        return []
    
# Function to save contacts to CSV file
def save_contacts(file_path, contacts):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ["Name", "Phone", "Email", "Address", "Social Media"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
        
# Function to display all contacts
def display_contacts(contacts):
    print("\n{:<20} {:<15} {:<30} {:<30} {:<20}".format("Name", "Phone", "Email", "Address", "Social Media"))
    print("-" * 115)
    for contact in contacts:
        print("{:<20} {:<15} {:<30} {:<30} {:<20}".format(contact["Name"], contact["Phone"], contact["Email"], contact["Address"], contact["Social Media"]))

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    social_media = input("Enter Social Media: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address, "Social Media": social_media})
    print("Contact added successfully.")
    
# Function to update an existing contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact ['Name'] == name:
            contact['Phone'] = input("Enter new Phone: ")
            contact['Email'] = input("Enter new Email: ")
            contact['Address'] = input("Enter new Address: ")
            contact['Social Media'] = input("Enter new Social Media: ")
            found = True
            print("Contact updated successfully.")
            break
    if not found:
        print("Contact not found.")
        
# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print("Contact not found.")

# Main function to run the contact management system
def run_contact_manager():
    filename = "contacts.csv"
    contacts = load_contacts(filename)
    
    while True:
        print("\nContact Management System")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Save and Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == '3':
            update_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == '5':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
# Running contact management system
run_contact_manager()