from customtkinter import *
from PIL import Image,ImageTk
app = CTk()
app.geometry("1100x700")
app.title("Personal Information")
app.config(bg="white")
app.resizable(False,False)


def delete():
    pass

def slider():
    def delete():
        f2.destroy()



    f2 = CTkFrame(app, width=250, height=900,fg_color="#0c4a7b",border_width=0,border_color="#0c4a7b"
                  ,bg_color="#0c4a7b")
    f2.place(x=0, y=50)
    b2 = CTkButton(f2,text="X",text_color="white",width=20,height=30,border_width=0,corner_radius=30
               ,font=("arial",25,"bold"),bg_color="black",fg_color="black",hover_color="#3c286e",command=delete)
    b2.place(x=10,y=10)



def contact():
    app.destroy()
    import contact

def mental():
    app.destroy()
    import mental


def physical():
    app.destroy()
    import physical


bg_img = CTkImage(dark_image=Image.open("pic 52.jpg"),size=(1100,700))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.pack()

f1 = CTkFrame(app,width=1100,height=50,fg_color="#3c286e",border_width=0,border_color="#400080",bg_color="#3c286e")
f1.place(x=0,y=0)
l1 = CTkLabel(f1,text="Zenvaitality",font=("arial",16),fg_color="#3c286e",text_color="white",)
l1.place(x=95,y=15)
bg_img = CTkImage(dark_image=Image.open("icons8-health-100.png"),size=(25,20))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=60,y=15)

b1=CTkButton(f1,text="Home",fg_color="#3c286e",text_color="white",font=("arial",16),width=20,hover_color="#0c4a7b")
b1.place(x=600,y=15)
b1=CTkButton(f1,text="about us",fg_color="#3c286e",text_color="white",font=("arial",16),width=20,hover_color="#0c4a7b")
b1.place(x=700,y=15)
b1=CTkButton(f1,text="contack Us",fg_color="#3c286e",text_color="white",font=("arial",16),width=20,hover_color="#0c4a7b"
             ,command=contact)
b1.place(x=800,y=15)
b1=CTkButton(f1,text="Help",fg_color="#3c286e",text_color="white",font=("arial",16),width=20,hover_color="#0c4a7b")
b1.place(x=930,y=15)

b1 = CTkButton(app,text="Path For Mental Fitness",text_color="white",width=400,height=50,border_width=0,corner_radius=40
               ,fg_color="#1a75ff",bg_color="#3c286e",font=("arial",20),command=mental)
b1.place(x=530,y=415)
b1 = CTkButton(app,text="Path For Physical Fitness",text_color="white",width=400,height=50,border_width=0,corner_radius=40
               ,font=("arial",20),bg_color="#3c286e",command=physical)
b1.place(x=580,y=470)

b1 = CTkButton(app,text="Path For Physical Fitness",text_color="white",width=400,height=50,border_width=0,corner_radius=40
               ,font=("arial",20),bg_color="#3c286e",command=physical)
b1.place(x=580,y=470)

b1 = CTkButton(app,text="☰",text_color="white",width=10,height=30,border_width=0,corner_radius=40
               ,font=("arial",20),bg_color="#3c286e",fg_color="#3c286e",command=slider)
b1.place(x=10,y=15)


















app.mainloop()
