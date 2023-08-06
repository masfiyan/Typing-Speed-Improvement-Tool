#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from tkinter import *
import PIL.ImageTk

class Time(Tk):
    H = int(time.strftime("%H"))
    M = int(time.strftime("%M"))
    S = int(time.strftime("%S"))
    def __init__(self, sentence):
        self.sentence = sentence
        super().__init__()
    def Ima(self):
        im = PIL.Image.open("14.png")
        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(self, image=photo)
        label.image = photo  # keep a reference!
        label.pack()
    def head(self):
        l = Label(self, text="Typing master ", bg="white", font=("Algerian", 68, "bold", "underline", "italic"))
        l.pack()
    def complete(self):
        H2 = int(time.strftime("%H"))
        M2 = int(time.strftime("%M"))
        S2 = int(time.strftime("%S"))
        print("ending time :\n{} Hour : {} Minute: {} Second".format(H2,M2,S2))
        s = 0
        if self.M==M2:
            e = self.S-S2
            s = s+e
            if s<0:
                print()
                print("you took {} seconds to write this".format(-1*s))
            else:
                print()
                print("you took {} seconds to write this".format(s))
        elif M2 > self.M:
            f = 60-self.S
            s = s+f
            b = M2-self.M
            c = b-1
            d = c*60
            s = d+s
            s = s+S2
            if s<0:
                print()
                print("you took {} seconds to write this".format(-1*s))
            else:
                print()
                print("you took {} seconds to write this".format(s))
    def gui(self):
        self.geometry("1400x3000")
        d = Label(self, text="Type this : \n{}".format(self.sentence), bg="white", font=("Arial", 15, "bold"))
        d.pack(side="top", fill="x")
        b = Label(self, text="starting time :\n{} Hour : {} Minute: {} Second".format(self.H, self.M, self.S), bg="white",
                  font=("Algerian", 50))
        b.pack()
        c = Entry(self, width=140, bg="black", fg="white", font=("Arial 50"))
        c.pack()
        d = Button(text = "If complete ?\nClick Me", command = self.complete,width=40,height=3,bg="black",fg="white", font=("Arial 10")).pack()
if __name__ == '__main__':
    a = Time('''uit stand for`s usman institute of technology''''')
    a.head()
    a.gui()
    a.Ima()
    a.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




