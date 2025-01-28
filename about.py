from customtkinter import *
from PIL import Image
app = CTk()
app.geometry("1150x800")
app.title("Personal Information")
app.config(bg="#3c286e")

def home():
    app.destroy()
    import home2

f1 = CTkFrame(app,width=800,height=210,corner_radius=30,bg_color="#3c286e")
f1.place(x=230,y=40)

bg_img = CTkImage(dark_image=Image.open("yogitamiss.jpeg"),size=(190,190))
bg_lab = CTkLabel(f1,image=bg_img,text="")
bg_lab.place(x=570,y=7)
l1 = CTkLabel(f1,text_color="white",text="Project Faculty Head",font=("times",30,"italic"))
l1.place(x=200,y=5)
l1 = CTkLabel(f1,text_color="white",text="Dr.Yogita Mane",font=("times",30,"bold"))
l1.place(x=30,y=50)
l1 = CTkLabel(f1,text_color="white",text="Head Of Department(HOD)-(Information Technology)",font=("times",20,"bold"))
l1.place(x=20,y=85)




f2 = CTkFrame(app,width=250,height=400,corner_radius=30,bg_color="#3c286e")
f2.place(x=10,y=270)
bg_img = CTkImage(dark_image=Image.open("rohit.jpg"),size=(190,190))
bg_lab = CTkLabel(f2,image=bg_img,text="")
bg_lab.place(x=30,y=50)
l1 = CTkLabel(f2,text_color="white",text="Group Leader",font=("times",30,"italic"))
l1.place(x=30,y=5)
l1 = CTkLabel(f2,text_color="white",text="Rohit Saundalkar",font=("times",25))
l1.place(x=35,y=245)
l1 = CTkLabel(f2,text_color="white",text="S.E.I.T (31)",font=("times",20))
l1.place(x=75,y=270)
l1 = CTkLabel(f2,text_color="white",text="""Worked On
fronted & Backend""",font=("times",20))
l1.place(x=35,y=300)




f3 = CTkFrame(app,width=250,height=400,corner_radius=30,bg_color="#3c286e")
f3.place(x=300,y=270)
bg_img = CTkImage(dark_image=Image.open("chinmai.jpg"),size=(190,190))
bg_lab = CTkLabel(f3,image=bg_img,text="")
bg_lab.place(x=30,y=50)
l1 = CTkLabel(f3,text_color="white",text="Group Member",font=("times",30,"italic"))
l1.place(x=30,y=5)
l1 = CTkLabel(f3,text_color="white",text="Chinmai Patil",font=("times",25))
l1.place(x=45,y=245)
l1 = CTkLabel(f3,text_color="white",text="S.E.I.T (22)",font=("times",20))
l1.place(x=75,y=270)
l1 = CTkLabel(f3,text_color="white",text="""Worked On
Resources & Info""",font=("times",20))
l1.place(x=35,y=300)





f4 = CTkFrame(app,width=250,height=400,corner_radius=30,bg_color="#3c286e")
f4.place(x=600,y=270)
bg_img = CTkImage(dark_image=Image.open("pratish.jpg"),size=(190,190))
bg_lab = CTkLabel(f4,image=bg_img,text="")
bg_lab.place(x=30,y=50)
l1 = CTkLabel(f4,text_color="white",text="Group Member",font=("times",30,"italic"))
l1.place(x=35,y=5)
l1 = CTkLabel(f4,text_color="white",text="Pratish Bhongle",font=("times",25))
l1.place(x=45,y=245)
l1 = CTkLabel(f4,text_color="white",text="S.E.I.T (59)",font=("times",20))
l1.place(x=75,y=270)
l1 = CTkLabel(f4,text_color="white",text="""Worked On Fronted""",font=("times",20))
l1.place(x=45,y=300)


f5 = CTkFrame(app,width=250,height=400,corner_radius=30,bg_color="#3c286e")
f5.place(x=880,y=270)
bg_img = CTkImage(dark_image=Image.open("nandan.jpg"),size=(190,190))
bg_lab = CTkLabel(f5,image=bg_img,text="")
bg_lab.place(x=30,y=50)
l1 = CTkLabel(f5,text_color="white",text="Group Member",font=("times",30,"italic"))
l1.place(x=30,y=5)
l1 = CTkLabel(f5,text_color="white",text="Nandan Savant",font=("times",25))
l1.place(x=45,y=245)
l1 = CTkLabel(f5,text_color="white",text="S.E.I.T (45)",font=("times",20))
l1.place(x=75,y=270)
l1 = CTkLabel(f5,text_color="white",text="""Worked On Information""",font=("times",20))
l1.place(x=35,y=300)




b4 = CTkButton(app,text="<-",border_width=0,fg_color="#ff0066",text_color="white",bg_color="#3c286e"
               ,font=("arial",15),corner_radius=20,hover_color="#33ff77"
               ,height=30,width=30,command=home)
b4.place(x=1070,y=5)







app.mainloop()