from customtkinter import *
import messagebox as tmsg
app = CTk()
app.geometry("1100x600")
app.title("Personal Information")
app.config(bg="#3c286e")
app.resizable(False,False)

def home():
    app.destroy()
    import home2
def msg():
    tmsg.showinfo("Message", "Your Response Submitted Successfully")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

c1 = CTkLabel(app,text="How Can We Help",text_color="black",font=
("times",35),bg_color="#3c286e")
c1.place(x=410,y=10)

f1 = CTkFrame(app,width=500,height=550,corner_radius=50,bg_color="#3c286e")
f1.place(x=300,y=50)

l2 = CTkLabel(f1,text="Desribe the Problem you're having",font=("times",20),text_color="white")
l2.place(x=20,y=10)

e1 = CTkEntry(f1,width=400,height=50,placeholder_text="Resending a campeign")
e1.place(x=20,y=50)
l2 = CTkLabel(f1,text="Give us the details",font=("times",20),text_color="white")
l2.place(x=20,y=110)

e2 = CTkEntry(f1,width=400,height=200,placeholder_text="type here.....")
e2.place(x=20,y=150)

l2 = CTkLabel(f1,text="Your contact Details",font=("times",20),text_color="white")
l2.place(x=20,y=350)
e3 = CTkEntry(f1,width=200,height=40,placeholder_text="Email")
e3.place(x=20,y=400)
e4 = CTkEntry(f1,width=200,height=40,placeholder_text="contact no")
e4.place(x=240,y=400)

b1 = CTkButton(f1,text="Send Message",font=("arial",17,"bold"),width=200,height=50,corner_radius=30,
               fg_color="#0c4a7b",command=msg,hover_color="#835187")
b1.place(x=150,y=460)

b4 = CTkButton(app,text="<-",border_width=0,fg_color="#ff0066",text_color="white",bg_color="#3c286e"
               ,font=("arial",15),corner_radius=20,hover_color="#33ff77"
               ,height=30,width=30,command=home)
b4.place(x=1050,y=20)





app.mainloop()