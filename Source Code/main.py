from tkinter import *
from tkinter import ttk
from singleStageOxidation import SingleStageOxidation
from multiStageOxidation import multiStageOxidation
from massoudSingleStage import SingleStageOxidationMassoud
from massoudMultiStage import multiStageOxidationMassoud
from oxideColor import colour
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt



#Method for Main Menu Screen with the following Options
# 1. Single Stage Oxidation
# 2. Multi Stage Oxidation
# 3. Find Oxide Color
# 4. Coefficients
# 5. Important Graphs
# 6. Quit


def introScreen():
    global startWin
    startWin = Tk()
    startWin.geometry("450x350+430+150")
    startWin.title('OXYSIM')

    # this wil create a label widget
    l1 = Label(startWin, text="OXYSIM")
    l1.config(width=200)
    l1.config(font=("Courier", 60, "bold"))
    l1.config(foreground="maroon")
    l1.pack()

    l2 = Label(startWin, text="An Oxidation Simulator")
    l2.config(width=200)
    l2.config(font=("Courier", 14))
    l2.config(foreground="blue")
    l2.pack(pady=10)

    button1 = Button(startWin, text='Start', width=30, background="light green", command=lambda:createMainScreen())
    button1.config(font=("Courier", 10, "bold"))
    button1.pack()
    button2 = Button(startWin, text='Quit', width=30, background="red", command=lambda:startWin.destroy())
    button2.config(font=("Courier", 10, "bold"))
    button2.pack(pady=15)

    l3 = Label(startWin, text="IIITD ICF Project")
    l3.config(width=200)
    l3.config(font=("Courier", 15, "bold"))
    l3.config(foreground="black")
    l3.pack(pady=10)

    l4 = Label(startWin, text="Creators:Subodh,Chandraveer,Puneet,Mukul")
    l4.config(width=200)
    l4.config(font=("Courier", 8,))
    l4.config(foreground="black")
    l4.pack()

    startWin.mainloop()

def createMainScreen():
    startWin.destroy()
    main_screen = Tk()
    main_screen.geometry("350x350+420+120")
    main_screen.title("OXYSIM")

    l1 = Label(main_screen, text="OXYSIM")
    l1.config(width=200)
    l1.config(font=("Courier", 60, "bold"))
    l1.config(foreground="maroon")
    l1.pack()

    button1 = Button(main_screen, text='Single Stage Oxidation', width=30, command=lambda:ssOxidationScreen())
    button1.config(font=("Courier", 10))
    button1.pack(pady=5)

    button2 = Button(main_screen, text='Multi Stage Oxidation', width=30, command=lambda:msOxidationScreen())
    button2.config(font=("Courier", 10))
    button2.pack(pady=5)

    button3 = Button(main_screen, text='Find Oxide Color', width=30, command=lambda:oxideColorScreen())
    button3.config(font=("Courier", 10))
    button3.pack(pady=5)

    button4 = Button(main_screen, text='Coefficients', width=30, command=lambda:coefficientScreen())
    button4.config(font=("Courier", 10))
    button4.pack(pady=5)

    button5 = Button(main_screen, text='Important Graphs', width=30, command=lambda:graphScreen())
    button5.config(font=("Courier", 10))
    button5.pack(pady=5)
    button6 = Button(main_screen, text='Quit', width=30, command=lambda:main_screen.destroy())
    button6.config(font=("Courier", 10))
    button6.pack(pady=5)
    main_screen.mainloop()


#Methods for Single Stage Oxidation
def ssOxidationScreen():
    global mode,orientation,ox_type,temp,time,flag,ithick
    global ssOxidation_screen
    ssOxidation_screen = Tk()
    ssOxidation_screen.geometry("500x320+420+100")
    ssOxidation_screen.title("Single Stage Oxidation")

    Label(ssOxidation_screen, text="Oxidation Model:").grid(row=0, column=0, sticky=E)
    n = StringVar()
    mode = ttk.Combobox(ssOxidation_screen, width=27, textvariable=n)
    mode['values'] = ('Deal Grove Model', 'Deal Grove + Massoud Model')
    mode.grid(column=1, row=0, pady=5)
    mode.current(0)

    Label(ssOxidation_screen, text="Crystal Orientation:").grid(row=1, column=0, sticky=E)
    n=StringVar()
    orientation = ttk.Combobox(ssOxidation_screen, width=27, textvariable=n)
    orientation['values'] = ('100','111')
    orientation.grid(column=1, row=1,pady=5)
    orientation.current(1)

    Label(ssOxidation_screen, text="Oxidation Type:").grid(row=2, column=0, sticky=E)
    n = StringVar()
    ox_type = ttk.Combobox(ssOxidation_screen, width=27, textvariable=n)
    ox_type['values'] = ('Dry','Wet')
    ox_type.grid(column=1, row=2,pady=5)
    ox_type.current(1)

    Label(ssOxidation_screen, text="Temperature(degree Celcius):").grid(row=3, column=0, sticky=E)
    temp = Entry(ssOxidation_screen,width=30)
    temp.insert(END,"1100")
    temp.grid(row=3, column=1,pady=5)

    Label(ssOxidation_screen, text="Duration of Oxidation(in hours):").grid(row=4, column=0, sticky=E)
    time = Entry(ssOxidation_screen, width=30)
    time.insert(END,"1")
    time.grid(row=4, column=1,pady=5)

    Label(ssOxidation_screen, text="Do you have initial oxide thickness(Y/N):").grid(row=5, column=0, sticky=E)
    n=StringVar()
    flag = ttk.Combobox(ssOxidation_screen, width=27, textvariable=n)
    flag['values'] = ('Y','N')
    flag.grid(row=5, column=1, pady=5)
    flag.current(1)

    Label(ssOxidation_screen, text="Enter the initial oxide thickness(in um):").grid(row=6, column=0, sticky=E)
    ithick = Entry(ssOxidation_screen, width=30)
    ithick.insert(END,"0")
    ithick.grid(row=6, column=1, pady=10)

    button1 = Button(ssOxidation_screen, text='Submit', width=25, background="light green", command=lambda:getSSFields())
    button1.grid(row=16,column=1)
    ssOxidation_screen.mainloop()

