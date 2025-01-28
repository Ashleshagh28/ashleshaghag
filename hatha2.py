import webbrowser
from customtkinter import *
from PIL import Image
app = CTk()
app.geometry("1150x800")
app.title("Personal Information")
app.config(bg="#D9EDBF")
app.resizable(False,False)


def home():
    app.destroy()
    import phy2
def go():
    video_url = "Hatha Yoga _ Traditional Yoga Practice _ Full Body Class (All Levels).mp4"
    webbrowser.open_new(video_url)


f1 = CTkFrame(app,width=2 ,height=600,fg_color="black")
f1.place(x=550,y=30)
l1 = CTkLabel(app,text_color="#90D26D",text="Hatha Yoga Posses",font=("arial",30,"italic"),fg_color="#2C7865",corner_radius=20
              ,bg_color="#D9EDBF")
l1.place(x=600,y=20)

bg_img = CTkImage(dark_image=Image.open("hatha1.jpg"),size=(280,210))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=570,y=60)
bg_img = CTkImage(dark_image=Image.open("hatha2.jpg"),size=(280,210))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=860,y=60)
bg_img = CTkImage(dark_image=Image.open("hatha3.jpg"),size=(280,210))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=570,y=280)
bg_img = CTkImage(dark_image=Image.open("hatha4.jpg"),size=(280,210))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=860,y=280)
bg_img = CTkImage(dark_image=Image.open("hatha5.jpg"),size=(280,210))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=700,y=500)

f2 = CTkFrame(app,width=500,height=650,fg_color="#FF9800",corner_radius=50,bg_color="#D9EDBF")
f2.place(x=10,y=20)

l3 = CTkLabel(f2,text_color="#90D26D",text="Benefits Of Hatha Yoga",font=("arial",30,"italic"),fg_color="#2C7865"
              ,corner_radius=20)
l3.place(x=70,y=10)

l4 = CTkLabel(f2,text_color="black",text="1. Helps you recognize your hidden physical and mental potential",font=("arial",20))
l4.place(x=0,y=70)
l5 = CTkLabel(f2,text_color="black",text="2. Helps you achieve a flexible and strong body",font=("arial",20))
l5.place(x=0,y=100)
l6 = CTkLabel(f2,text_color="black",text="3. Opens energy channels, which in turn allow"
                                         " spiritual energy to flow freely",font=("arial",20))
l6.place(x=0,y=130)
l7 = CTkLabel(f2,text_color="black",text="4. Massage and tone your internal organs",font=("arial",20))
l7.place(x=0,y=160)
l8 = CTkLabel(f2,text_color="black",text="5. They also bring balance to internal and glandular functions Help",font=("arial",20))
l8.place(x=0,y=190)
l9 = CTkLabel(f2,text_color="black",text="6. Helps you achieve enlightenment",font=("arial",20))
l9.place(x=0,y=220)

l10 = CTkLabel(f2,text=" Learn Yoga From Our Video Tutorial ",text_color="#90D26D",font=("times",30),fg_color="#2C7865"
               ,corner_radius=30)
l10.place(x=10,y=350)

b2 = CTkButton(f2,text="Click Here",border_width=0,fg_color="#ff0066",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#33ff77",bg_color="#FF9800"
               ,height=40,width=150,command=go)
b2.place(x=160,y=450)

b4 = CTkButton(app,text="<-",border_width=0,fg_color="#ff0066",text_color="white",bg_color="#D9EDBF"
               ,font=("arial",15),corner_radius=20,hover_color="#33ff77"
               ,height=30,width=30,command=home)
b4.place(x=1050,y=20)






app.mainloop()