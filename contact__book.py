import tkinter as tk


#WINDOW
window = tk.Tk()
window.title('daftarche ie mokhatab')
window.geometry('400x500')


#TITEL
title_label = tk.Label(window,text = 'daftarche ie mokhatab',font=('Arial',20))
title_label.grid(row=0,column=0,columnspan=2,pady=1)


#NAME LABEL
name_label = tk.Label(window,text='NAME:        ')
name_label.grid(row=1,column=0,columnspan=10,pady=10)
name_entry=tk.Entry(window)
name_entry.grid(row=1,column=1,columnspan=10,pady=10)


edit_index = None


#NUMBER LABEL
phone_label = tk.Label(window,text='PHONE:           ')
phone_label.grid(row=2,column=0,columnspan=10,pady=10)
phone_entry=tk.Entry(window)
phone_entry.grid(row=2,column=1,columnspan=10,pady=10)


#TAVABE BUTTONS
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name !='' and phone !='':
        contact_list.insert(tk.END,name + '--' + phone)
        name_entry.delete(0,tk.END)
        phone_entry.delete(0,tk.END)


def delete_contact():
    selected = contact_list.curselection()

    if selected:
        contact_list.delete(selected[0])


def edit_contact():
    global edit_index
    selected = contact_list.curselection()

    if selected:
       edit_index = selected[0]
       contact=contact_list.get(edit_index)

       name , phone = contact.split('--')

       name_entry.delete(0,tk.END)
       phone_entry.delete(0,tk.END)

       name_entry.insert(0,name)
       phone_entry.insert(0,phone)
       
def save_edit():
    global edit_index

    if edit_index is not None:
        name = name_entry.get()
        phone = phone_entry.get()
        if name != '' and phone != '':
            contact_list.delete(edit_index)
            contact_list.insert(edit_index,name + '--' + phone)

            edit_index = None
        name_entry.delete(0,tk.END)
        phone_entry.delete(0,tk.END)
       
       
def search_contact():
    serch_name = name_entry.get()
    contact_list.selection_clear(0,tk.END)
    for i in range (contact_list.size()):
        contact = contact_list.get(i)
        if serch_name.lower() in contact.lower():
            contact_list.selection_set(i)
            contact_list.see(i)

#BUTTON
add_button=tk.Button(window,text='ADD',command=add_contact)
add_button.grid(row=3,column=0,columnspan=10,pady=10)


edit_button=tk.Button(window,text='EDIT',command=edit_contact)
edit_button.grid(row=3,column=1,columnspan=10,pady=10)


save_button=tk.Button(window,text='SAVE',command=save_edit)
save_button.grid(row=4,column=0,columnspan=10,pady=10)

delit_button=tk.Button(window,text='DELETE',command=delete_contact)
delit_button.grid(row=3,column=2,columnspan=10,pady=10)

serch_button=tk.Button(window,text='SEARCH',command=search_contact)
serch_button.grid(row=4,column=2,columnspan=10,pady=10)


#PHOND LIST
contact_list = tk.Listbox(window,width=35,height=10)
contact_list.grid(row=5,column=0,columnspan=2,padx=10,pady=20)

window.mainloop()
