import webbrowser
from customtkinter import *
from PIL import Image
app = CTk()
app.geometry("1150x800")
app.title("Personal Information")
app.config(bg="#F8F6E3")


def home():
    app.destroy()
    import mental
def go():
    video_url = "How to do Adho Mukha Svanasana (Downward Facing Dog).mp4"
    webbrowser.open_new(video_url)


f1 = CTkFrame(app,width=2 ,height=600,fg_color="black")
f1.place(x=700,y=30)



f2 = CTkFrame(app,width=620,height=650,fg_color="#6AD4DD",corner_radius=50,bg_color="#F8F6E3")
f2.place(x=10,y=20)

l3 = CTkLabel(f2,text_color="black",text="Benefits Of Adho mukha Yoga",font=("times",30,"italic"),fg_color="#97E7E1"
              ,corner_radius=20)
l3.place(x=100,y=10)

l4 = CTkLabel(f2,text_color="black",text="""
1.Benefits of adho mukha svanasana for hypertension:   
One of the best yoga positions to lower high blood pressure is adho mukha svanasana. 
As it boosts blood flow to the brain, this forward-bending position may allow the 
heart rate to slow down. This feature may be good to fight the factors contributing 
to excessive blood pressure. It may also help reduce stress by calming the body and 
the central nervous system.4 However, please do not rely on adho mukha svanasana because 
it may not help to get rid of hypertension on its own. So, kindly see a doctor for 
proper treatment. It is best to try this under the supervision of a trainer.  
2.Benefits of adho mukha svanasana for Chronic Lower Back Pain:  
Chronic low back pain (CLBP) is due to an imbalance of weak muscles and poor posture. 
 et al., 2019 studied that the downwardfacing dog position may help strengthen the arms, 
 legs and lower body in people with CLBP. It may also stretch the chest, back, calves and 
 feet and relieve lower back pain. This might help increase strength and flexibility. 
 As a result, adho mukha svanasana may be beneficial for CLBP.5 However, 
 you should visit a doctor for better outcomes and avoid severe problems.  
3.Benefits of adho mukha svanasana for mental health:  
Phadke et al.,2014 claimed that suryanamaskar yoga such as adho mukha svanasana 
can alleviate stress, anxiety and depression. Additionally, the regulation of 
breath used in suryanamaskar has a calming effect on the nervous system and calms the mind. 
1 But, the result of adho mukha svanasana in improving mental health needs to be explored. 
Please consult the doctor to avoid complications.   
4.Benefits of adho mukha svanasana for chronic pelvic pain:   
Chronic Pelvic Pain (CPP) is a condition in which you may have pain below your chest 
and above your hips that lasts for an extended period. Alison et al., 2017 studied the 
benefits of adho mukha svanasana and other yoga positions in women with CPP.t
 may aid in reducing pelvic floor dysfunction, which may include constipation and 
 promote deep breathing, awareness and relaxation, all of which may assist in lowering 
CPP.7 However, you must see a doctor for better outcomes and to avoid any complications.   
5.Benefits of adho mukha svanasana for tendonitis:  
Tendonitis is when pain and inflammation occur in the tendons, the connections between 
the muscles and the bones. It can occur in the area near the ankles and wrists. 
The book ‘The Yoga Beginner’s Bible’, by Morello, 2015, demonstrated that adho mukha 
svanasana might help manage tendonitis. While doing the adho mukha svanasana, 
the heels are pressed on the ground. It might help stretch the calf muscles.
2 Even so, you must consult a doctor for proper diagnosis and treatment

""",font=("arial",15),)
l4.place(x=0,y=70)

l10 = CTkLabel(app,text=""" Learn Yoga From Our Video
                Tutorial """,text_color="black",font=("times",30,"italic"),fg_color="#97E7E1"
               ,bg_color="#F8F6E3")
l10.place(x=730,y=70)

b2 = CTkButton(app,text="Click Here",border_width=0,fg_color="#7AA2E3",text_color="black"
               ,font=("arial",20,"bold"),corner_radius=20,hover_color="#33ff77",bg_color="#F8F6E3"
               ,height=40,width=150,command=go)
b2.place(x=840,y=200)


b4 = CTkButton(app,text="<-",border_width=3,border_color="black",fg_color="#ff0066",text_color="white",bg_color="#F8F6E3"
               ,font=("arial",15),corner_radius=20,hover_color="#33ff77"
               ,height=30,width=30,command=home)
b4.place(x=1050,y=20)






app.mainloop()