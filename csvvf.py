from tkinter import *
from tkinter import messagebox as msg
import csv
import pandas as pd
from tkinter import filedialog
class CSV_VALUE_FINDER():
    def __init__(self,master):
        self.master = master
        self.master.title("CSV VALUE FINDER")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit",command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu)
        self.about_menu.add_command(label = "About",command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu)
        self.help_menu.add_command(label = "Help",command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        
        self.insertcsv = Button(self.master,text ="INSERT A CSV FILE ",command =self.inscsv)
        self.insertcsv.pack()
        """
        colmlist = list(range(1,21)) TODO THE LIST
        self.colset = StringVar(master)
        self.colset.set(colmlist[0])
        self.popupcolmenu = OptionMenu(self.master,self.colset,*colmlist)
        self.popupcolmenu.pack()
        """
        self.textfind = Text(self.master,height=1)
        self.textfind.pack()
        self.serb = Button(self.master,text ="SEARCH",command = self.searchb)
        self.serb.pack()
        
    def searchb(self):
        pass
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def aboutmenu(self):
        pass
    def helpmenu(self):
        pass
    
    def inscsv(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",filetypes=(("csv files","*.csv"),("all files","*.*")))
        print(self.filename)
        
def main():
    root=Tk()
    CVF = CSV_VALUE_FINDER(root)
    root.mainloop()
    
if __name__=='__main__':
    main()