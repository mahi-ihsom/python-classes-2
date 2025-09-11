#getting started with widgets
from tkinter import *
from datetime import date
root= Tk()
root.title("getting started with widgets !!!")
root.geometry("400x300")
lb1= Label(text= "hey there !", fg= "white", bg= "#C5A4E1", height= 1, width= 300)
name_lb1= Label(text= "full name", bg= "#8ABCDE")
name_entry= Entry()
def display():
    name= name_entry.get()
    global message
    message= "welcome to the application.  \ntodays date: "
    greet= "hello."+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box= Text(height= 3)
btn= Button(text= "start", command=display, height=1, bg= "#713DA2", fg= "white")
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()