def getSSFields():
    global oxidation_mode,crystal_orientation,oxidation_type,oxidation_temp,oxidation_time,thickness_flag,initial_thickness,result
    oxidation_mode=mode.get()
    crystal_orientation=int(orientation.get())
    oxidation_type=ox_type.get()
    oxidation_temp=float(temp.get())+273
    oxidation_time=float(time.get())
    thickness_flag=flag.get()
    initial_thickness=float(ithick.get())

    if(oxidation_mode == "Deal Grove Model"):
        OxideThickness = SingleStageOxidation(
            crystal_orientation, oxidation_type, oxidation_temp, oxidation_time, initial_thickness,
            thickness_flag)
        result = OxideThickness.calculateOxideThickness()
        Label(ssOxidation_screen, text="The calculated oxide thickness (in um):").grid(row=20, column=0, sticky=E)
        res = Entry(ssOxidation_screen, width=30)
        res.insert(END, round(result,3))
        res.grid(row=20, column=1, pady=10)

        Label(ssOxidation_screen, text="Do you want to plot the graph?:").grid(row=22, column=0, sticky=E)
        button1 = Button(ssOxidation_screen, text='Yes', width=10, background="green", command=lambda:plotSSGraph())
        button1.grid(row=22, column=1)
        button2 = Button(ssOxidation_screen, text='No', width=10, background="red", command=lambda:ssOxidation_screen.destroy())
        button2.grid(row=22, column=2)

    elif (oxidation_mode == "Deal Grove + Massoud Model"):
        OxideThickness = SingleStageOxidationMassoud(
            crystal_orientation, oxidation_type, oxidation_temp, oxidation_time, initial_thickness,
            thickness_flag)
        result = OxideThickness.calculateOxideThickness()
        Label(ssOxidation_screen, text="The calculated oxide thickness (in um):").grid(row=20, column=0, sticky=E)
        res = Entry(ssOxidation_screen, width=30)
        res.insert(END, round(result,3))
        res.grid(row=20, column=1, pady=10)

        Label(ssOxidation_screen, text="Do you want to plot the graph?:").grid(row=22, column=0, sticky=E)
        button1 = Button(ssOxidation_screen, text='Yes', width=10, background="green", command=lambda:plotSSGraph())
        button1.grid(row=22, column=1)
        button2 = Button(ssOxidation_screen, text='No', width=10, background="red", command=lambda:ssOxidation_screen.destroy())
        button2.grid(row=22, column=2)
        ssOxidation_screen.mainloop()


def plotSSGraph():
    if(oxidation_mode == "Deal Grove Model"):
        xValues = []
        yValues = []
        step_size = oxidation_time / 50
        for i in np.arange(0, oxidation_time, step_size):
            obj = SingleStageOxidation(
                crystal_orientation, oxidation_type, oxidation_temp, i, initial_thickness,
                thickness_flag)
            y = obj.calculateOxideThickness()
            xValues.append(i)
            yValues.append(y)
        xValues.append(oxidation_time)
        yValues.append(result)
        #print(xValues)
        #print(yValues)
        fig = plt.figure()
        ax = plt.subplot(111)
        plt.xlabel("Time(in hours)")
        plt.ylabel("Oxide Thickness(in um)")
        ax.plot(xValues, yValues, marker='.')
        plt.title('Oxide Thickness vs Time')
        #plt.show()
        fig.savefig('plot.png')
        top = Toplevel()
        top.geometry("640x480")
        top.title("Deal Grove Model")
        img = ImageTk.PhotoImage(Image.open("plot.png"))
        l2 = Label(top, image=img)
        l2.pack()
        top.mainloop()

    elif(oxidation_mode == "Deal Grove + Massoud Model"):
        xValues = []
        yValues = []
        step_size = oxidation_time / 50
        for i in np.arange(0, oxidation_time, step_size):
            obj = SingleStageOxidationMassoud(
                crystal_orientation, oxidation_type, oxidation_temp, i, initial_thickness,
                thickness_flag)
            y = obj.calculateOxideThickness()
            xValues.append(i)
            yValues.append(y)
        xValues.append(oxidation_time)
        yValues.append(result)
        #print(xValues)
        #print(yValues)
        fig = plt.figure()
        ax = plt.subplot(111)
        plt.xlabel("Time(in hours)")
        plt.ylabel("Oxide Thickness(in um)")
        ax.plot(xValues, yValues, marker='.')
        plt.title('Oxide Thickness vs Time')
        #plt.show()
        fig.savefig('plot.png')
        top = Toplevel()
        top.geometry("640x480")
        top.title("Deal Grove + Massoud Model")
        img = ImageTk.PhotoImage(Image.open("plot.png"))
        l2 = Label(top, image=img)
        l2.pack()
        top.mainloop()


