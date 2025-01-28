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
    video_url = "Balasana (Child’s Pose) Benefits, How to Do & Contraindications by Yogi Sandeep - Siddhi Yoga.mp4"
    webbrowser.open_new(video_url)


f1 = CTkFrame(app,width=2 ,height=600,fg_color="black")
f1.place(x=700,y=30)



f2 = CTkFrame(app,width=620,height=650,fg_color="#6AD4DD",corner_radius=50,bg_color="#F8F6E3")
f2.place(x=10,y=20)

l3 = CTkLabel(f2,text_color="black",text="Benefits of balasana Yoga",font=("times",30,"italic"),fg_color="#97E7E1"
              ,corner_radius=20)
l3.place(x=100,y=10)

l4 = CTkLabel(f2,text_color="black",text="""What Are the Health Benefits of Balasana? 
Child’s Pose is easy to follow and is an extremely beneficial yoga posture that 
boosts flexibility and enhances muscle strength. Additionally, it tones your body 
and improves your breathing. Here are the top 15 health benefits of Child’s Pose: 
1. Relaxes Your Mind 
A stressed-out mind affects the body resulting in an unhealthy lifestyle. 
To prevent yourself from such instances, do the Child’s Pose yogasana regularly. 
You will feel an instant soothing experience after you rest your forehead slowly 
on the floor while doing this exercise. As you close your eyes, your brain sends 
a signal to the central nervous system. This relaxes your mind, promotes a feeling 
of safety and reduces anxiety levels. 
2. Boosts Digestion 
Regularly practising this yoga posture will improve your digestive system. 
As you rest the stomach on the top of your thighs, it massages the abdominal 
organs and allows movement of the digestive system. During the posture, ensure 
deep inhales and exhales in gentle and repetitive rhythms. As you do it repetitively, 
it will strengthen your intestinal tract and reduce the risk of acidity. 
3. Stretches Lower Back 
If your job involves constant standing or sitting, it might lead to compression 
in your lower back, causing severe back aches. The reason behind this is that we 
tend to put all our body weight on the lower body part and do not involve the lower 
abdominal muscles in activities for days. During this asana, stretching your body widens 
your lower back area, allowing your body to strengthen and lengthen. 
4. Opens up Your Hips 
As you sit for prolonged hours due to work pressure, the muscles around your hips 
tend to tighten, thus causing discomfort. In Child's Pose, as you widen the knees 
and allow your stomach to rest in between the knees, your hips get stretched. 
This posture reduces hip pain, maintaining the health of your hip muscles. 
5. Stimulates Blood Circulation 
One of the many benefits of Balasana includes stimulating blood circulation 
if you regularly practise this yogasana. As there is increased blood circulation, 
it allows optimal functioning of the abdominal organs boosting the overall health of your body. 
6. Strengthens Ligaments 
Healthy ligaments help to stabilise your joints and promote bone health. 
If you lack strong ligaments, it might lead to several health issues. 
Practising Balasana regularly strengthens and stretches the ligaments 
and the tendons of the knees, thus helping you to perform daily activities smoothly. 


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
               ,font=("arial",15),corner_radius=20,hover_color="#97E7E1"
               ,height=30,width=30,command=home)
b4.place(x=1050,y=20)






app.mainloop()