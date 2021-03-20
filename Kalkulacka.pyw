from tkinter import *
win = Tk()
win.geometry("260x357")
win.title("Calculáter")
win.resizable(False,False)

#Vstupny display
vstup = StringVar() 

Display = Entry(win,width=66,font = "Consolas 33",textvariable=vstup)

Display.pack()

#Funkcie 1
def output():
    priklad = str(vstup.get())
    try:
        t = eval(priklad)
        print(t)
        Display.delete(0,"end")
        Display.insert(0, t) 
    except:
        print("Error ocured")
        Display.delete(0,"end")
        Display.insert(0, "An error occured")

def stepBack():
    Display.delete(0,"end")

#Tlacitka na execute
b = Button(win,text="ENTER",height=6,width=5,font="Consolas 14",command=output)
b.place(x=200,y=208)
resetB = Button(win,text="↰",height=6,width=5,font="Consolas 14",command=stepBack)
resetB.place(x=200,y=58)

#Tlacitka na cisla
def jeden0():
    Display.insert("end","1")
jeden = Button(win,text="1",font = "Consolas 27",command=jeden0)
jeden.place(x=0,y=58)
#jeden.pack()

#Tlacitka na scitanie
def dva0():
    Display.insert("end","2")
dva = Button(win,text="2",font = "Consolas 27",command=dva0)
dva.place(x=50,y=58)

def tri0():
    Display.insert("end","3")
tri = Button(win,text="3",font = "Consolas 27",command=tri0)
tri.place(x=100,y=58)

def styri0():
    Display.insert("end","4")
styri = Button(win,text="4",font = "Consolas 27",command=styri0)
styri.place(x=0,y=133)

def pat0():
    Display.insert("end","5")
pat = Button(win,text="5",font = "Consolas 27",command=pat0)
pat.place(x=50,y=133)

def sest0():
    Display.insert("end","6")
sest = Button(win,text="6",font = "Consolas 27",command=sest0)
sest.place(x=100,y=133)

def sedem0():
    Display.insert("end","7")
sedem = Button(win,text="7",font = "Consolas 27",command=sedem0)
sedem.place(x=0,y=208)

def osem0():
    Display.insert("end","8")
osem = Button(win,text="8",font = "Consolas 27",command=osem0)
osem.place(x=50,y=208)

def devet0():
    Display.insert("end","9")
devet = Button(win,text="9",font = "Consolas 27",command=devet0)
devet.place(x=100,y=208)

def nula0():
    Display.insert("end","0")
nula = Button(win,text="0",width=7,font = "Consolas 27",command=nula0)
nula.place(x=0,y=283)

#Tlacitka na vypocty
def plus0():
    Display.insert("end","+")
plus = Button(win,text="+",font = "Consolas 27",bg="lightblue",command=plus0)
plus.place(x=150,y=58)

def minus0():
    Display.insert("end","-")
minus = Button(win,text="-",font = "Consolas 27",bg="lightblue",command=minus0)
minus.place(x=150,y=133)

def delene0():
    Display.insert("end","/")
delene = Button(win,text="÷",font = "Consolas 27",bg="lightblue",command=delene0)
delene.place(x=150,y=208)

def krat0():
    Display.insert("end","*")
minus = Button(win,text="x",font = "Consolas 27",bg="lightblue",command=krat0)
minus.place(x=150,y=283)


mainloop()