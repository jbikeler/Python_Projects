import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #create page description
        self.description = Label(self.master, text="Enter custom text or click Default button")
        self.description.grid(row=0, column=0, padx=(0,0), pady=(10,3))
        #create user input box
        self.custom_entry = Entry(self.master, width=80)
        self.custom_entry.grid(columnspan=2, row=1, column=0, padx=(25,25), pady=(5,20))
        #create default button
        self.btn_default = Button(self.master, text="Use Default", width=30, height=2,command=self.defaultHTML)
        self.btn_default.grid(row=2, column=0, padx=(10,10), pady=(10,10))
        #create custom button
        self.btn_custom = Button(self.master, text="Use Custom", width=30, height=2,command=self.customHTML)
        self.btn_custom.grid(row=2, column=1, padx=(10,10), pady=(10,10))

    #Create a web page with default settings
    def defaultHTML(self) :
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    
    #Create a web page with custom settings
    def customHTML(self) :
        htmlText = self.custom_entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
       
        

if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

