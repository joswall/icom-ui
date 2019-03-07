

# buttons  http://effbot.org/tkinterbook/button.htm

# Menu

from tkinter import *



class Application(Frame):
    """application for rig"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.btnCW = Button(self, text = "CW", width=5, height=2, padx=5)
        self.btnCW.grid(row=2, column=10, columnspan=1)
        #self.btnCW(relx=20, rely=)
        self.btnCW["command"] = self.set_mode_cw
        self.btnUSB = Button(self, text= "USB", width=5, height=2)
        self.btnUSB.grid(row=3, column=10, columnspan=1)
        #self.btnUSB.grid()
        self.btnUSB["command"] = self.set_mode_usb
        self.btnLSB = Button(self, text ="LSB", width=5, height=2)
        #self.btnLSB.grid()
        self.btnLSB.grid(row=4, column=10, columnspan=1)
        self.btnLSB["command"] = self.set_mode_lsb

    def set_mode_cw(self):
        self.btnCW.config(relief=SUNKEN)
        self.btnCW["bg"] = ""

    def set_mode_usb(self):
        self.btnUSB["bg"] = ""

    def set_mode_lsb(self):
        self.btnLSB["bg"] = ""


#create the root window
root = Tk()


root.title("Rig Control")
root.geometry("800x600")

app = Application(root)


root.mainloop()



