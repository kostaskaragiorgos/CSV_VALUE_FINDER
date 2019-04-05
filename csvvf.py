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
        
    def searchb(self):
        self.textfind.configure(state="disable")
        self.popupcolmenu.configure(state="disable")
        if (self.pandascheck.any()[self.pandascheck.any()[self.colset.get()]==self.textfind.get(1.0,END)]) == True:
            msg.showinfo("FOUND","THE VALUE EXISTS")
            self.textfind.configure(state="normal")
            self.popupcolmenu.configure(state="normal")
        else:
            msg.showinfo("NOT FOUND","THE VALUE DOES NOT EXISTS")
            self.textfind.configure(state="normal")
            self.popupcolmenu.configure(state="normal")
        
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    def aboutmenu(self):
        msg.showinfo("About","About CSV VALUE FINDER  \nVersion 1.0\n")
    
    def helpmenu(self):
        msg.showinfo("Help","Help CSV VALUE FINDER \n1.PRESS THE BUTTON INSERT A CSV FILE\n"+
                     "2.CHPPSE A COLIMN FROM THE DROP DOWN LIST\n3.TYPE WHAT ARE YOU LOOKING FOR \n4.PRESS THE SEARCH BUTTON")
    
    def inscsv(self):
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",filetypes=(("csv files","*.csv"),("all files","*.*")))
        if ".csv" in self.filename:
            msg.showinfo("SUCCESS","THE CSV FILE LOADED SUCCESSFULLY")
            self.pandascheck = pd.read_csv(self.filename)
            colmlist = list(self.pandascheck.columns)
            self.colset = StringVar(self.master)
            self.colset.set(colmlist[0])
            self.popupcolmenu = OptionMenu(self.master,self.colset,*colmlist)
            self.popupcolmenu.pack()
            self.lookleb = Label(self.master,text ="LOOKING FOR")
            self.lookleb.pack()
            self.textfind = Text(self.master,height=1)
            self.textfind.pack()
            self.serb = Button(self.master,text ="SEARCH",command = self.searchb)
            self.serb.pack()
            self.insertcsv.configure(state= "disable")
        else:
            msg.showerror("ERROR","NO FILE LOADED")
def main():
    root=Tk()
    CVF = CSV_VALUE_FINDER(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
