from cProfile import label

from email import message
from encodings.utf_8 import encode
from tkinter import*
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="grey")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="decrypt",font="aria",fg="white",bg="black").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=5)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("encryption","Input password")


    elif password !="1234":
        messagebox.showerror("encryption","Invalid password")    

    




def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="red")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="encrypt",font="aria",fg="white",bg="black").place(x=10,y=0)
        text2=Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=5)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input password")


    elif password !="1234":
        messagebox.showerror("encryption","Invalid password")    

    




def main_screen():

    global screen 
    global code
    global text1


    screen=Tk()
    screen.geometry("375x398")
    screen.configure(bg="yellow")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    #textbox label
    Label(text="Enter text for encryption and decryption",fg="red",font=("calbri",13)).place(x=10,y=10)

    #textbox
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=10)
    text1.place(x=10,y=50,width=355,height=100)


    screen.title("encrpytNdecrypt")

    #key label
    Label(text="enter secret key",fg="red",font=("calibri",13)).place(x=10,y=170)

    #key textbox
    code=StringVar()
    Entry(textvariable=code,width=12,bd=5,font=("arial",20),show="*").place(x=10,y=200)

    #buttons
    Button(text="ENC",height="2",width=5,bg="pink",fg="black",bd=5,command=encrypt).place(x=10,y=250)
    Button(text="DEC",height="2",width=5,bg="pink",fg="black",bd=5,command=decrypt).place(x=120,y=250)
    Button(text="reset",height="2",width=5,bg="purple",fg="black",bd=5,command=reset).place(x=60,y=300)
    
    screen.mainloop()

main_screen()    