#Methods for Multi Stage Oxidation
def msOxidationScreen():
    global msOxidation_screen,button_1
    global modeMS,orientationMS,stages,flagMS,ithickMS
    msOxidation_screen = Tk()
    msOxidation_screen.geometry("850x450+200+100")
    msOxidation_screen.title("Multi Stage Oxidation")

    Label(msOxidation_screen, text="Oxidation Model:").grid(row=0, column=0, sticky=E)
    n = StringVar()
    modeMS = ttk.Combobox(msOxidation_screen, width=20, textvariable=n)
    modeMS['values'] = ('Deal Grove Model', 'Deal Grove + Massoud Model')
    modeMS.grid(column=1, row=0, pady=5)
    modeMS.current(0)

    Label(msOxidation_screen, text="Crystal Orientation:").grid(row=1, column=0, sticky=E)
    n = StringVar()
    orientationMS = ttk.Combobox(msOxidation_screen, width=20, textvariable=n)
    orientationMS['values'] = ('100','111')
    orientationMS.grid(column=1, row=1, pady=5)
    orientationMS.current(1)

    Label(msOxidation_screen, text="Do you have initial oxide thickness(Y/N):").grid(row=2, column=0, sticky=E)
    n = StringVar()
    flagMS = ttk.Combobox(msOxidation_screen, width=20, textvariable=n)
    flagMS['values'] = ('Y','N')
    flagMS.grid(row=2, column=1, pady=5)
    flagMS.current(1)

    Label(msOxidation_screen, text="Enter the initial oxide thickness(in um):").grid(row=3, column=0, sticky=E)
    ithickMS = Entry(msOxidation_screen, width=20)
    ithickMS.insert(END, "0")
    ithickMS.grid(row=3, column=1, pady=10)

    Label(msOxidation_screen, text="Number of stages:").grid(row=4, column=0, sticky=E)
    n = StringVar()
    stages = ttk.Combobox(msOxidation_screen, width=20, textvariable=n)
    stages['values'] = ('2','3','4','5')
    stages.grid(column=1, row=4, pady=5,padx=5)
    stages.current(1)

    button_1 = Button(msOxidation_screen, text='Ok', width=10, command=msOxidationScreen2)
    button_1.grid(row=4,column=3)
    msOxidation_screen.mainloop()

