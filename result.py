import tkinter as tk
from tkinter import ttk

def Result():

    myfile=open(file_name.get(),"rt")
    x=0
    print("Result")
    for each_line in myfile:
         x=each_line.find("Result")
         if(x>=0):
            print(each_line)
    myfile.close()
    myfile2=open(file_name.get(),"rt")
    y=0
    print("open filterd Ports:")
    for port_find in myfile2:
         y=port_find.find("open|filtered")
         if(y>=0):
            print(port_find)
   

root=tk.Tk()
root.geometry("600x200")

label=ttk.Label(root,text="Enter File Name :")
label.pack(side="left")

file_name=tk.StringVar()
inp=ttk.Entry(root,width=15,textvariable=file_name)
inp.pack(side="left")
inp.focus()

greet_button=ttk.Button(root,text="Result",command=Result)
greet_button.pack(side="left",fill="x",expand=True)

quit_button=ttk.Button(root,text="quit",command=root.destroy)
quit_button.pack(side="left",fill="x",expand=True)

root.mainloop() 