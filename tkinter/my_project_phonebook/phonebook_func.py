import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

# import other modules
import phonebook_main
import phonebook_gui


def center_window(self, w, h):
    
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    # calculate the x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))

    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user clicks on the window X to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # closes the app
        self.master.destroy()
        os._exit(0)



#=======================================================
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # create the phonebook table if it doesn't exist
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count


# Select item in ListBox
def onSelect(self, event):
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # this returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() # remove blank space before and after
    var_lname = var_lname.strip()
    var_fname = var_fname.title() # capitalize the first character
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            # check the database for existence of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no instance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update the listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there are data in all four fields.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete the last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #call the function to clear all of the textboxes and the selected index of listbox
###                onRefresh(self) #update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select))
    conn.close()


def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
###    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)


def onRefresh(self):
    # populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing Selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # the user will only be allowed to update changes for phone and emails.
    # for name changes, the user will need to delete teh entire record and start over.
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0:
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \nProceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}', col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel Request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No Changes Detected","both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone,var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing Information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)


if __name__ == "__main__":
    pass