def msOxidationScreen2():
    button_1.destroy()
    global button_2,button_3,button_4,button_5
    global ox_type1,ox_type2,ox_type3,ox_type4,ox_type5
    global temp1,temp2,temp3,temp4,temp5
    global time1,time2,time3,time4,time5
    num=stages.get()

    if(num=='2'):
        #button1.grid(row=3, column=2)
        Label(msOxidation_screen, text="Stage 1 : Oxidation Type:").grid(row=5, column=0, sticky=E)
        n = StringVar()
        ox_type1 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type1['values'] = ('Dry', 'Wet')
        ox_type1.grid(column=1, row=5, pady=5,padx=5)
        ox_type1.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=5, column=2, sticky=E)
        temp1 = Entry(msOxidation_screen, width=10)
        temp1.insert(END, "1100")
        temp1.grid(row=5, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=5, column=4, sticky=E)
        time1 = Entry(msOxidation_screen, width=10)
        time1.insert(END, "1")
        time1.grid(row=5, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 2 : Oxidation Type:").grid(row=6, column=0, sticky=E)
        n = StringVar()
        ox_type2 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type2['values'] = ('Dry', 'Wet')
        ox_type2.grid(column=1, row=6, pady=5,padx=5)
        ox_type2.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=6, column=2, sticky=E)
        temp2 = Entry(msOxidation_screen, width=10)
        temp2.insert(END, "1100")
        temp2.grid(row=6, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=6, column=4, sticky=E)
        time2 = Entry(msOxidation_screen, width=10)
        time2.insert(END, "1")
        time2.grid(row=6, column=5, pady=5,padx=5)

        button_2 = Button(msOxidation_screen, text='Submit', width=8, background="light green", command=getMSFields)
        button_2.grid(row=9, column=5)

    elif(num=='3'):
        #button1.grid(row=3, column=2)
        Label(msOxidation_screen, text="Stage 1 : Oxidation Type:").grid(row=5, column=0, sticky=E)
        n = StringVar()
        ox_type1 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type1['values'] = ('Dry', 'Wet')
        ox_type1.grid(column=1, row=5, pady=5,padx=5)
        ox_type1.current(1)

        Label(msOxidation_screen, text="Temperature(degree celcius):").grid(row=5, column=2, sticky=E)
        temp1 = Entry(msOxidation_screen, width=10)
        temp1.insert(END, "1100")
        temp1.grid(row=5, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=5, column=4, sticky=E)
        time1 = Entry(msOxidation_screen, width=10)
        time1.insert(END, "1")
        time1.grid(row=5, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 2 : Oxidation Type:").grid(row=6, column=0, sticky=E)
        n = StringVar()
        ox_type2 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type2['values'] = ('Dry', 'Wet')
        ox_type2.grid(column=1, row=6, pady=5,padx=5)
        ox_type2.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=6, column=2, sticky=E)
        temp2 = Entry(msOxidation_screen, width=10)
        temp2.insert(END, "1100")
        temp2.grid(row=6, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=6, column=4, sticky=E)
        time2 = Entry(msOxidation_screen, width=10)
        time2.insert(END, "1")
        time2.grid(row=6, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 3 : Oxidation Type:").grid(row=7, column=0, sticky=E)
        n = StringVar()
        ox_type3 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type3['values'] = ('Dry', 'Wet')
        ox_type3.grid(column=1, row=7, pady=5,padx=5)
        ox_type3.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=7, column=2, sticky=E)
        temp3 = Entry(msOxidation_screen, width=10)
        temp3.insert(END, "1100")
        temp3.grid(row=7, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=7, column=4, sticky=E)
        time3 = Entry(msOxidation_screen, width=10)
        time3.insert(END, "1")
        time3.grid(row=7, column=5, pady=5,padx=5)

        button_3 = Button(msOxidation_screen, text='Submit', width=8, background="light green", command=getMSFields)
        button_3.grid(row=10, column=5)

    elif(num=='4'):
        #button1.grid(row=3, column=2)
        Label(msOxidation_screen, text="Stage 1 : Oxidation Type:").grid(row=5, column=0, sticky=E)
        n = StringVar()
        ox_type1 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type1['values'] = ('Dry', 'Wet')
        ox_type1.grid(column=1, row=5, pady=5,padx=5)
        ox_type1.current(1)

        Label(msOxidation_screen, text="Temperature(degree celcius):").grid(row=5, column=2, sticky=E)
        temp1 = Entry(msOxidation_screen, width=10)
        temp1.insert(END, "1100")
        temp1.grid(row=5, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=5, column=4, sticky=E)
        time1 = Entry(msOxidation_screen, width=10)
        time1.insert(END, "1")
        time1.grid(row=5, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 2 : Oxidation Type:").grid(row=6, column=0, sticky=E)
        n = StringVar()
        ox_type2 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type2['values'] = ('Dry', 'Wet')
        ox_type2.grid(column=1, row=6, pady=5,padx=5)
        ox_type2.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=6, column=2, sticky=E)
        temp2 = Entry(msOxidation_screen, width=10)
        temp2.insert(END, "1100")
        temp2.grid(row=6, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=6, column=4, sticky=E)
        time2 = Entry(msOxidation_screen, width=10)
        time2.insert(END, "1")
        time2.grid(row=6, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 3 : Oxidation Type:").grid(row=7, column=0, sticky=E)
        n = StringVar()
        ox_type3 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type3['values'] = ('Dry', 'Wet')
        ox_type3.grid(column=1, row=7, pady=5,padx=5)
        ox_type3.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=7, column=2, sticky=E)
        temp3 = Entry(msOxidation_screen, width=10)
        temp3.insert(END, "1100")
        temp3.grid(row=7, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=7, column=4, sticky=E)
        time3 = Entry(msOxidation_screen, width=10)
        time3.insert(END, "1")
        time3.grid(row=7, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 4 : Oxidation Type:").grid(row=8, column=0, sticky=E)
        n = StringVar()
        ox_type4 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type4['values'] = ('Dry', 'Wet')
        ox_type4.grid(column=1, row=8, pady=5,padx=5)
        ox_type4.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=8, column=2, sticky=E)
        temp4 = Entry(msOxidation_screen, width=10)
        temp4.insert(END, "1100")
        temp4.grid(row=8, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=8, column=4, sticky=E)
        time4 = Entry(msOxidation_screen, width=10)
        time4.insert(END, "1")
        time4.grid(row=8, column=5, pady=5,padx=5)

        button_4 = Button(msOxidation_screen, text='Submit', width=8, background="light green", command=getMSFields)
        button_4.grid(row=11, column=5)

    elif(num=='5'):
        #button1.grid(row=3, column=2)
        Label(msOxidation_screen, text="Stage 1 : Oxidation Type:").grid(row=5, column=0, sticky=E)
        n = StringVar()
        ox_type1 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type1['values'] = ('Dry', 'Wet')
        ox_type1.grid(column=1, row=5, pady=5,padx=5)
        ox_type1.current(1)

        Label(msOxidation_screen, text="Temperature(degree celcius):").grid(row=5, column=2, sticky=E)
        temp1 = Entry(msOxidation_screen, width=10)
        temp1.insert(END, "1100")
        temp1.grid(row=5, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=5, column=4, sticky=E)
        time1 = Entry(msOxidation_screen, width=10)
        time1.insert(END, "1")
        time1.grid(row=5, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 2 : Oxidation Type:").grid(row=6, column=0, sticky=E)
        n = StringVar()
        ox_type2 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type2['values'] = ('Dry', 'Wet')
        ox_type2.grid(column=1, row=6, pady=5,padx=5)
        ox_type2.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=6, column=2, sticky=E)
        temp2 = Entry(msOxidation_screen, width=10)
        temp2.insert(END, "1100")
        temp2.grid(row=6, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=6, column=4, sticky=E)
        time2 = Entry(msOxidation_screen, width=10)
        time2.insert(END, "1")
        time2.grid(row=6, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 3 : Oxidation Type:").grid(row=7, column=0, sticky=E)
        n = StringVar()
        ox_type3 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type3['values'] = ('Dry', 'Wet')
        ox_type3.grid(column=1, row=7, pady=5,padx=5)
        ox_type3.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=7, column=2, sticky=E)
        temp3 = Entry(msOxidation_screen, width=10)
        temp3.insert(END, "1100")
        temp3.grid(row=7, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=7, column=4, sticky=E)
        time3 = Entry(msOxidation_screen, width=10)
        time3.insert(END, "1")
        time3.grid(row=7, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 4 : Oxidation Type:").grid(row=8, column=0, sticky=E)
        n = StringVar()
        ox_type4 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type4['values'] = ('Dry', 'Wet')
        ox_type4.grid(column=1, row=8, pady=5,padx=5)
        ox_type4.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=8, column=2, sticky=E)
        temp4 = Entry(msOxidation_screen, width=10)
        temp4.insert(END, "1100")
        temp4.grid(row=8, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=8, column=4, sticky=E)
        time4 = Entry(msOxidation_screen, width=10)
        time4.insert(END, "1")
        time4.grid(row=8, column=5, pady=5,padx=5)

        Label(msOxidation_screen, text="Stage 5 : Oxidation Type:").grid(row=9, column=0, sticky=E)
        n = StringVar()
        ox_type5 = ttk.Combobox(msOxidation_screen, width=10, textvariable=n)
        ox_type5['values'] = ('Dry', 'Wet')
        ox_type5.grid(column=1, row=9, pady=5,padx=5)
        ox_type5.current(1)

        Label(msOxidation_screen, text="Temperature(degree Celcius):").grid(row=9, column=2, sticky=E)
        temp5 = Entry(msOxidation_screen, width=10)
        temp5.insert(END, "1100")
        temp5.grid(row=9, column=3, pady=5,padx=5)

        Label(msOxidation_screen, text="Duration of Oxidation(in hr):").grid(row=9, column=4, sticky=E)
        time5 = Entry(msOxidation_screen, width=10)
        time5.insert(END, "1")
        time5.grid(row=9, column=5, pady=5,padx=5)

        button_5 = Button(msOxidation_screen, text='Submit', width=8, background="light green", command=getMSFields)
        button_5.grid(row=12, column=5)

