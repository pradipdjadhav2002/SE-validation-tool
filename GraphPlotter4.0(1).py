from matplotlib import pyplot
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from math import *

window=Tk()
window.title('Trignometric and Polynomial Function Plot Validator')
window.geometry('300x400')


def PlotEq(X,Y,eq,limity=False):
    global c
    if 'n' in eq or 'c' in eq:
        pyplot.xlabel('X axis (degrees)')
        pyplot.ylabel('Y axis')
        pyplot.title('Graph of '+eq)
    else:
        pyplot.xlabel('X axis')
        pyplot.ylabel('Y axis')
        pyplot.title('Graph of polynomial f(x)='+eq)
    if c!='r':
        pyplot.title('Graph of multiple functions')
    pyplot.plot(X,Y,c,label=eq,linewidth=2)
    #Toggling line color
    if c=='r':
        c='b'
    elif c=='b':
        c='g'
    elif c=='g':
        c='y'
    else:
        c='o'
    #
    if limity:
        pyplot.ylim(-100,100)
    pyplot.legend()
    pyplot.grid(True,color='b')
    pyplot.show()

    #msg.showinfo('Message from Yasir','Kindly close the program! ')

def CordFromEq(eq):
    print('CordFromEq:',eq)
    X=[]
    Y=[]
    x=-10
    while x<=1000:
        X.append(x)
        Y.append(eval(eq))
        x+=0.1
    if 't' in eq:
        PlotEq(X,Y,eq,limity=True)
    else:
        PlotEq(X,Y,eq)

