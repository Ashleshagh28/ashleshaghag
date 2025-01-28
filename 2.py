from tkinter import *
import messagebox as tmsg
from PIL import ImageTk,Image


# n, ne, e, se, s, sw, w, nw, or center
window = Tk()
window.geometry("750x600")
window.title("LOGIN PAGE")
window.configure(bg="white")

image = Image.open("pic40.jpg")
width, height = 750, 600

resized_image = image.resize((width,height))

photo = ImageTk.PhotoImage(resized_image)
label = Label(window, image=photo)
label.pack()

def home():
    global window
    window.withdraw()
    global master
    master = Tk()
    master.title("Zenvitality")
    master.geometry("750x600")
    master.configure(bg="grey")

    l1 = Label(master,text="Zenvitality",font="arial 20 bold",bg="black",fg='white',padx=10)
    l1.pack(side=TOP,fill=X)



    master.mainloop()

def libr():
    global window
    window.withdraw()
    global win, c1,c2,c3
    win = Tk()
    win.title("PERSONAL INFORMATION")
    win.geometry("750x600")


    tmsg.showinfo("LOGIN"," Your login Was Succesful")


    l4 = Label(win, text="What Is Your Gender ...?", font="arial 19 bold")
    l4.place(x=300,y=30)
    c1 = Checkbutton(win, text="Male", font="Calibri 16 bold")
    c1.place(x=300,y=100)
    c2 = Checkbutton(win, text="Female", font="calibri 16 bold")
    c2.place(x=300,y=150)
    c3 = Checkbutton(win, text="Preferred Not To Ans", font="calibri 16 bold")
    c3.place(x=300,y=200)

    l3 = Label(win,text="What is Your Age",font="arial 15 bold")
    l3.place(x=300,y=250)

    age = IntVar()
    e3 = Entry(win,width=10,font="arial 20 bold")
    e3.place(x=300,y=300)

    Button(win, text="NEXT", font="arial 15 bold", borderwidth=3, bg="black", fg="white",
           activebackground="#6600ff",command=info).place(x=300,y=400)


    win.mainloop()

def register():
    global window
    window.withdraw()
    global reg, c1, c2, c3
    reg = Tk()
    reg.title("Register")
    reg.geometry("750x600")
    l4 = Label(reg, text="Name", font="times 15 bold")
    l4.place(x=200, y=50)
    l5 = Label(reg, text="Email ID", font="times 15 bold")
    l5.place(x=200, y=100)
    l6 = Label(reg, text="Phone no.", font="times 15 bold")
    l6.place(x=200, y=150)
    l7 = Label(reg, text="Password", font="times 15 bold")
    l7.place(x=200, y=200)
    l8 = Label(reg, text="Confirm password", font="times 15 bold")
    l8.place(x=200, y=250)


    uservalue = StringVar()

    e3 = Entry(reg,textvariable=uservalue,width=30)
    e3.place(x=400,y =50)
    e3 = Entry(reg,textvariable=uservalue,width=30)
    e3.place(x=400, y=100)
    e3 = Entry(reg,textvariable=uservalue,width=30)
    e3.place(x=400,y =150)
    e3 = Entry(reg,textvariable=uservalue,width=30)
    e3.place(x=400, y=200)
    e3 = Entry(reg,textvariable=uservalue,width=30)
    e3.place(x=400, y=250)
    b4 = Button(reg, text="Register", font="arial 10 bold", borderwidth=3, bg="black", fg="white",
           activebackground="#6600ff",command=libr)
    b4.place(x=350, y=350)





    reg.mainloop()




def info():
    global window
    window.withdraw()
    global root,l1,l2,l3,l4,l5,l6,l7,l8
    root = Tk()
    root.title("PERSONAL INFORMATION")
    root.geometry("750x600")

    l9 = Label(root, text="What is Your Main FocusArea...?", font="arial 20 bold")
    l9.place(x=300,y=30)

    l1 = Label(root, text="Improve Flexibility", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l2 = Label(root, text="Relieve stress", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l3 = Label(root, text="Improve sleep Quantity", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l4 = Label(root, text="Burn Caleries", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l5 = Label(root, text="Fix Posture", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l6 = Label(root, text="Releive pain", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l7 = Label(root, text="build strength", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)
    l8 = Label(root, text="promote relaxation", font="calibri 15 bold", borderwidth=3, relief=SUNKEN)

    l1.place(x=300,y=100)
    l2.place(x=300,y=150)
    l3.place(x=300,y=200)
    l4.place(x=300,y=250)
    l5.place(x=300,y=300)
    l6.place(x=300,y=350)
    l7.place(x=300,y=400)
    l8.place(x=300,y=450)

    Button(root, text="NEXT", font="arial 15 bold", borderwidth=3, bg="black", fg="white",
           activebackground="#6600ff",command=home).place(x=350,y=550)

    c1 = Checkbutton(root)
    c1.place(x=500 , y=100)
    c2 = Checkbutton(root )
    c2.place(x=500,y=150)
    c3 = Checkbutton(root )
    c3.place(x=500,y=200)
    c4 = Checkbutton(root )
    c4.place(x=500,y=250)
    c5 = Checkbutton(root )
    c5.place(x=500,y=300)
    c6 = Checkbutton(root )
    c6.place(x=500,y=350)
    c7 = Checkbutton(root )
    c7.place(x=500,y=400)
    c8 = Checkbutton(root )
    c8.place(x=500,y=450)

    root.mainloop()




l1 = Label(window,text="Zenvitality",font="times 30 italic")

usid = Label(window, text='USER ID',font="times 15 bold")
paswrd = Label(window, text='PASSWORD',font="times 15 bold",highlightcolor="red")
e1 = Entry(window, width=20,font="times 10 bold",borderwidth=5)
e2 = Entry(window, width=20,font="times 10 bold",borderwidth=5)
b1 = Button(window, text=' LOGIN',borderwidth=3,relief=SUNKEN, height=1, width=15,font="Times 13 bold italic"
            ,activebackground="green",command=libr)

l3 = Label(window,text="Don't Have Any Account..?")
l3.place(x=250,y=320)
b2 = Button(window,text="Register",font="times 10 bold",command=register)
b2.place(x=400,y=320)
# wel.place(x=160,y=20)
# lib.place(x=110,y=70)
l1.place(x=270,y=60)
usid.place(x=220, y=200)
paswrd.place(x=220, y=270)
e1.place(x=350, y=200)
e2.place(x=350, y=270)
b1.place(x=300, y=350)

















window.mainloop()