import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
import time



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #set the title of the window
        self.master.title("File Transfer")

        #button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source",width=20,command=self.sourceDir)
        self.sourceDir_btn.grid(row=0,column=0,padx=(20,10),pady=(30,0))

        #entry for source directory selection
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0,column=1,columnspan=2,padx=(20,10),pady=(30,0))

        #button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination",width=20,command=self.destDir)
        self.destDir_btn.grid(row=1,column=0,padx=(20,10),pady=(15,10))

        #entry for destination directory selection
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1,column=1,columnspan=2,padx=(20,10),pady=(15,10))

        #button to transfer files
        self.transfer_btn = Button(text="Transfer Files",width=20,command=self.transferFiles)
        self.transfer_btn.grid(row=2,column=1,padx=(200,0),pady=(0,15))

        #button to exit program
        self.exit_btn = Button(text="Exit",width=20,command=self.exitProgram)
        self.exit_btn.grid(row=2,column=2,padx=(10,40),pady=(0,15))


    #function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0,END)
        self.source_dir.insert(0,selectSourceDir)


    #function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0,selectDestDir)


    #function to transfer files from one directory to another
    def transferFiles(self):
        #get source directory
        source = self.source_dir.get()
        #get destination directory
        destination = self.destination_dir.get()
        #get a list of files in source directory
        source_files = os.listdir(source)

        #current time
        now = time.time()

        #empty list for files to transfer
        transfer_files = []

        #get modified time for each file and if it has been less than 24 hours,
        #add it to the list to be transferred
        for j in source_files:
            mtime = os.path.getmtime(source + '/' + j)
            timeSinceMod = ((now - mtime) / 60 / 60 / 24)
            if (timeSinceMod < 1):
                transfer_files.append(j)
            
            
        #run through each file in list of files to be transferred
        for i in transfer_files:
            #move each file from source to destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')


    #function to exit program
    def exitProgram(self):
        root.destroy()
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
