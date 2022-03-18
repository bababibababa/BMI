from tkinter import *
import csv
mywin = Tk()

display = StringVar()
displayresult = StringVar()
myinput = IntVar()
myinput2 = IntVar()
inputname = StringVar()
inputage = IntVar()
zone=IntVar()
sex=IntVar()

bmi=0
result=StringVar()

mywin.title('คำนวณค่าดัชนีมวลกาย')
mywin.minsize(400,300)


def resultbmi():
    global bmi
    global result
    if bmi >= 30:
        result.set('Obese')
    elif bmi >=25:
        
        result.set('Over weight')
    elif bmi >= 18.50:
        result.set('Normal weight')
    else:
        result.set('Underweight')
    with open ("info.csv","a")as f:
        f.write(inputname.get()+","+str(inputage.get())+","+str(myinput.get())+","
                +str(myinput2.get())+","+result.get()+","+str(bmi)+"\n")
    
def calbmi():
    global bmi
    input_weight = myinput.get()
    input_height = myinput2.get()
    input_name = inputname.get()
    input_age = inputage.get()
    try:
        bmi = (input_weight / (input_height**2))*10000
    except:
        print("ERROR ! Please enter weight and height must > 0")
    display.set('{:2f}'.format(bmi))
    x()

def x():
    global bmi
    global result
    if zone.get()==1:
        if bmi >= 28:
            result.set('Obese')
        elif bmi >=23:
            result.set('Over weight')
        elif bmi >= 17.50:
            result.set('Normal weight')
        else:
            result.set('Underweight')
        with open ("info.csv","a")as f:
            f.write(inputname.get()+","+str(inputage.get())+","+str(myinput.get())+","
                    +str(myinput2.get())+","+result.get()+","+str(bmi)+"\n")
        
    elif zone.get()==2:
        if bmi >= 30:
            result.set('Obese')
        elif bmi >=25:
            result.set('Over weight')
        elif bmi >= 18.50:
            result.set('Normal weight')
        else:
            result.set('Underweight')
        with open ("info.csv","a")as f:
            f.write(inputname.get()+","+str(inputage.get())+","+str(myinput.get())+","
                    +str(myinput2.get())+","+result.get()+","+str(bmi)+"\n")
    else:
        resultbmi()                  

head = Label(mywin, text = 'Body Mass Index : BMI', font = "Tahoma 20 bold")
head.grid(row=0,columnspan=3,pady=20)

lbname = Label(mywin, text ='Enter your name', width = 22)
lbname.grid(row=2, column=0, sticky=W)

nameip = Entry(mywin, textvariable = inputname, width=22)
nameip.grid(row=2, column=1, sticky=W)

lbage = Label(mywin, text ='Enter your age',width =22)
lbage.grid(row=3, column=0)

m=Radiobutton(text="M",width=5,variable=sex,value=1)
m.grid(row=3,column=1,sticky=E)
f=Radiobutton(text="F",width=5,variable=sex,value=2)
f.grid(row=3,column=2,sticky=W)

a=Radiobutton(text="ASIA",width=5,variable=zone,value=1)
a.grid(row=1,column=0)
eu=Radiobutton(text="EUROPE",width=5,variable=zone,value=2)
eu.grid(row=1,column=1)

ageip = Entry(mywin, textvariable = inputage, width=10)
ageip.grid(row=3, column=1, sticky=W)

lb = Label(mywin, text ='Enter your weight', width = 22)
lb.grid(row=4, column=0, sticky=E)

lbl = Label(mywin, textvariable = display,pady=8,text="Red Text in Tahoma",
            fg="red",font="Tahoma 12 bold")
lbl.grid(row=8, column=1, pady=5)

lblresult = Label(mywin, textvariable = result,pady=8,text="Red Text in Tahoma",
            fg="red",font="Tahoma 12 bold")
lblresult.grid(row=8, column=0, pady=5)

inp1 = Entry(mywin, textvariable = myinput,width=22)
inp1.grid(row=4, column=1, sticky=W)
inp1.focus()

lb2 = Label(mywin, text ='Enter your height', width = 22)
lb2.grid(row=5, column=0, sticky=W)


inp2 = Entry(mywin, textvariable = myinput2,width=22)
inp2.grid(row=5, column=1, sticky=W)
inp2.focus()

btOK = Button(mywin, text='CALCULATE', width=10, bg='#999999', command=calbmi)
btOK.grid(row=10, column=2)

bt = Button(mywin, text='CLOSE', command=mywin.destroy,width=10)
bt.grid(row=10,column=0)

mywin.bind('<Return>',calbmi)

mainloop()
