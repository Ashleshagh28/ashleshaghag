from customtkinter import *
from PIL import Image,ImageTk
app = CTk()
app.geometry("1150x650")
app.title("Personal Information")
app.config(bg="#D9EDBF")
app.resizable(False,False)



def go():
    app.destroy()
    import hatha2
def home():
    app.destroy()
    import home2
def contact():
    pass

f1 = CTkFrame(app,width=1200,height=50,fg_color="#FF9800",border_width=0,border_color="#400080",bg_color="white",corner_radius=0)
f1.place(x=0,y=0)
l1 = CTkLabel(f1,text="Zenvaitility",font=("times",25,"italic"),fg_color="#FF9800",text_color="black",)
l1.place(x=65,y=15)
bg_img = CTkImage(dark_image=Image.open("icons8-health-100.png"),size=(25,20))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=30,y=15)

b1=CTkButton(f1,text="Home",fg_color="#FF9800",text_color="black",font=("arial",16),width=20,hover_color="#90D26D",command=home)
b1.place(x=700,y=15)
b1=CTkButton(f1,text="about us",fg_color="#FF9800",text_color="black",font=("arial",16),width=20,hover_color="#90D26D")
b1.place(x=800,y=15)
b1=CTkButton(f1,text="contact Us",fg_color="#FF9800",text_color="black",font=("arial",16),width=20,hover_color="#90D26D"
             ,command=contact)
b1.place(x=900,y=15)
b1=CTkButton(f1,text="Help",fg_color="#FF9800",text_color="black",font=("arial",16),width=20,hover_color="#90D26D")
b1.place(x=1030,y=15)


bg_img = CTkImage(dark_image=Image.open("pic53.jpg"),size=(500,500))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=650,y=60)

f3 = CTkFrame(app,fg_color="#FF9800",width=630,height=560,corner_radius=40,bg_color="#D9EDBF")
f3.place(x=0,y=70)

l1 = CTkLabel(f3,text="1.Hatha Yoga:--",text_color="black",font=("times",40,"italic"),fg_color="#FF9800")
l1.place(x=20,y=10)
l2 = CTkLabel(f3,text="""Hatha Yoga, school of Yoga that stresses mastery of the body as a 
way of attaining a state of spiritual perfection in which the mind is withdrawn from external objects.
 Hatha Yoga traces its origins especially to Gorakhnath, the legendary 11th-century founder of the
Kanphata Yogis, but it grew out of yogic traditions dating back
 at least as far as Patanjali (2nd century BCE or 5th century CE), 
 author of the Hindu classics the Yoga-sutras and the 
 Mahabhasya (“Great Commentary”).

Category: Arts & Culture
Sanskrit: “Discipline of Force”
Related Topics: exercise
Hatha Yoga places great importance on diet, purificatory processes, regulation of breathing 
(Pranayama), and the adoption of bodily postures called asanas, which structure a program 
of physical exertion. A common asana is the padmasana (“lotus posture”), in which the 
crossed feet rest on the opposite thighs. This is the position in which many Hindu and Buddhist
gods are often depicted, but it is only one of dozens described in Hatha Yoga treatises. The “salute 
to the sun” is a well-known sequence of 12 asanas performed in a fluid movement.

Hatha Yoga has grown in popularity in the West as a form of exercise that develops
strength, flexibility,bodily relaxation, and mental concentration. Its true object,
however, is to awaken the dormant energy (shakti) of Shiva that animates the subtle 
body but is concealed behind the gross human frame. The subtle anatomy containing it is usually
described as a series of lotiform chakras (“wheels”) rising from the anal or genital 
area to the top of the head. 
Through the forceful suppression of physical and mental activity, 
the female shakti is enabled to rise along the 
chakras and unite with the male Shiva in the uppermost chakra, a union 
indistinguishable from enlightenment and 
even immortality.""",text_color="black",font=("arial",15),bg_color="transparent")
l2.place(x=0,y=70)


b2 = CTkButton(app,text="NEXT",border_width=0,fg_color="#ff0066",bg_color="#D9EDBF",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#90D26D"
               ,height=40,width=150,command=go)
b2.place(x=700,y=600)


app.mainloop()
