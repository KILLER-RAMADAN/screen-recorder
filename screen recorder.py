from tkinter import *
import customtkinter
from customtkinter import *
import pyscreenrec 
from tkinter import filedialog
import os
from threading import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import numpy as np
import cv2
import pyautogui
import time
import datetime

home_directory = os.path.expanduser( '~' )
print( home_directory )

def browse():
    global file_name
    global locate_entry
    global Filename
    locate_entry.delete(0,10000)
    Filename.set("")
    locate_entry.configure(state=NORMAL)
    file_name=filedialog.askdirectory(initialdir=os.getcwd())
    locate_entry.insert(0,file_name)
    

rec=pyscreenrec.ScreenRecorder()

def record_sc():
    global locate_entry
    global file_name
    global record
    global time_stamp
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    if locate_entry.get()=="":
        messagebox.showinfo("location","Please Enter File Location!!")
    if frame_box.get()=="":
        messagebox.showinfo("location","Please Enter video frames!!")
    else:
     try:
      screen.state(newstate='iconic')
      time.sleep(1)
      status.configure(text="Status: Recording...")
      stop_button.configure(state=NORMAL)
      play_button.configure(state=NORMAL)
      finish_button.configure(state=NORMAL)
      start_button.configure(state=DISABLED)
      rec.start_recording(video_name=str(f"{file_name}//record{time_stamp}.mp4"),fps=int(frame_box.get()))
     except:
         messagebox.showerror("Erorr","Make Sure About File Location..")
         screen.state(newstate='normal')
         status.configure(text="Status: Erorr File Location... ")
         stop_button.configure(state=DISABLED)
         play_button.configure(state=DISABLED)
         finish_button.configure(state=DISABLED)
         start_button.configure(state=NORMAL)
    



def puase():
    status.configure(text="Status: Puase")
    rec.pause_recording()


def resume():
    status.configure(text="Status: Resume")
    rec.resume_recording()



def finish():
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    status.configure(text="Status: Finish Reconding...")
    stop_button.configure(state=DISABLED)
    play_button.configure(state=DISABLED)
    finish_button.configure(state=DISABLED)
    start_button.configure(state=NORMAL)
    rec.stop_recording()
    rec._save_video(str(f"{file_name}//record{time_stamp}.mp4"))
    
def screenshoot():
    global file_name
    global time_stamp
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    screen.state(newstate='iconic')
    time.sleep(1)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"screenshot\\screenshot{time_stamp}.png", image)
    status.configure(text="Status: Screenshot Done!!")
    screen.state(newstate='normal')



def start_threding():
    Target=Thread(target=record_sc)
    Target.start()


def stop_threding():
    Target=Thread(target=finish)
    Target.start()





screen=customtkinter.CTk()
customtkinter.set_appearance_mode("black")
screen.geometry("470x178+1300+800")
screen.title("screen recorder")
screen.iconbitmap("images/recording.ico")
img=PhotoImage(file="images\\background.png")
Label(screen,image=img).place(x=0,y=0)
screen.resizable(0,0)
screen.attributes("-topmost",True)



start_button_img=PhotoImage(file="images//rec-button.png")
stop_button_img=PhotoImage(file="images//stop.png")
finish_button_img=PhotoImage(file="images//finish-rec.png")
countinue_button_img=PhotoImage(file="images//play.png")
screenshot_button_img=PhotoImage(file="images//screenshot.png")
file_button_img=PhotoImage(file="images//search.png")


start_button=tk.Button(screen,text="",bd=0,image=start_button_img,width=0,height=0,command=start_threding)
start_button.place(x=30,y=150)
start_button.configure(state=NORMAL)

stop_button=tk.Button(screen,text="",bd=0,image=stop_button_img,width=0,height=0,command=puase)
stop_button.place(x=120,y=150)
stop_button.configure(state=DISABLED)

play_button=tk.Button(screen,text="",bd=0,image=countinue_button_img,width=0,height=0,command=resume)
play_button.place(x=220,y=150)
play_button.configure(state=DISABLED)

finish_button=tk.Button(screen,text="",bd=0,image=finish_button_img,width=0,height=0,command=stop_threding)
finish_button.place(x=320,y=150)
finish_button.configure(state=DISABLED)

file_button=tk.Button(screen,text="",bd=0,image=file_button_img,width=0,height=0,command=browse)
file_button.place(x=530,y=150)

screenshot_button=tk.Button(screen,text="",bd=0,image=screenshot_button_img,width=0,height=0,command=screenshoot)
screenshot_button.place(x=400,y=150)


Filename=StringVar()
locate_entry=tk.Entry(screen,bg="white",textvariable=Filename,width=29,font=("arial",10,"bold"))
locate_entry.place(x=320,y=120)
Filename.set("FILE LOCATION")
locate_entry.configure(state=DISABLED)

frame_box=Combobox(screen,width=10,font=("arial",10,"bold"))
frame_box.place(x=200,y=120)
frame_box["value"]=("30","25","15","10","5")


status=tk.Label(screen,text="Status: Ready",font=("calibre 10 italic"),fg="black",bg="white",anchor="w")
status.place(rely=1,anchor="sw",relwidth=1)












screen.mainloop()







# def start_rec():
#     file =Filename.get()
#     rec.start_recording(str(file+".mp4"),5)

# def pause_rec():
#     rec.pause_recording()
# def resume_rec():
#     rec.resume_recording()
# def stop_rec():
#     rec.stop_recording()