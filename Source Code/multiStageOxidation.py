import math
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image

boltzmannConstant = 8.617 * 10 ** (-5)


class multiStageOxidation:

    crystalOrientation = 0
    numOxidationStages = 0
    oxidationType = []
    temperature = []
    oxidationTime = []
    initialOxideThickness = []
    initialOxideThicknessAvailable = " "

    def __init__(self, crystalOrientation, numOxidationStages, oxidationType, temperature, oxidationTime, initialOxideThickness, initialOxideThicknessAvailable):
        self.crystalOrientation = crystalOrientation
        self.numOxidationStages = numOxidationStages
        self.oxidationType = oxidationType
        self.temperature = temperature
        self.oxidationTime = oxidationTime  # in hr
        emptyList = [None] * (self.numOxidationStages + 1)
        if (initialOxideThicknessAvailable == "Y"):
            emptyList[0] = initialOxideThickness
            self.initialOxideThickness = emptyList
        else:
            if oxidationType[0] == "Wet":
                emptyList[0] = 0
                self.initialOxideThickness = emptyList
            else:
                emptyList[0] = 0.025
                self.initialOxideThickness = emptyList

    def calculateOxideThickness(self, crystalOrientation, oxidationType, temperature, oxidationTime, initialOxideThickness):
        if (oxidationType == "Wet" and crystalOrientation == 100):
            linearCoefficient = 9.7 * (10 ** 7)
            parabolicCoefficient = 386
            linearActivationEnergy = 2.05
            parabolicActivationEnergy = 0.78

        elif (oxidationType == "Wet" and crystalOrientation == 111):
            linearCoefficient = 1.63 * (10 ** 8)
            parabolicCoefficient = 386
            linearActivationEnergy = 2.05
            parabolicActivationEnergy = 0.78

        elif (oxidationType == "Dry" and crystalOrientation == 100):
            linearCoefficient = 3.71 * (10 ** 6)
            parabolicCoefficient = 772
            linearActivationEnergy = 2
            parabolicActivationEnergy = 1.23

        elif (oxidationType == "Dry" and crystalOrientation == 111):
            linearCoefficient = 6.23 * (10 ** 6)
            parabolicCoefficient = 772
            linearActivationEnergy = 2
            parabolicActivationEnergy = 1.23

        BbyA = linearCoefficient * \
            math.exp(-1 * linearActivationEnergy /
                     (boltzmannConstant * temperature))
        B = parabolicCoefficient * \
            math.exp(-1 * parabolicActivationEnergy /
                     (boltzmannConstant * temperature))

        A = B / BbyA

        tau = initialOxideThickness ** 2 / B + initialOxideThickness / BbyA

        finalOxideThickness = 0.5 * A * \
            (math.sqrt(1 + (4 * B / A ** 2) * (oxidationTime + tau)) - 1)

        return finalOxideThickness

    def calculateFinalOxideThickness(self):

        for i in range(0, self.numOxidationStages):
            self.initialOxideThickness[i+1] = self.calculateOxideThickness(
                self.crystalOrientation, self.oxidationType[i], self.temperature[i], self.oxidationTime[i], self.initialOxideThickness[i])

        # self.initialOxideThickness.pop(0)

        return self.initialOxideThickness

    def calculateOxideThicknessGraph(self):
        xValues = []
        yValues = []

        for i in range(0, self.numOxidationStages):
            if (i == 0):
                j = 0
            else:
                j += self.oxidationTime[i - 1]

            for k in np.linspace(0, self.oxidationTime[i], 10, True):

                y = self.calculateOxideThickness(
                    self.crystalOrientation, self.oxidationType[i], self.temperature[i], k, self.initialOxideThickness[i])
                xValues.append(j+k)
                yValues.append(y)

                if (k == self.oxidationTime[i]):
                    self.initialOxideThickness[i+1] = self.calculateOxideThickness(
                        self.crystalOrientation, self.oxidationType[i], self.temperature[i], k, self.initialOxideThickness[i])
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
        top.title("Plot")
        img = ImageTk.PhotoImage(Image.open("plot.png"))
        l2 = Label(top, image=img)
        l2.pack()
        top.mainloop()