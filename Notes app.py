
import tkinter as tk # This allows you to have a Graphical User Interface
import sqlite3 # This allows you to create a database


#Creating a window
window = tk.Tk() # a window instance
window.title("Notes")
window.geometry("500x500") #creates the window size


# destroy all widgets

def destroy_all_widgets():
    """Destroy all widgets in the window."""
    for widget in window.winfo_children():
        widget.destroy()

# go back function

def go_back():
    
    destroy_all_widgets()
    add=tk.Button(window, text="Add", font=("Helvetica", 16, "bold"), command=add_notes) #Button 1
    add.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    view=tk.Button(window, text="View", font=("Helvetica", 16, "bold"), command=view_notes) #Button 2
    view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    delete=tk.Button(window, text="Delete", font=("Helvetica", 16, "bold"), command=delete_notes) #Button 3
    delete.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# Add notes function - this add notes page should have text box, a button to save the notes, and ability to delete the notes 
# when you delete the notes it should say are you sure and when you save it should ask a title and then a enter or go back button
def add_notes():
    destroy_all_widgets()
    text_box = tk.Text(window, height=10, width=40)
    text_box.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(window, text="Type name of file", font=("Helvetica", 16, "bold"))
    label.pack(side=tk.TOP, fill=tk.X, pady=10)
    same_title_label = tk.Label(window, text="Rename file - there is a note with the same title", font=("Helvetica", 16, "bold"))
    same_title_label.pack_forget()
    no_title_label = tk.Label(window, text="Type name of file and click save to save note", font=("Helvetica", 16, "bold"))
    no_title_label.pack_forget()
    file_saved_label = tk.Label(window, text="File saved!", font=("Helvetica", 16, "bold"))
    file_saved_label.pack_forget()

    entry = tk.Entry(window, font=("Helvetica", 16, "bold")) #where you will type the name of the file
    entry.pack(side=tk.TOP, fill=tk.X, pady=10)

    # creating a frame at the button to hold the two buttons save and back
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side="bottom", pady=10)

    back =tk.Button(bottom_frame, text="back", font=("Helvetica", 16, "bold"), command=go_back) # back button
    back.pack(side="left", fill="x", pady=10)

    def save(): #creating a save function
        
        title_content = entry.get()

        conn = sqlite3.connect('notes.sqlite') #connects to the database and creates a notes database if it does not exists
        cur = conn.cursor() # gives you the ability to start doing things in the database
        cur.execute("SELECT title FROM Files WHERE title = ?" , (title_content,))
        check_column = cur.fetchone()
        conn.commit()
        conn.close()


        if title_content == '':
            
            label.pack_forget()
            same_title_label.pack_forget()
            file_saved_label.pack_forget()

            no_title_label.pack(side=tk.TOP, fill=tk.X, pady=10)

        elif check_column is not None:

            if title_content == check_column[0]:
                
                label.pack_forget()
                no_title_label.pack_forget()
                file_saved_label.pack_forget()
                same_title_label.pack(side=tk.TOP, fill=tk.X, pady=10)

        else:
                    
            same_title_label.pack_forget()
            no_title_label.pack_forget()
            label.forget()
            file_saved_label.pack()
                
            notes_content = text_box.get("1.0", tk.END).strip()  # Strip to remove any trailing newline
            conn = sqlite3.connect('notes.sqlite') #connects to the database and creates a notes database if it does not exists
            cur = conn.cursor() # gives you the ability to start doing things in the database
            cur.execute('INSERT INTO Files (title, notes) VALUES (?, ?)', (title_content, notes_content))
            conn.commit()
            conn.close()

            

    save =tk.Button(bottom_frame, text="Save", font=("Helvetica", 16, "bold"), command=save) # Save button
    save.pack(side="right", fill="x", pady=10)


