from customtkinter import *
from PIL import Image,ImageTk
app = CTk()
app.geometry("1150x650")
app.title("Personal Information")
app.config(bg="#F8F6E3")
app.resizable(False,False)



def go():
    app.destroy()
    import bala2
def home():
    app.destroy()
    import home2
def contact():
    pass

f1 = CTkFrame(app,width=1200,height=50,fg_color="#6AD4DD",border_width=0,border_color="#400080",bg_color="white",corner_radius=0)
f1.place(x=0,y=0)
l1 = CTkLabel(f1,text="Zenvaitility",font=("times",25),fg_color="#6AD4DD",text_color="black",)
l1.place(x=65,y=15)
bg_img = CTkImage(dark_image=Image.open("icons8-health-100.png"),size=(25,20))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=30,y=15)

b1=CTkButton(f1,text="Home",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#7AA2E3",command=home)
b1.place(x=700,y=15)
b1=CTkButton(f1,text="about us",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#7AA2E3")
b1.place(x=800,y=15)
b1=CTkButton(f1,text="contact Us",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#7AA2E3"
             ,command=contact)
b1.place(x=900,y=15)
b1=CTkButton(f1,text="Help",fg_color="#6AD4DD",text_color="black",font=("arial",16),width=20,hover_color="#7AA2E3")
b1.place(x=1030,y=15)

bg_img = CTkImage(dark_image=Image.open("Picture3.jpg"),size=(400,400))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=700,y=70)

f3 = CTkFrame(app,fg_color="#97E7E1",width=630,height=560,corner_radius=40,bg_color="#F8F6E3")
f3.place(x=0,y=70)

l1 = CTkLabel(f3,text="1.Balasana:--",text_color="black",font=("arial",40,"italic"),fg_color="#97E7E1")
l1.place(x=20,y=10)
l2 = CTkLabel(f3,text="""Balasana or resting pose has therapeutic 
benefits for anxiety, stress, depression, sleeping difficulties and
fatigue. 
This asana may activate the limbic system which helps the body respond 
to intense emotions such as fear and anger by activating the fight or 
flight response. 
Balasana is so named as it refers to the basic fetal position and the
subsequent child-like vulnerabilities that may be experienced as a 
result of the pose. 
Many even believe assuming this pose allows one to reconnect to 
primal memories of being in the womb. 
While bowing one’s forehead to the floor can often indicate surrender 
or weakness in the West, it is a dignified act of humility in its 
original Indian context.Balasana provides the following spiritual benefits: 
•Encourages introspection and contemplation 
•Practices mindfulness 
•Stimulates the third eye chakra 
•Aligns breath and organs with spiritual energies 
•Displays honor, devotion and humanity.
""",text_color="black",font=("Century Gothic",17,"bold"),bg_color="transparent")
l2.place(x=0,y=70)


b2 = CTkButton(app,text="NEXT",border_width=0,fg_color="#7AA2E3",bg_color="#D9EDBF",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#97E7E1"
               ,height=40,width=150,command=go)
b2.place(x=700,y=600)


app.mainloop()