def Menu():
    def get_value():
        print("You want the value of trignometric function for given angle")
        def BTMenu():
            valueframe.distroy()
            Menu()

        def Getsin():
            p = int(input("Enter here also: "))
            t = round(sin(p),2)
            q = str(t)
            L0.config(text = "Output is: " +q)
           # valueframe.destroy()
            print("You got your result:"); print(t)
        def Getcos():
            p = int(input("Enter here also: "))
            t = round(cos(p),2)
            q = str(t)
            L0.config(text = "Output is: " +q)
            #valueframe.destroy()
            print("You got your result:"); print(t)
        def Gettan():
            p = int(input("Enter here also: "))
            t = round(tan(p),2)
            q = str(t)
            L0.config(text = "Output is: " +q)
            #valueframe.destroy()
            print("You got your result:"); print(t)


        def getResult(eqt):
            window.geometry('400x400')
            L0.configure(text='\tSelect input for function: '+eqt)
            Label(valueframe,text=' ').grid(row=3,column=0)
            A0.destroy()
            A1.destroy()
            A2.destroy()
            if(eqt == 'sin'):
                L1 = Label(valueframe, text="Enter Angle in Degree", font=('Calibri 10'))
                L1.grid(row=3,column=2)
                T1 = Entry(valueframe, width = 20)
                T2 = T1.get()
                T1.grid(row=3,column=2)
                print(T2)
                P=Button(valueframe,text='Proceed!',command=Getsin())
                P.grid(row=4,column=2)
                
            elif(eqt == 'cos'):
                L1 = Label(valueframe, text="Enter Angle in Degree", font=('Calibri 10'))
                L1.grid(row=3,column=2)
                T1 = Entry(valueframe, width = 20)
                T2 = T1.get()
                T1.grid(row=3,column=2)
                P=Button(valueframe,text='Proceed!',command=Getcos())
                P.grid(row=4,column=2)   
            elif(eqt == 'tan'):
                L1 = Label(valueframe, text="Enter Angle in Degree", font=('Calibri 10'))
                L1.grid(row=3,column=2)
                T1 = Entry(valueframe, width = 20)
                T2 = T1.get()
                T1.grid(row=3,column=2)
                P=Button(valueframe,text='Proceed!',command=Gettan())
                P.grid(row=4,column=2)         
        



        
        def t_sin(): 
            print("Enter the angle in deg only: ")
            eqt = 'sin'
            getResult(eqt)
        def t_cos(): 
            print("Enter the angle in deg only: ")
            eqt = "cos"
            getResult(eqt) 

        def t_tan(): 
            print("Enter the angle in deg only: ")
            eqt = "tan"
            getResult(eqt)
        
        menuframe.destroy()

        valueframe=Frame(window)
        valueframe.grid()
        print("Now you can proceed with selection of function you want to work with:\n")
        BTM=Button(valueframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        L0=Label(valueframe,text='Choose type of function:')
        A0=Button(valueframe,text='sin',command=t_sin)
        A1=Button(valueframe,text='cos',command=t_cos)
        A2=Button(valueframe,text='tan',command=t_tan)
        #B3=Button(trigframe,text='sin+cos',command=trigsinNcos)

        L0.grid()
        A0.grid()
        A1.grid()
        A2.grid()
        #B3.grid()


    def TrigFun():
        print("You want to plot the graph can choose one of the functions available: \n")
        def BTMenu():
            trigframe.destroy()
            Menu()
        def GetCoeff(eqt):
            def GetEq():
                   eq=C0.get()
                   for i in range(len(eqt)):
                    if eqt[i] in ('x','y'):
                        eq=eq+C1.get()
                    elif eqt[i]=='+':
                        eq=eq+C2.get()
                    elif eqt[i]=='z':
                        eq=eq+C3.get()
                    else:
                        eq=eq+eqt[i]
                   print(eq)
                   CordFromEq(eq)
            window.geometry('400x400')
            L0.configure(text='Select input for function:'+eqt)
            Label(trigframe,text=' ').grid(row=3,column=0)
            B0.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            print("Now select appropriate sign and value for plot to be drawn:\n")
            print("Remember you have to select one value else default will be set\n")
            if eqt=='sin(y)+cos(z)':
                L1=Label(trigframe,text='sin(')
                L2=Label(trigframe,text=')')
                L3=Label(trigframe,text='cos(')
                L4=Label(trigframe,text=')')
                C0=Combobox(trigframe,width=2)
                C1=Combobox(trigframe,width=5)
                C2=Combobox(trigframe,width=2)
                C3=Combobox(trigframe,width=5)
                C0['values']=['+','-']
                C1['values']=['0.5*x','1*x','1.5*x','2*x']
                C2['values']=['+','-']
                C3['values']=['0.5*x','1*x','1.5*x','2*x']
                print("Successfully Got the value\n")
                print("For getting plot click on proceed\n")
                C0.current(0)
                C1.current(1)
                C2.current(0)
                C3.current(1)

                C0.grid(row=3,column=1)
                L1.grid(row=3,column=2)
                C1.grid(row=3,column=3)
                L2.grid(row=3,column=4)
                C2.grid(row=3,column=5)
                L3.grid(row=3,column=6)
                C3.grid(row=3,column=7)
                L4.grid(row=3,column=8)

            else:
                L1=Label(trigframe,text=eqt[:-3])
                L2=Label(trigframe,text='))')
                C0=Combobox(trigframe,width=2)
                C0['values']=['+','-']
                C1=Combobox(trigframe,width=5)
                C1['values']=['0.5*x','1*x','1.5*x','2*x']
                print("Successfully Got the value\n")
                print("For getting plot click on proceed\n")
                C0.current(0)
                C1.current(1)

                C0.grid(row=3,column=1)
                L1.grid(row=3,column=2)
                C1.grid(row=3,column=3)
                L2.grid(row=3,column=4)

            P=Button(trigframe,text='Proceed!',command=GetEq)
            P.grid(row=4,column=2)
            print("Congrates you get your graph...\n")

        def trigsin():
            print("Your Enter data is validated..\n")
            print("It is related to sine function\n")
            eqt='sin(radians(x))'
            GetCoeff(eqt)
        def trigcos():
            print("Your Enter data is validated..\n")
            print("It is related to cosine function\n")
            eqt='cos(radians(x))'
            GetCoeff(eqt)
        def trigtan():
            print("Your Enter data is validated..\n")
            print("It is related to tangent function\n")
            eqt='tan(radians(x))'
            GetCoeff(eqt)
        def trigsinNcos():
            print("Your Enter data is validated..\n")
            print("It is related to sine and cosine function\n")
            eqt='sin(y)+cos(z)'
            GetCoeff(eqt)
        menuframe.destroy()

        trigframe=Frame(window)
        trigframe.grid()

        BTM=Button(trigframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()

        L0=Label(trigframe,text='Choose type of function:')
        B0=Button(trigframe,text='sin',command=trigsin)
        B1=Button(trigframe,text='cos',command=trigcos)
        B2=Button(trigframe,text='tan',command=trigtan)
        B3=Button(trigframe,text='sin+cos',command=trigsinNcos)

        L0.grid()
        B0.grid()
        B1.grid()
        B2.grid()
        B3.grid()

    def help():
        def BTMenu():
            helpframe.destroy()
            Menu()
        menuframe.destroy()

        helpframe=Frame(window)
        helpframe.grid()

        BTM=Button(helpframe,text='<<< Back To Menu',command=BTMenu)
        BTM.grid()
        print("Going back to the main menu...")

        Label(helpframe,text='Help coming soon!').grid()

    def exit():
        try:
            pyplot.close()
        except:
            pass
        print("Everything is goving to be closed...")
        window.destroy()


    menuframe=Frame(window)
    menuframe.grid(row=0,column=3)
    print("Created main page for you......")
    L0=Label(menuframe,text='Trignometric Function Validator\n',font=('Times New Roman',20))
    L1=Label(menuframe,text='MENU',font=('Times New Roman',20))

    B0=(Button(menuframe,text='Give Value',command=get_value,width=30))
    B1=(Button(menuframe,text='Plot T - Functions',command=TrigFun,width=30))
    B2=(Button(menuframe,text='Help',command=help,width=30))
    B3=(Button(menuframe,text='About Project',command=help,width=30))
    B4=(Button(menuframe,text='Exit',command=exit,width=30))
    print("Following is the list available for validation purpose:\n")
    print("\t1.Give value - Takes angle and gives result\n")
    print("\t2. Plot the trignometric function graph\n")
    print("\t3. For any help\n")
    print("\t4. Gives project info\n")
    print("\t5. Exit\n")

    L0.grid(row=0,column=3)
    L1.grid(row=1,column=3)
    B0.grid(row=2,column=3)
    B1.grid(row=3,column=3)
    B2.grid(row=4,column=3)
    B3.grid(row=5,column=3)
    B4.grid(row=6,column=3)


c='r' #global line color for toggling
print("Validation Tool has been started.......\n")
Menu()

window.mainloop()
