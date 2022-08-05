import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #label for custom HTML text entry
        self.lblCustomHTML = Label(self.master,text="Enter custom text or click the Default HTML Page button")
        self.lblCustomHTML.grid(row=0,column=0,padx=(10,10),pady=(30,10))

        #entry for text to create custom HTML page
        self.txtCustomHTML = Entry(self.master,text="",width=140)
        self.txtCustomHTML.grid(row=1,column=0,columnspan=4,padx=(15,15),pady=(10,15))

        #button to create the default HTML page
        self.btnDefaultHTML = Button(self.master,text="Default HTML Page",width=30,height=2,command=self.defaultHTML)
        self.btnDefaultHTML.grid(row=2,column=2,padx=(10,10),pady=(10,10))

        #button to create HTML page with custom text
        self.btnCustomHTML = Button(self.master,text="Submit Custom Text",width=30,height=2,command=self.customHTML)
        self.btnCustomHTML.grid(row=2,column=3,padx=(0,0),pady=(10,10))


    #create default HTML page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    #create HTML page using user entered text
    def customHTML(self):
        customText = self.txtCustomHTML.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