# a widget opens up and you search the name of file you would like to view - when you click enter it opens the notes
# You should have the ability to go back to the main page
def view_notes(): 
    destroy_all_widgets()
    
    label_view = tk.Label(window, text="Type name of file", font=("Helvetica", 16, "bold"))
    label_view.pack()
    entry_view = tk.Entry(window, font=("Helvetica", 16, "bold")) #where you will type the name of the file
    entry_view.pack()

    # creating a frame at the button to hold the two buttons delete and back
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side="bottom", pady=10)

    back =tk.Button(window, text="back", font=("Helvetica", 16, "bold"), command=go_back) # back button
    back.pack(side="bottom", fill="x", pady=10)

    def find_file():
        find_content = entry_view.get()
        
        destroy_all_widgets()

        # creating a frame at the button to hold the two buttons save and back
        bottom_frame = tk.Frame(window)
        bottom_frame.pack(side="bottom", pady=10)
        
        back =tk.Button(bottom_frame, text="back", font=("Helvetica", 16, "bold"), command=go_back) # back button
        back.pack(side="bottom", fill="x", pady=10)



        conn = sqlite3.connect('notes.sqlite') #connects to the database and creates a notes database if it does not exists
        cur = conn.cursor() # gives you the ability to start doing things in the database
        cur.execute("SELECT notes FROM Files WHERE title = ?", (find_content,)) #change to select
        note_file = cur.fetchone()
        file_text_box = tk.Text(window, height=10, width=40)
        file_text_box.pack(fill=tk.BOTH, expand=True)
        file_text_box.insert(tk.END, note_file[0])
        conn.commit()
        conn.close()

        def resave_file():
            resave_content = file_text_box.get("1.0", tk.END).strip()  # Strip to remove any trailing newline
            conn = sqlite3.connect('notes.sqlite') #connects to the database and creates a notes database if it does not exists
            cur = conn.cursor() # gives you the ability to start doing things in the database
            cur.execute("UPDATE Files SET notes = ? WHERE title = ?", (resave_content, find_content))
            conn.commit()
            conn.close()

        resave =tk.Button(bottom_frame, text="Resave", font=("Helvetica", 16, "bold"), command= resave_file) #resave button
        resave.pack(side="right", fill="x", pady=10)



    find_but = tk.Button(bottom_frame, text="find", font=("Helvetica", 16, "bold"), command=find_file) # find file button
    find_but.pack(side="bottom", fill="x", pady=10)


# a widget opens up and you search the name of file you would like to delete - it then says are you sure and then deletes or goes back
def delete_notes(): 
    destroy_all_widgets()

    delete_page_label= tk.Label(window, text="Type name of file", font=("Helvetica", 16, "bold"))
    delete_page_label.pack()

    file_deleted_label = tk.Label(window, text="The file has been deleted", font=("Helvetica", 16, "bold"))
    file_deleted_label.pack_forget()

    file_noexist_label = tk.Label(window, text="The file does not exist", font=("Helvetica", 16, "bold"))
    file_noexist_label.pack_forget()

    entry_delete = tk.Entry(window, font=("Helvetica", 16, "bold")) #where you will type the name of the file
    entry_delete.pack(side=tk.TOP, fill=tk.X, pady=10)


    # creating a frame at the button to hold the two buttons delete and back
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side="bottom", pady=10)

    back =tk.Button(bottom_frame, text="back", font=("Helvetica", 16, "bold"), command=go_back) # back button
    back.pack(side="left", fill="x", pady=10)



    def delete():
        delete_content = entry_delete.get()

        conn = sqlite3.connect('notes.sqlite') #connects to the database and creates a notes database if it does not exists
        cur = conn.cursor() # gives you the ability to start doing things in the database
        cur.execute("SELECT title FROM Files WHERE title = ?" , (delete_content,))
        check_column = cur.fetchone()
        conn.commit()
        conn.close()

        if delete_content != '':

            if check_column is not None:

                    
                    delete_page_label.pack_forget()
                    file_noexist_label.pack_forget()
                    file_deleted_label.pack(side=tk.TOP, fill=tk.X, pady=10)
            
                    conn = sqlite3.connect('notes.sqlite') #connects to the database and creates a notes database if it does not exists
                    cur = conn.cursor() # gives you the ability to start doing things in the database
                    cur.execute("DELETE FROM Files WHERE title = ?", (delete_content,))
                    conn.commit()
                    conn.close()

            else:
                
                file_noexist_label.pack()
                file_deleted_label.pack_forget()
                delete_page_label.pack_forget()


    delete_but =tk.Button(bottom_frame, text="delete", font=("Helvetica", 16, "bold"), command= delete) # back buttonont
    delete_but.pack(side="bottom", fill="x", pady=10)

   



# initial buttons

add=tk.Button(window, text="Add", font=("Helvetica", 16, "bold"), command=add_notes) #Button 1
add.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
view=tk.Button(window, text="View", font=("Helvetica", 16, "bold"), command=view_notes) #Button 2
view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
delete=tk.Button(window, text="Delete", font=("Helvetica", 16, "bold"), command=delete_notes) #Button 3
delete.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


window.mainloop() #allows you to see the window