def getMSFields():
    global oxidation_modeMS,crystal_orientationMS,thickness_flagMS,initial_thicknessMS
    global num,multiStageOxidationObj2,multiStageOxidationObj3,multiStageOxidationObj4,multiStageOxidationObj5
    oxidation_modeMS=modeMS.get()
    num=int(stages.get())
    crystal_orientationMS = int(orientationMS.get())
    thickness_flagMS = flagMS.get()
    initial_thicknessMS = float(ithickMS.get())

    if(num== 2):
        oxideThicknessList = []
        oxidation_type1 = ox_type1.get()
        oxidation_temp1 = float(temp1.get()) + 273
        oxidation_time1 = float(time1.get())

        oxidation_type2 = ox_type2.get()
        oxidation_temp2 = float(temp2.get()) + 273
        oxidation_time2 = float(time2.get())

        oxidationTypeMS = [oxidation_type1, oxidation_type2]
        temperatureMS = [oxidation_temp1, oxidation_temp2]
        oxidationTimeMS = [oxidation_time1, oxidation_time2]

        if(oxidation_modeMS == "Deal Grove Model"):
            multiStageOxidationObj2 = multiStageOxidation(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj2.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        elif(oxidation_modeMS == "Deal Grove + Massoud Model"):
            multiStageOxidationObj2 = multiStageOxidationMassoud(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj2.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 1:").grid(row=11, column=0, sticky=E)
        res1 = Entry(msOxidation_screen, width=10)
        res1.insert(END, oxideThicknessList[1])
        res1.grid(row=11, column=1, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 2:").grid(row=12, column=0, sticky=E)
        res2 = Entry(msOxidation_screen, width=10)
        res2.insert(END, oxideThicknessList[2])
        res2.grid(row=12, column=1, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 3:").grid(row=11, column=2, sticky=E)
        res3 = Entry(msOxidation_screen, width=10)
        res3.grid(row=11, column=3, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 4:").grid(row=12, column=2, sticky=E)
        res4 = Entry(msOxidation_screen, width=10)
        res4.grid(row=12, column=3, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 5:").grid(row=11, column=4, sticky=E)
        res5 = Entry(msOxidation_screen, width=10)
        res5.grid(row=11, column=5, pady=5)

        Label(msOxidation_screen, text="Do you want to plot the graph?:").grid(row=21, column=0, sticky=E)
        btn1 = Button(msOxidation_screen, text='Yes', width=10, background="green", command=plotMSGraph)
        btn1.grid(row=21, column=1)
        btn2 = Button(msOxidation_screen, text='No', width=10, background="red", command=msOxidation_screen.destroy)
        btn2.grid(row=21, column=2)

    elif(num==3):
        oxideThicknessList = []
        oxidation_type1 = ox_type1.get()
        oxidation_temp1 = float(temp1.get()) + 273
        oxidation_time1 = float(time1.get())

        oxidation_type2 = ox_type2.get()
        oxidation_temp2 = float(temp2.get()) + 273
        oxidation_time2 = float(time2.get())

        oxidation_type3 = ox_type3.get()
        oxidation_temp3 = float(temp3.get()) + 273
        oxidation_time3 = float(time3.get())

        oxidationTypeMS = [oxidation_type1, oxidation_type2,oxidation_type3]
        temperatureMS = [oxidation_temp1, oxidation_temp2,oxidation_temp3]
        oxidationTimeMS = [oxidation_time1, oxidation_time2,oxidation_time3]

        if (oxidation_modeMS == "Deal Grove Model"):
            multiStageOxidationObj3 = multiStageOxidation(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj3.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        elif (oxidation_modeMS == "Deal Grove + Massoud Model"):
            multiStageOxidationObj3 = multiStageOxidationMassoud(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj3.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 1:").grid(row=12, column=0, sticky=E)
        res1 = Entry(msOxidation_screen, width=10)
        res1.insert(END, oxideThicknessList[1])
        res1.grid(row=12, column=1, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 2:").grid(row=13, column=0, sticky=E)
        res2 = Entry(msOxidation_screen, width=10)
        res2.insert(END, oxideThicknessList[2])
        res2.grid(row=13, column=1, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 3:").grid(row=12, column=2, sticky=E)
        res3 = Entry(msOxidation_screen, width=10)
        res3.insert(END, oxideThicknessList[3])
        res3.grid(row=12, column=3, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 4:").grid(row=13, column=2, sticky=E)
        res4 = Entry(msOxidation_screen, width=10)
        res4.grid(row=13, column=3, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 5:").grid(row=12, column=4, sticky=E)
        res5 = Entry(msOxidation_screen, width=10)
        res5.grid(row=12, column=5, pady=5)

        Label(msOxidation_screen, text="Do you want to plot the graph?:").grid(row=22, column=0, sticky=E)
        btn1 = Button(msOxidation_screen, text='Yes', width=10, background="green", command=plotMSGraph)
        btn1.grid(row=22, column=1)
        btn2 = Button(msOxidation_screen, text='No', width=10, background="red", command=msOxidation_screen.destroy)
        btn2.grid(row=22, column=2)

    elif(num==4):
        oxideThicknessList = []
        oxidation_type1 = ox_type1.get()
        oxidation_temp1 = float(temp1.get()) + 273
        oxidation_time1 = float(time1.get())

        oxidation_type2 = ox_type2.get()
        oxidation_temp2 = float(temp2.get()) + 273
        oxidation_time2 = float(time2.get())

        oxidation_type3 = ox_type3.get()
        oxidation_temp3 = float(temp3.get()) + 273
        oxidation_time3 = float(time3.get())

        oxidation_type4 = ox_type4.get()
        oxidation_temp4 = float(temp4.get()) + 273
        oxidation_time4 = float(time4.get())

        oxidationTypeMS = [oxidation_type1, oxidation_type2, oxidation_type3,oxidation_type4]
        temperatureMS = [oxidation_temp1, oxidation_temp2, oxidation_temp3,oxidation_temp4]
        oxidationTimeMS = [oxidation_time1, oxidation_time2, oxidation_time3,oxidation_time4]

        if (oxidation_modeMS == "Deal Grove Model"):
            multiStageOxidationObj4 = multiStageOxidation(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj4.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        elif (oxidation_modeMS == "Deal Grove + Massoud Model"):
            multiStageOxidationObj4 = multiStageOxidationMassoud(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj4.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 1:").grid(row=13, column=0, sticky=E)
        res1 = Entry(msOxidation_screen, width=10)
        res1.insert(END, oxideThicknessList[1])
        res1.grid(row=13, column=1, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 2:").grid(row=14, column=0, sticky=E)
        res2 = Entry(msOxidation_screen, width=10)
        res2.insert(END, oxideThicknessList[2])
        res2.grid(row=14, column=1, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 3:").grid(row=13, column=2, sticky=E)
        res3 = Entry(msOxidation_screen, width=10)
        res3.insert(END, oxideThicknessList[3])
        res3.grid(row=13, column=3, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 4:").grid(row=14, column=2, sticky=E)
        res4 = Entry(msOxidation_screen, width=10)
        res4.insert(END, oxideThicknessList[4])
        res4.grid(row=14, column=3, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 5:").grid(row=13, column=4, sticky=E)
        res5 = Entry(msOxidation_screen, width=10)
        res5.grid(row=13, column=5, pady=5)

        Label(msOxidation_screen, text="Do you want to plot the graph?:").grid(row=23, column=0, sticky=E)
        btn1 = Button(msOxidation_screen, text='Yes', width=10, background="green", command=plotMSGraph)
        btn1.grid(row=23, column=1)
        btn2 = Button(msOxidation_screen, text='No', width=10, background="red", command=msOxidation_screen.destroy)
        btn2.grid(row=23, column=2)

    elif(num==5):
        oxideThicknessList = []
        oxidation_type1 = ox_type1.get()
        oxidation_temp1 = float(temp1.get()) + 273
        oxidation_time1 = float(time1.get())

        oxidation_type2 = ox_type2.get()
        oxidation_temp2 = float(temp2.get()) + 273
        oxidation_time2 = float(time2.get())

        oxidation_type3 = ox_type3.get()
        oxidation_temp3 = float(temp3.get()) + 273
        oxidation_time3 = float(time3.get())

        oxidation_type4 = ox_type4.get()
        oxidation_temp4 = float(temp4.get()) + 273
        oxidation_time4 = float(time4.get())

        oxidation_type5 = ox_type5.get()
        oxidation_temp5 = float(temp5.get()) + 273
        oxidation_time5 = float(time5.get())

        oxidationTypeMS = [oxidation_type1, oxidation_type2, oxidation_type3, oxidation_type4,oxidation_type5]
        temperatureMS = [oxidation_temp1, oxidation_temp2, oxidation_temp3, oxidation_temp4,oxidation_temp5]
        oxidationTimeMS = [oxidation_time1, oxidation_time2, oxidation_time3, oxidation_time4,oxidation_time5]

        if (oxidation_modeMS == "Deal Grove Model"):
            multiStageOxidationObj5 = multiStageOxidation(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj5.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
           # print(oxideThicknessList)

        elif (oxidation_modeMS == "Deal Grove + Massoud Model"):
            multiStageOxidationObj5 = multiStageOxidationMassoud(
                crystal_orientationMS, num, oxidationTypeMS, temperatureMS, oxidationTimeMS, initial_thicknessMS,
                thickness_flagMS)
            oxideThicknessList = multiStageOxidationObj5.calculateFinalOxideThickness()
            oxideThicknessList = [round(num, 3) for num in oxideThicknessList]
            #print(oxideThicknessList)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 1:").grid(row=14, column=0, sticky=E)
        res1 = Entry(msOxidation_screen, width=10)
        res1.insert(END, oxideThicknessList[1])
        res1.grid(row=14, column=1, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 2:").grid(row=15, column=0, sticky=E)
        res2 = Entry(msOxidation_screen, width=10)
        res2.insert(END, oxideThicknessList[2])
        res2.grid(row=15, column=1, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 3:").grid(row=14, column=2, sticky=E)
        res3 = Entry(msOxidation_screen, width=10)
        res3.insert(END, oxideThicknessList[3])
        res3.grid(row=14, column=3, pady=5)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 4:").grid(row=15, column=2, sticky=E)
        res4 = Entry(msOxidation_screen, width=10)
        res4.insert(END, oxideThicknessList[4])
        res4.grid(row=15, column=3, pady=10)

        Label(msOxidation_screen, text="Oxide Thickness after Stage 5:").grid(row=14, column=4, sticky=E)
        res5 = Entry(msOxidation_screen, width=10)
        res5.insert(END, oxideThicknessList[5])
        res5.grid(row=14, column=5, pady=5)

        Label(msOxidation_screen, text="Do you want to plot the graph?:").grid(row=24, column=0, sticky=E)
        btn1 = Button(msOxidation_screen, text='Yes', width=10, background="green", command=plotMSGraph)
        btn1.grid(row=24, column=1)
        btn2 = Button(msOxidation_screen, text='No', width=10, background="red", command=msOxidation_screen.destroy)
        btn2.grid(row=24, column=2)

def plotMSGraph():
    if(num == 2):
        multiStageOxidationObj2.calculateOxideThicknessGraph()
    elif(num == 3):
        multiStageOxidationObj3.calculateOxideThicknessGraph()
    elif(num == 4):
        multiStageOxidationObj4.calculateOxideThicknessGraph()
    elif(num == 5):
        multiStageOxidationObj5.calculateOxideThicknessGraph()




#Methods for Oxide Color Finder
def oxideColorScreen():
    global oxideColor_screen
    global thickness_color
    oxideColor_screen = Tk()
    oxideColor_screen.geometry("350x100+420+100")
    oxideColor_screen.title("Oxide Color Finder")
    Label(oxideColor_screen, text="Oxide Thickness (in um):").grid(row=0, column=0,sticky=E)
    thickness_color = Entry(oxideColor_screen, width=10)
    thickness_color.insert(END, "0")
    thickness_color.grid(row=0, column=1, pady=5)
    button1 = Button(oxideColor_screen, text='Submit', width=10, background="light green", command=getOCFields)
    button1.grid(row=5, column=1,pady=5)
    oxideColor_screen.mainloop()

def getOCFields():
    oxy_color=thickness_color.get()
    oxyColor= colour(oxy_color)
    result=oxyColor.calcthickness()
    if(result == "Out of range"):
        Label(oxideColor_screen, text="Thickness not found!!!:").grid(row=7, column=1)
    else:
        Label(oxideColor_screen, text="Oxide Color:").grid(row=7, column=0, sticky=E)
        res = Entry(oxideColor_screen, width=30)
        res.insert(END, result)
        res.grid(row=7, column=1, pady=10)


#Methods for Displaying Coefficients for Dry<100>,Dry<111>,Wet<100>,Wet<111>
def coefficientScreen():
    coeff_screen = Tk()
    coeff_screen.geometry("250x250+420+100")
    coeff_screen.title("Coefficients")
    l1 = Label(coeff_screen, text="Coefficients")
    l1.config(width=200)
    l1.config(font=("Courier",20, "bold"))
    l1.config(foreground="maroon")
    l1.pack(pady=20)
    button1 = Button(coeff_screen, text='Wet<100>', width=30, command=wet100)
    button1.pack(pady=5)
    button2 = Button(coeff_screen, text='Wet<111>', width=30, command=wet111)
    button2.pack(pady=5)
    button3 = Button(coeff_screen, text='Dry<100>', width=30, command=dry100)
    button3.pack(pady=5)
    button4 = Button(coeff_screen, text='Dry<111>', width=30, command=dry111)
    button4.pack(pady=5)

def wet100():
    wet100_screen = Tk()
    wet100_screen.geometry("300x100+420+100")
    wet100_screen.title("Wet<100>")
    Label(wet100_screen, text="B:Parabolic Rate Constant(um^2/hr):").grid(row=0, column=0, sticky=E)
    Label(wet100_screen, text="B:Activation Energy(eV):").grid(row=1, column=0, sticky=E)
    Label(wet100_screen, text="B/A:Linear Rate Constant(um/hr):").grid(row=2, column=0, sticky=E)
    Label(wet100_screen, text="B/A:Activation Energy(eV):").grid(row=3, column=0, sticky=E)
    a1 = Entry(wet100_screen)
    a1.insert(END,"386")
    a1.grid(row=0, column=1)
    a2 = Entry(wet100_screen)
    a2.insert(END, "0.78")
    a2.grid(row=1, column=1)
    a3 = Entry(wet100_screen)
    a3.insert(END, "9.7e7")
    a3.grid(row=2, column=1)
    a4 = Entry(wet100_screen)
    a4.insert(END, "2.05")
    a4.grid(row=3, column=1)

def wet111():
    wet111_screen = Tk()
    wet111_screen.geometry("300x100+420+100")
    wet111_screen.title("Wet<111>")
    Label(wet111_screen, text="B:Parabolic Rate Constant(um^2/hr):").grid(row=0, column=0, sticky=E)
    Label(wet111_screen, text="B:Activation Energy(eV):").grid(row=1, column=0, sticky=E)
    Label(wet111_screen, text="B/A:Linear Rate Constant(um/hr):").grid(row=2, column=0, sticky=E)
    Label(wet111_screen, text="B/A:Activation Energy(eV):").grid(row=3, column=0, sticky=E)
    a1 = Entry(wet111_screen)
    a1.insert(END, "386")
    a1.grid(row=0, column=1)
    a2 = Entry(wet111_screen)
    a2.insert(END, "0.78")
    a2.grid(row=1, column=1)
    a3 = Entry(wet111_screen)
    a3.insert(END, "1.63e8")
    a3.grid(row=2, column=1)
    a4 = Entry(wet111_screen)
    a4.insert(END, "2.05")
    a4.grid(row=3, column=1)

def dry100():
    dry100_screen = Tk()
    dry100_screen.geometry("300x100+420+100")
    dry100_screen.title("Dry<100>")
    Label(dry100_screen, text="B:Parabolic Rate Constant(um^2/hr):").grid(row=0, column=0, sticky=E)
    Label(dry100_screen, text="B:Activation Energy(eV):").grid(row=1, column=0, sticky=E)
    Label(dry100_screen, text="B/A:Linear Rate Constant(um/hr):").grid(row=2, column=0, sticky=E)
    Label(dry100_screen, text="B/A:Activation Energy(eV):").grid(row=3, column=0, sticky=E)
    a1 = Entry(dry100_screen)
    a1.insert(END, "772")
    a1.grid(row=0, column=1)
    a2 = Entry(dry100_screen)
    a2.insert(END, "1.23")
    a2.grid(row=1, column=1)
    a3 = Entry(dry100_screen)
    a3.insert(END, "3.71e6")
    a3.grid(row=2, column=1)
    a4 = Entry(dry100_screen)
    a4.insert(END, "2.00")
    a4.grid(row=3, column=1)

def dry111():
    dry111_screen = Tk()
    dry111_screen.geometry("300x100+420+100")
    dry111_screen.title("Dry<111>")
    Label(dry111_screen, text="B:Parabolic Rate Constant(um^2/hr):").grid(row=0, column=0, sticky=E)
    Label(dry111_screen, text="B:Activation Energy(eV):").grid(row=1, column=0, sticky=E)
    Label(dry111_screen, text="B/A:Linear Rate Constant(um/hr):").grid(row=2, column=0, sticky=E)
    Label(dry111_screen, text="B/A:Activation Energy(eV):").grid(row=3, column=0, sticky=E)
    a1 = Entry(dry111_screen)
    a1.insert(END, "772")
    a1.grid(row=0, column=1)
    a2 = Entry(dry111_screen)
    a2.insert(END, "1.23")
    a2.grid(row=1, column=1)
    a3 = Entry(dry111_screen)
    a3.insert(END, "6.23e6")
    a3.grid(row=2, column=1)
    a4 = Entry(dry111_screen)
    a4.insert(END, "2.00")
    a4.grid(row=3, column=1)


#Methods for displaying important graphs for oxidation and rate constants
def graphScreen():
    graph_screen = Tk()
    graph_screen.geometry("250x250+420+100")
    graph_screen.title("Graphs")
    l1 = Label(graph_screen, text="Graphs")
    l1.config(width=200)
    l1.config(font=("Courier", 20, "bold"))
    l1.config(foreground="maroon")
    l1.pack(pady=20)
    button1 = Button(graph_screen, text='Oxidation <100>', width=30, command=img100)
    button1.pack(pady=5)
    button2 = Button(graph_screen, text='Oxidation <111>', width=30, command=img111)
    button2.pack(pady=5)
    button3 = Button(graph_screen, text='Linear Rate Constant', width=30, command=linear_img)
    button3.pack(pady=5)
    button4 = Button(graph_screen, text='Parabolic Rate Constant', width=30, command=parabolic_img)
    button4.pack(pady=5)

def img100():
    top = Toplevel()
    top.geometry("800x546")
    top.title("<100> Oxidation ")
    img = ImageTk.PhotoImage(Image.open("100.JPG"))
    l2 = Label(top,image=img)
    l2.pack()
    top.mainloop()

def img111():
    top = Toplevel()
    top.geometry("800x537")
    top.title("<111> Oxidation ")
    img = ImageTk.PhotoImage(Image.open("111.JPG"))
    l2 = Label(top, image=img)
    l2.pack()
    top.mainloop()

def linear_img():
    top = Toplevel()
    top.geometry("800x594")
    top.title("Linear Rate Constant ")
    img = ImageTk.PhotoImage(Image.open("linear.JPG"))
    l2 = Label(top, image=img)
    l2.pack()
    top.mainloop()

def parabolic_img():
    top = Toplevel()
    top.geometry("800x609")
    top.title("Parabolic Rate Constant")
    img = ImageTk.PhotoImage(Image.open("parabolic.JPG"))
    l2 = Label(top, image=img)
    l2.pack()
    top.mainloop()


introScreen()

