from tkinter import Tk,StringVar,ttk
import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("670x300+0+0")
root.configure(background="white")
root.title("Distance Converter")
root.resizable(width=False, height=False)  # user cant adjust the size
Tops=Frame(root,width=1000,height=50, bg="white", bd=16, relief="raise")
Tops.pack(side=TOP)
LeftMainFrame=Frame(root,width=300,height=300,bd=8, bg="white", relief="raise")
LeftMainFrame.pack(side=LEFT)
RightMainFrame=Frame(root,width=300,height=300,bd=8, bg="white", relief="raise")
RightMainFrame.pack(side=RIGHT)
#--------------------------------------------------------------------------
Distance=IntVar()
value0=StringVar()
convert=IntVar()

#======================Functions Exit=============

def Exit():
    Exit = tkinter.messagebox.askyesno("Exit System","Do you want to quit?")
    if Exit > 0:
        root.destroy()
        return
#======================Function Reset=============
def reset():
    Distance.set("0")
    value0.set("")
    convert.set("0")

def Convert():
    if value0.get()=='Miles to Kilometres':
        convert1=float(convert.get()*1.609344)
        convert2=str('%.1f'%(convert1)),'Kilometres'
        Distance.set(convert2)
    elif value0.get()=='Kilometres to Miles':
        convert1=float(convert.get()/1.609344)
        convert2=str('%.1f'%(convert1)),'Miles'
        Distance.set(convert2)
    elif value0.get()=='Nautical Miles to Miles':
        convert1=float(convert.get()*1.15078)
        convert2=str('%.1f'%(convert1)),'Miles'
        Distance.set(convert2)
    elif value0.get()=='Miles to Nautical Miles':
        convert1=float(convert.get()/1.15078)
        convert2=str('%.1f'%(convert1)),'Nautical Miles'
        Distance.set(convert2)
    elif value0.get()=='Kilometres to centimeter':
        convert1=float(convert.get()*100000)
        convert2=str('%.1f'%(convert1)),'Centimeter'
        Distance.set(convert2)
    elif value0.get()=='Centimeter to Kilometres':
        convert1=float(convert.get()/100000)
        convert2=str('%.1f'%(convert1)),'Kilometres'
        Distance.set(convert2)
    elif (value0.get() == " ") or (Distance.set(0) ):
        tkinter.messagebox.showinfo("Convert?","Make a selection?")


#=====================================The name
lblMiles=Label(Tops,text="Distance Converter",font=('Helvetica',50,'italic'),fg="black",bg="white", pady=2, padx=2, bd=2)
lblMiles.grid(row=0,column=2,sticky=W)
#---------------------------------------------------------------------------------------
box=ttk.Combobox(LeftMainFrame,textvariable=value0,state='readonly',font=('Helvetica',20,'italic'),width=30)
box['values']=(' ','Miles to Kilometres','Kilometres to Miles','Nautical Miles to Miles','Miles to Nautical Miles','Kilometres to centimeter', 'Centimeter to Kilometres' )
box.current(0)
box.grid(row=0,column=0)
#----------------------------------------------------------------------------
EntMiles=Entry(LeftMainFrame,font=('Helvetica',20,'italic'),textvariable=convert, bg="white", bd=2, width=31, justify='center' )
EntMiles.grid(row=1,column=0)

lblConvert=Label(LeftMainFrame,font=('Helvetica',20,'italic'),fg="black",bg="white", textvariable=Distance, bd=2, width=27, pady=2, padx=2, relief= 'sunken')
lblConvert.grid(row=2,column=0)

lblSpace=Label(LeftMainFrame,font=('Helvetica',20,'italic'),bg="white",bd=2,width=27, pady=2, padx=2, relief= 'sunken')
lblSpace.grid(row=3,column=0)
#=============================================Buttons=======================================================
btnConvert=Button(RightMainFrame,text="Convert",font=('Helvetica',18,'italic'), width=10, height=0,  bg="white", pady=2, padx=2, bd=2, command=Convert)
btnConvert.grid(row=1,column=0)

btnReset=Button(RightMainFrame,text="Reset",font=('Helvetica',18,'italic'), width=10, height=0, pady=2, bg="white", padx=2, bd=2, command=reset)
btnReset.grid(row=2,column=0)

btnExit=Button(RightMainFrame,text="Exit",font=('Helvetica',18,'italic'), width=10, height=0, pady=2, bg="white",  padx=2, bd=2, command=Exit)
btnExit.grid(row=3,column=0)


root.mainloop()
