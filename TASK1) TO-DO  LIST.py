#importing libraries
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk
#creating main window
root=Tk()
root.geometry("650x650")
#setting window icon
root.iconphoto(False,tk.PhotoImage(file="to do list.png"))

l1=Label(root,text="TO-DO LIST APPLICATION",font="Arial 22 bold",fg="darkorchid4",padx=20,pady=20)
l1.place(x=145,y=15)
#function to add the task from the entry widget into the listbox
def add():
    list.insert(END, entry.get())
    #deleting the task from the entry widget when the task is added into the listbox
    entry.delete(0,END)
    print(list.get(END))


#function to delete a specific task from the listbox
def delete():
    selected_index = list.curselection()
    if selected_index:
        list.delete(selected_index)

#function to save all the tasks present in the listbox into a text file
def save():
    with open("TO-DO LIST.txt",'a') as f:
        for item in list.get(0,END):
            f.write(item + "\n")
        f.close()

root.title("TO-DO LIST")
l2=Label(root,text="ENTER YOUR TASK HERE :",font="arial 14 bold",fg="blue4")
l2.place(x=45,y=125)

l3=Label(root,text="TO-DO LIST ",font="arial 15 bold ",fg="deeppink3")
l3.place(x=245,y=185)

#creating an entry to get user's tasks
entry=Entry(root,width=30,font="arial 13")
entry.place(x=320,y=127)

#opening a delete image and creating a button out of it which will delete a task from the listbox
picture1=Image.open("delete.png")
picture1=picture1.resize((45,45))
delete_image=ImageTk.PhotoImage(picture1)
delete_button=Button(root,text="delete",image=delete_image,command=delete,borderwidth=0,cursor="hand2")
delete_button.place(x=555,y=320)

#opening an add task image and creating a button out of it which will add a task into the listbox
picture2=Image.open("add_task.png")
picture2=picture2.resize((45,45))
add_task_image=ImageTk.PhotoImage(picture2)
add_task_image_button=Button(root,image=add_task_image,command=add,borderwidth=0,cursor="hand2")
add_task_image_button.place(x=551,y=250)

#opening a save file image and creating a button out of it which will save the tasks from the listbox into a text file
picture3=Image.open("save_file.png")
picture3=picture3.resize((40,40))
save_to_file_image=ImageTk.PhotoImage(picture3)
save_to_file_image_button=Button(root,image=save_to_file_image,command=save,borderwidth=0,cursor="hand2")
save_to_file_image_button.place(x=558,y=400)

#creating a listbox
list=Listbox(root,width=40,height=19,font="arial 13 bold")
list.place(x=127,y=230)

image = Image.open("to do list.png")
image = image.resize((80, 80))
list_image = ImageTk.PhotoImage(image)
l9 = Label(image=list_image)
l9.place(x=60,y=15)
mainloop()