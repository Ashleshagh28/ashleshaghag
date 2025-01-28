import cv2
import tkinter as tk
from PIL import Image,ImageTk

def video_play():

    cap = cv2.VideoCapture("video (2160p).mp4")


    while True:
        ret, frame = cap.read()


        if not ret:
            break

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.config(image=imgtk)

        window.update()

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

window = tk.Tk()
window.title("Video Player")
window.geometry("1100x600")

label = tk.Label(window)
label.pack()

button = tk.Button(window, text="Play Video", command=video_play)
button.pack()

window.mainloop()