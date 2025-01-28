from customtkinter import *
from PIL import Image,ImageTk
app = CTk()
app.geometry("1150x650")
app.title("Personal Information")
app.config(bg="#F8F6E3")
app.resizable(False,False)



def go():
    app.destroy()
    import adho2
def home():
    app.destroy()
    import home2
def contact():
    pass

f1 = CTkFrame(app,width=1200,height=50,fg_color="#6AD4DD",border_width=0,border_color="#400080",bg_color="white",corner_radius=0)
f1.place(x=0,y=0)
l1 = CTkLabel(f1,text="Zenvaitility",font=("times",25,"italic"),fg_color="#6AD4DD",text_color="black",)
l1.place(x=65,y=15)
bg_img = CTkImage(dark_image=Image.open("icons8-health-100.png"),size=(25,20))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=30,y=15)

b1=CTkButton(f1,text="Home",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#90D26D",command=home)
b1.place(x=700,y=15)
b1=CTkButton(f1,text="about us",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#90D26D")
b1.place(x=800,y=15)
b1=CTkButton(f1,text="contact Us",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#90D26D"
             ,command=contact)
b1.place(x=900,y=15)
b1=CTkButton(f1,text="Help",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#90D26D")
b1.place(x=1030,y=15)


bg_img = CTkImage(dark_image=Image.open("Men.jpeg"),size=(500,500))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=650,y=60)

f3 = CTkFrame(app,fg_color="#97E7E1",width=630,height=560,corner_radius=40,bg_color="#F8F6E3")
f3.place(x=0,y=70)

l1 = CTkLabel(f3,text="1.Adho Mukha Svanasana:--",text_color="black",font=("arial",40),fg_color="#97E7E1")
l1.place(x=20,y=10)
l2 = CTkLabel(f3,text="""Adho mukha svanasana is a foundational yoga asana that requires 
flexibility and upper body strength. In this asana, the body forms an inverted “V” with the feet 
and hands pressing into the ground and the hips pushing to the sky. As well as a range of 
physical benefits, it is believed to calm the mind, yet energize and rejuvenate the body. 
The name comes from the 
Sanskrit adhas, meaning 
“down,” mukha, meaning “face,” svana, meaning “dog,” and asana, meaning “pose.” 
The common English name for adho mukha svanasana is downward-facing dog pose, 
or simply downward dog Adho mukha svanasana is part of the surya namaskara (sun salutation) 
series in many types of yoga. It serves as a transitional resting pose and is often one 
of the first poses someone new to yoga learns. 
Traditionally, this asana is believed to activate a number of the chakras, including the 
manipura and ajna chakras. Activating the manipura chakra through adho mukha svanasana 
is thought to dispel fear and insecurity, while the ajna chakra stimulates perception and inspiration. 
As an inverted pose, adho mukha svanasana gets blood and body fluids flowing in 
the opposite direction by reversing the action of gravity. The inversion is also 
thought to provide a different perspective on an emotional level, 
boosting confidence. """,text_color="black",font=("arial",15),bg_color="transparent")
l2.place(x=0,y=70)


b2 = CTkButton(app,text="NEXT",border_width=0,fg_color="#7AA2E3",bg_color="#D9EDBF",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#90D26D"
               ,height=40,width=150,command=go)
b2.place(x=700,y=600)


app.mainloop()
