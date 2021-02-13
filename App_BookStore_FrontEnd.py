from tkinter import *
from backend import Database

database = Database()

window = Tk()#Creating teh window app
window.wm_title("BookStore")

#This function will iterate through backend View function and insert all the data into the Listbox
def view_command():
    list1.delete(0, END)
    for rows in database.View():
        list1.insert(END, rows)

#This function will iterate through backend Search function and return the data base on the user's input
def search_command():
    list1.delete(0, END)
    #Search function is expecting 4 argumets. We are linking title, author, year and isbn to our entries values strings and calling .get function in order to have the string returned
    for item in database.Search(e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get()):
        list1.insert(END, item)

def insert_command():
    database.Insert(e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get())
    list1.delete(0,END)
    list1.insert(END, (e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get()))

def get_selected_row(event): # Creating a function that will grab the index of the selceted item and binding that on the "list1.bind"

    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(selected_tuple[1])


def delete_command():
    database.Delete(selected_tuple[0])



def update_command():
    database.Update(selected_tuple[0],e1_value.get(),e3_value.get(),e2_value.get(),e4_value.get())


l1 = Label(window,text = "Title")
l1.grid(row = 0, column = 0)
e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0, column = 1)

l2 = Label(window, text = "Year")
l2.grid(row = 1, column = 0)
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row = 1, column = 1)

l3 = Label(window, text = "Author")
l3.grid(row = 0, column = 2)
e3_value = StringVar()
e3 = Entry(window, textvariable = e3_value)
e3.grid(row= 0, column = 3)


l4 = Label(window, text = "ISBN")
l4.grid(row= 1, column = 2)
e4_value = StringVar()
e4 = Entry(window, textvariable = e4_value)
e4.grid(row = 1, column = 3)

#Adding the list box and allowing the rows and columns to span across multiple lines
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6 , columnspan = 2)

#CREATING THE SCROLLBAR FOR THE LISTBOX
sb1 = Scrollbar(window)
sb1.grid(row= 2, column =2, rowspan = 6) # Allowing the scrollbar to span across row2-6

#Configuring the scrollbar and attaching it to the ListBox
list1.configure(yscrollcommand = sb1.set)#Applying the scrollbar to the ListBox
sb1.configure(command = list1.yview)# Applying the scrollbar so the vertical view will change
list1.bind('<<listboxSelect>>',get_selected_row)

b1 = Button(window, text = "View all", width = 12,command = view_command)
b1.grid(row = 2, column =3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = insert_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)



window.mainloop()# Wrapping the entire window
