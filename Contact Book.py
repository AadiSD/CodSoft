import tkinter as tk
from tkinter import messagebox

def center_window(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 600) // 2
    y = (screen_height - 350) // 2
    root.geometry(f"600x350+{x}+{y}")
    root.configure(background='light gray')

def list_contacts():
    contact_list.delete(0, tk.END)
    for name, contact_info in contacts.items():
        phone_number = contact_info['phone']
        contact_list.insert(tk.END, f"{name} - {phone_number}")

def show_contact_details(event):
    selected_indices = contact_list.curselection()
    if selected_indices:
        selected_contact = contact_list.get(selected_indices[0])
        selected_name = selected_contact.split(" - ")[0]
        contact_info = contacts[selected_name]
        contact_details_label.config(
            text=f"Name: {selected_name}\nPhone: {contact_info['phone']}\nEmail: {contact_info['email']}\nAddress: {contact_info['address']}")
        update_name_entry.delete(0, tk.END)
        update_name_entry.insert(0, selected_name)

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    if not selected_contact:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return

    confirmation = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
    if confirmation:
        selected_name = selected_contact.split(" - ")[0]
        if selected_name in contacts:
            del contacts[selected_name]
            list_contacts()
            clear_entries()
        else:
            messagebox.showerror("Error", "Selected contact not found.")

def search_contact():
    search_term = search_entry.get()
    matching_contacts = {}

    for name, contact_info in contacts.items():
        if search_term.lower() in name.lower() or search_term in contact_info['phone']:
            matching_contacts[name] = contact_info

    contacts.clear()
    contacts.update(matching_contacts)
    list_contacts()

def update_contact():
    selected_name = update_name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if selected_name in contacts:
        if phone:
            contacts[selected_name]['phone'] = phone
        if email:
            contacts[selected_name]['email'] = email
        if address:
            contacts[selected_name]['address'] = address

        list_contacts()
        clear_entries()
    else:
        messagebox.showerror("Error", "Selected contact not found.")

def view_all_contacts():
    contacts.clear()
    contacts.update(all_contacts)
    list_contacts()

def validate_phone_input(P):
    if P == "" or P.isdigit():
        return True
    else:
        return False

def clear_fields():
    clear_entries()

root = tk.Tk()
root.title("Contact Book")
center_window(root)

contacts = {}
all_contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name:
        all_contacts[name] = {'phone': phone, 'email': email, 'address': address}
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        list_contacts()
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter a name for the contact.")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_label.configure(background="light gray")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_label.configure(background="light gray")

phone_validation = root.register(validate_phone_input)
phone_entry = tk.Entry(root, validate="key", validatecommand=(phone_validation, "%P"))
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_label.configure(background="light gray")

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5)
address_label.configure(background="light gray")

address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
add_button.configure(background='white')

update_name_label = tk.Label(root, text="Update Contact:")
update_name_label.grid(row=5, column=0, padx=10, pady=5)
update_name_label.configure(background="light gray")

update_name_entry = tk.Entry(root)
update_name_entry.grid(row=5, column=1, padx=10, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
update_button.configure(background='white')

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, width=15)
delete_button.place(x=300, y=135)
delete_button.configure(background='white')

search_label = tk.Label(root, text="Search Contact:")
search_label.place(x=300, y=175)
search_label.configure(background="light gray")

search_entry = tk.Entry(root, width=25)
search_entry.place(x=420, y=175)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.place(x=420, y=210)
search_button.configure(background='white')

view_all_button = tk.Button(root, text="View All Contacts", command=view_all_contacts, width=15)
view_all_button.grid(row=11, column=1, padx=10, pady=10)
view_all_button.place(x=460, y=135)
view_all_button.configure(background='white')

clear_button = tk.Button(root, text="Clear Fields", command=clear_fields, width=10)
clear_button.place(x=424, y=250)
clear_button.configure(background='white')

contact_list = tk.Listbox(root, selectmode=tk.SINGLE, height=7, width=45)
contact_list.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
contact_list.place(x=300, y=5)
contact_list.bind("<<ListboxSelect>>", show_contact_details)

contact_details_label = tk.Label(root, text="", anchor="w")
contact_details_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
contact_details_label.configure(background="light gray")

root.mainloop()
