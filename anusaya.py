from customtkinter import *
from PIL import Image,ImageTk
app = CTk()
app.geometry("1150x650")
app.title("Personal Information")
app.config(bg="#D9EDBF")
app.resizable(False,False)



def go():
    app.destroy()
    import anusaya2
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


bg_img = CTkImage(dark_image=Image.open("pic58.jpg"),size=(500,500))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=650,y=60)

f3 = CTkFrame(app,fg_color="#FF9800",width=630,height=560,corner_radius=40,bg_color="#D9EDBF")
f3.place(x=0,y=70)

l1 = CTkLabel(f3,text="1.Anusara Yoga:--",text_color="black",font=("times",40,"italic"),fg_color="#FF9800")
l1.place(x=20,y=10)
l2 = CTkLabel(f3,text="""The meaning of the word Anusara
The Sanskrit term Anusara translates to “listening to your heart,
“opening to grace,” “aligning with the divine”, or “flowing with grace” 
depending on the interpretation. The word Anusara is pronounced “AHN-yoo-SAH-rah”).
The Anusara yoga practice
Anusara yoga is a type of Hatha yoga with a primary focus on alignment. 
However, it's not all about physical poses (like Bikram) as it's known as a very 
heart-centered yoga practice. So, as well as finding alignment in the asanas, the 
method teaches you to align your body, heart, and mind in a way that opens you to 
the supreme consciousness.
Anusara yoga is based on the non-dual Tantric philosophy of intrinsic goodness. 
Anusara yoga's philosophy follows the “Universal Principles of Alignment,”. 
The first principle of Anusara yoga is to set the foundation and “open to grace.
” This principle is about setting an intention, becoming present, and softening the 
physical body to allow the heart to expand.
Anusara methodology also includes ‘the 3 A's”:
Attitude – using the power of the heart as the force behind every action.
Alignment – mindful awareness of how each aspect of ourselves is interconnected.
Action – the body's natural flow of energy that provides stability and freedom.""",text_color="black",font=("arial",20),bg_color="transparent")
l2.place(x=0,y=70)


b2 = CTkButton(app,text="NEXT",border_width=0,fg_color="#ff0066",bg_color="#D9EDBF",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#90D26D"
               ,height=40,width=150,command=go)
b2.place(x=700,y=600)


app.mainloop()
