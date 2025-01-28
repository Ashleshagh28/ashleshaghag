from customtkinter import *
from PIL import Image,ImageTk
app = CTk()
app.geometry("1100x600")
app.title("Personal Information")
app.config(bg="white")
app.resizable(False,False)

def go():
    app.destroy()
    import home2




f1 = CTkFrame(app,width=900,height=450,fg_color="#D9D9D9",corner_radius=30,bg_color="white")
f1.place(x=90,y=90)

f2 = CTkFrame(f1,width=2,height=300,corner_radius=30,fg_color="black")
f2.place(x=450,y=30)
# bg_img = CTkImage(dark_image=Image.open("pic 49.jpg"),size=(400,400))
# bg_lab = CTkLabel(app,image=bg_img,text="")
# bg_lab.place(x=600,y=100)
l1 = CTkLabel(app,text="Zenvaitality",font=("impact",25),bg_color="white",text_color="orange")
l1.place(x=50,y=30)

bg_img = CTkImage(dark_image=Image.open("icons8-health-100.png"),size=(30,30))
bg_lab = CTkLabel(app,image=bg_img,text="")
bg_lab.place(x=15,y=30)


l1 = CTkLabel(f1,text="What Is Your Gender...?",font=("arial",25,"bold"),text_color="black")
l1.place(x=40,y=40)

c1 = CTkRadioButton(f1,text="Male",text_color="black",font=("arial",17,"bold"),radiobutton_width=17,radiobutton_height=17)
c1.place(x=40,y=120)
c1 = CTkRadioButton(f1,text="Female",text_color="black",font=("arial",17,"bold"),radiobutton_width=17,radiobutton_height=17)
c1.place(x=40,y=150)
c1 = CTkRadioButton(f1,text="Preferred Not To Ans",text_color="black",radiobutton_width=17,radiobutton_height=17
                    ,font=("arial",17,"bold"))
c1.place(x=40,y=180 )

l3 = CTkLabel(f1,text="Enter Your Age",text_color="black",font=("arial",25,"bold"))
l3.place(x=70,y=250)
e2 = CTkEntry(f1,width=100)
e2.place(x=150,y=300)

l4 = CTkLabel(f1,text="What is Focus Area....?",text_color="black",font=("arial",25,"bold"))
l4.place(x=500,y=30)

c2=CTkCheckBox(f1,text="Improve Flexibility",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c2.place(x=500,y=80)
c3=CTkCheckBox(f1,text="Relieve Stress",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c3.place(x=500,y=110)
c4=CTkCheckBox(f1,text="Improve Sleep Qauntity",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c4.place(x=500,y=140)
c5=CTkCheckBox(f1,text="Burn Caleries",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c5.place(x=500,y=170)
c6=CTkCheckBox(f1,text="Fix Posture",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c6.place(x=500,y=200)
c7=CTkCheckBox(f1,text="Relieve pain",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c7.place(x=500,y=230)
c8=CTkCheckBox(f1,text="Build Strength",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c8.place(x=500,y=260)
c8=CTkCheckBox(f1,text="Promote Relaxation",text_color="black",font=("arial",15,"bold"),checkbox_width=15,checkbox_height=15
               ,checkmark_color="white")
c8.place(x=500,y=290)
b2 = CTkButton(f1,text="NEXT",border_width=0,fg_color="#ff0066",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#33ff77"
               ,height=40,width=150,command=go)
b2.place(x=370,y=370)



app.mainloop()

