import os

contacts = []

def clear():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except:
        pass

def line():
    print("=" * 60)

def pause():
    input("\nPress Enter to continue...")

def find_contact(phone):
    for contact in contacts:
        if contact["Phone"] == phone:
            return contact
    return None

def add_contact():
    line()
    print("ADD NEW CONTACT")
    line()

    name = input("Enter Name: ").strip().title()
    phone = input("Enter Phone: ").strip()

    if find_contact(phone):
        print("Contact with this phone number already exists!")
        return

    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts.append({
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    })

    print("Contact Added Successfully!")

def view_contacts():
    line()
    print("CONTACT LIST")
    line()

    if len(contacts) == 0:
        print("No contacts available.")
        return

    contacts.sort(key=lambda x: x["Name"])

    print("{:<20} {:<15}".format("Name", "Phone"))
    print("-" * 40)

    for c in contacts:
        print("{:<20} {:<15}".format(c["Name"], c["Phone"]))

def search_contact():
    line()
    print("SEARCH CONTACT")
    line()

    key = input("Enter Name or Phone: ").strip().lower()

    found = False

    for c in contacts:
        if key == c["Phone"] or key in c["Name"].lower():
            line()
            print("Name    :", c["Name"])
            print("Phone   :", c["Phone"])
            print("Email   :", c["Email"])
            print("Address :", c["Address"])
            found = True

    if not found:
        print("Contact Not Found!")

def update_contact():
    line()
    print("UPDATE CONTACT")
    line()

    phone = input("Enter Phone Number: ").strip()

    contact = find_contact(phone)

    if contact is None:
        print("Contact Not Found!")
        return

    print("Leave blank to keep old value.")

    name = input("New Name: ").strip()
    email = input("New Email: ").strip()
    address = input("New Address: ").strip()

    if name:
        contact["Name"] = name.title()
    if email:
        contact["Email"] = email
    if address:
        contact["Address"] = address

    print("Contact Updated Successfully!")

def delete_contact():
    line()
    print("DELETE CONTACT")
    line()

    phone = input("Enter Phone Number: ").strip()

    contact = find_contact(phone)

    if contact is None:
        print("Contact Not Found!")
        return

    contacts.remove(contact)
    print("Contact Deleted Successfully!")

def main():
    while True:
        clear()

        line()
        print("CONTACT BOOK MANAGEMENT SYSTEM")
        line()

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

        clear()

        if choice == "1":
            add_contact()
            pause()

        elif choice == "2":
            view_contacts()
            pause()

        elif choice == "3":
            search_contact()
            pause()

        elif choice == "4":
            update_contact()
            pause()

        elif choice == "5":
            delete_contact()
            pause()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")
            pause()

if __name__ == "__main__":
    main()
