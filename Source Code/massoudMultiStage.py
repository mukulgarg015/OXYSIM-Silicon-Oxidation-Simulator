import math
import numpy as np
#import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

boltzmannConstant = 8.617 * 10 ** (-5)


class multiStageOxidationMassoud:

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
            emptyList[0] = 0
            self.initialOxideThickness = emptyList

    def calculateOxideThickness(self, crystalOrientation, oxidationType, temperature, oxidationTime, initialOxideThickness):

        if oxidationType == "Wet":
            if crystalOrientation == 100:
                linearCoefficient = 9.7 * (10 ** 7)
                parabolicCoefficient = 386
                linearActivationEnergy = 2.05
                parabolicActivationEnergy = 0.78

            elif crystalOrientation == 111:
                linearCoefficient = 1.63 * (10 ** 8)
                parabolicCoefficient = 386
                linearActivationEnergy = 2.05
                parabolicActivationEnergy = 0.78

            BbyA = linearCoefficient * \
                math.exp(-1 * linearActivationEnergy /
                         (boltzmannConstant * temperature))
            B = parabolicCoefficient * \
                math.exp(-1 * parabolicActivationEnergy /
                         (boltzmannConstant * temperature))

            A = B/BbyA

            tau = initialOxideThickness ** 2 / B + initialOxideThickness / BbyA

            finalOxideThickness = 0.5 * A * \
                (math.sqrt(1 + (4 * B / A ** 2) * (oxidationTime + tau)) - 1)
            return finalOxideThickness

        elif oxidationType == "Dry":
            if (crystalOrientation == 111 and temperature < 1273):
                linearCoefficient = 1.32 * (10 ** 71)
                parabolicCoefficient = 1.34 * (10 ** 9)
                linearActivationEnergy = 1.74
                parabolicActivationEnergy = 1.71
                ActivationEnergyk1 = 1.74
                ActivationEnergyk2 = 1.76
                ActivationEnergytau1 = 1.45
                ActivationEnergytau2 = 1.90
                tau1Coefficient = 1.72 * (10 ** -6)
                tau2Coefficient = 1.56 * (10 ** -7)
                k1Coefficient = 2.70 * (10 ** 9)
                k2Coefficient = 1.33 * (10 ** 9)

            elif (crystalOrientation == 111 and temperature >= 1273):
                linearCoefficient = 6.50 * (10 ** 11)
                parabolicCoefficient = 2.56 * (10 ** 5)
                linearActivationEnergy = 2.95
                parabolicActivationEnergy = 0.76
                ActivationEnergyk1 = 1.74
                ActivationEnergyk2 = 1.76
                ActivationEnergytau1 = 1.45
                ActivationEnergytau2 = 1.90
                tau1Coefficient = 1.72 * (10 ** -6)
                tau2Coefficient = 1.56 * (10 ** -7)
                k1Coefficient = 2.70 * (10 ** 9)
                k2Coefficient = 1.33 * (10 ** 9)

            elif (crystalOrientation == 100 and temperature < 1273):
                linearCoefficient = 7.35 * (10 ** 6)
                parabolicCoefficient = 1.70 * (10 ** 11)
                linearActivationEnergy = 1.76
                parabolicActivationEnergy = 2.22
                ActivationEnergyk1 = 2.18
                ActivationEnergyk2 = 2.28
                ActivationEnergytau1 = 1.38
                ActivationEnergytau2 = 1.88
                tau1Coefficient = 4.14 * (10 ** -6)
                tau2Coefficient = 2.71 * (10 ** -7)
                k1Coefficient = 2.49 * (10 ** 11)
                k2Coefficient = 3.72 * (10 ** 11)

            elif (crystalOrientation == 100 and temperature >= 1273):
                linearCoefficient = 3.53 * (10 ** 12)
                parabolicCoefficient = 1.31 * (10 ** 5)
                linearActivationEnergy = 3.20
                parabolicActivationEnergy = 0.68
                ActivationEnergyk1 = 2.18
                ActivationEnergyk2 = 2.28
                ActivationEnergytau1 = 1.38
                ActivationEnergytau2 = 1.88
                tau1Coefficient = 4.14 * (10 ** -6)
                tau2Coefficient = 2.71 * (10 ** -7)
                k1Coefficient = 2.49 * (10 ** 11)
                k2Coefficient = 3.72 * (10 ** 11)

            BbyA = linearCoefficient * \
                math.exp(-1 * linearActivationEnergy /
                         (boltzmannConstant * temperature))
            B = parabolicCoefficient * \
                math.exp(-1 * parabolicActivationEnergy /
                         (boltzmannConstant * temperature))

            A = B/BbyA

            k1 = k1Coefficient * \
                math.exp(-1 * ActivationEnergyk1 /
                         (boltzmannConstant * temperature))

            k2 = k2Coefficient * \
                math.exp(-1 * ActivationEnergyk2 /
                         (boltzmannConstant * temperature))

            tau1 = tau1Coefficient * \
                math.exp(-1 * ActivationEnergytau1 /
                         (boltzmannConstant * temperature))

            tau2 = tau2Coefficient * \
                math.exp(-1 * ActivationEnergytau2 /
                         (boltzmannConstant * temperature))

            m1 = k1 * tau1
            m2 = k2 * tau2
            m0 = (initialOxideThickness ** 2) * 10**6 + \
                A * initialOxideThickness * 1000

            finalOxideThickness = (math.sqrt((A ** 2 / 4) + B * (oxidationTime * 60) + m1 * (
                1 - math.exp(-1 * oxidationTime * 60 / tau1)) + m2 * (1 - math.exp(-1 * oxidationTime * 60 / tau2)) + m0) - A/2)

            return (finalOxideThickness/1000)

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