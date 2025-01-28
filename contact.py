from customtkinter import *
from PIL import Image,ImageTk
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
    tmsg.showinfo("Message","Your Response Submitted Successfully")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

f1 =CTkFrame(app,width=520,height=550,corner_radius=30,bg_color="#3c286e")
f1.place(x=10,y=20)
f2 =CTkFrame(app,width=500,height=550,corner_radius=30,bg_color="#3c286e")
f2.place(x=550,y=20)
l1 = CTkLabel(f1,text="Lets talk About",text_color="white",font=("arial",50))
l1.place(x=10,y=10)
l1 = CTkLabel(f1,text="Thoughts & Opinions.",text_color="white",font=("arial",50))
l1.place(x=10,y=70)
l1 = CTkLabel(f1,text="Our Location",text_color="white",font=("arial",20,"bold"))
l1.place(x=10,y=150)
l1 = CTkLabel(f1,text="Universal college Of Engineering,kaman",text_color="white",font=("arial",15))
l1.place(x=10,y=190)
l1 = CTkLabel(f1,text="sales@zenvaitaility.com",text_color="white",font=("arial",15))
l1.place(x=10,y=250)
l1 = CTkLabel(f1,text="Email Address",text_color="white",font=("arial",20,"bold"))
l1.place(x=10,y=220)
l1 = CTkLabel(f1,text="Supports@Zenvaitaility.com",text_color="white",font=("arial",15))
l1.place(x=10,y=280)
l1 = CTkLabel(f1,text="Contact Numbers",text_color="white",font=("arial",20,"bold"))
l1.place(x=10,y=310)
l1 = CTkLabel(f1,text="+91-9022345682",text_color="white",font=("arial",15))
l1.place(x=10,y=350)
l1 = CTkLabel(f1,text="91-7837639051",text_color="white",font=("arial",15))
l1.place(x=10,y=380)

e1 = CTkEntry(f2,placeholder_text="Full Name",width=450,height=60)
e1.place(x=10,y=20)
e2 = CTkEntry(f2,placeholder_text="Email",width=450,height=60)
e2.place(x=10,y=100)
e3 = CTkEntry(f2,placeholder_text="Enter Your Number",width=450,height=60)
e3.place(x=10,y=180)
e4 = CTkEntry(f2,placeholder_text="Message",width=450,height=180)
e4.place(x=10,y=260)

b1 = CTkButton(f2,text="Send Message",font=("arial",17,"bold"),width=200,height=50,corner_radius=30,
               fg_color="#0c4a7b",command=msg,hover_color="#835187")
b1.place(x=150,y=460)

b4 = CTkButton(app,text="<-",border_width=2,fg_color="#ff0066",text_color="white",bg_color="white"
               ,font=("arial",15),corner_radius=20,border_color="#f2f2f2"
               ,height=40,width=50,command=home)
b4.place(x=1020,y=30)








app.mainloop()