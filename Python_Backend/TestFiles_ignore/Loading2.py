
from tkinter import Tk, Label
from time import sleep

class Loading:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg = "black")
        self.root.title("Custom Loader")
        self.root.attributes("-fullscreen", True)
        self.totaltime = 300
        # Loading text
        Label(self.root, text = "Loading...", font = "Bahnschrift 15", bg= "black", fg ="#FFBD09").place(x=490, y=320)
        
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
        for i in range(self.totaltime+1):
            for j in range(20):
                #make block yellow:
                Label(self.root, bg="#7FFF00",width=2, height=1).place(x=(j+22)*22, y = 350)
                sleep(0.05)
                self.root.update_idletasks()
                #make block dark:
                Label(self.root, bg="#ECECEC", width=2, height=1).place(x=(j + 22)*22,y=350)
            Rate =round((i+1)*100/self.totaltime,2)
            Label(self.root,text='Progress:'+str(Rate)+'%', font = "Bahnschrift 15", bg= "black", fg ="#FFBD09").place(x=490, y=380)

        else:
            sleep(1)
            #for i in range(20):
                #Label(self.root, bg ="#7FFF00", width = 2, height = 1 ).place(x=(i+22)*22, y = 350)
            
            self.root.destroy()
            exit(0)
            
if __name__ == "__main__":
    Loading()
