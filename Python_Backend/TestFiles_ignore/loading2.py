
from tkinter import Tk, Label
from time import sleep
import time

class Loading:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg = "black")
        self.root.title("Custom Loader")
        self.root.attributes("-fullscreen", True)
        self.time_to_run = 175
        self.time_left = self.time_to_run                                                                                                                                                                                        
        # Loading text
        Label(self.root, text = "Khởi tạo chương trình... Vui lòng đợi", font = "Bahnschrift 15", bg= "black", fg ="#FFBD09").place(x=490, y=320)
        
        #Loading block
        for i in range(20):
            Label(self.root, bg ="#ECECEC", width = 2, height = 1 ).place(x=(i+22)*22, y = 350)
        
        #update root  to see animation:
        self.root.update()
        self.play_animation()

        #window in mainloop:
        self.root.mainloop()
    #loader animation
    def play_animation(self):
        while (self.time_left > 0):
            start = time.time()
            for j in range(20):
                #make block yellow:
                Label(self.root, bg="#7FFF00",width=2, height=1).place(x=(j+22)*22, y = 350)
                sleep(0.01)
                self.root.update_idletasks()
                #make block dark:
                Label(self.root, bg="#ECECEC", width=2, height=1).place(x=(j + 22)*22,y=350)
            end = time.time()
            
            #print(f"Time left: {self.time_left}")
            self.time_left = self.time_left - (end-start)
            Rate =round((self.time_to_run - self.time_left)*100/self.time_to_run,2)
            Label(self.root,text='Tiến độ khởi tạo: '+str(Rate)+'%', font = "Bahnschrift 15", bg= "black", fg ="#FFBD09").place(x=490, y=380)
    

        Label(self.root,text='Tiến độ khởi tạo: '+str(100)+'%', font = "Bahnschrift 15", bg= "black", fg ="#FFBD09").place(x=490, y=380)
        sleep(1)
            
        self.root.destroy()
        exit(0)
            
if __name__ == "__main__":
    Loading()