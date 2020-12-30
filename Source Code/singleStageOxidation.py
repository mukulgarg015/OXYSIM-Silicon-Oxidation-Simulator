import math

boltzmannConstant = 8.617 * 10 ** (-5)


class SingleStageOxidation:

    crystalOrientation = 0
    oxidationType = " "  # wet = 0, dry = 1
    temperature = 0
    oxidationTime = 0
    initialOxideThickness = 0
    initialOxideThicknessAvailable = " "

    def __init__(self, crystalOrientation, oxidationType, temperature, oxidationTime, initialOxideThickness, initialOxideThicknessAvailable):
        self.crystalOrientation = crystalOrientation
        self.oxidationType = oxidationType  # wet = 0, dry = 1
        self.temperature = temperature
        self.oxidationTime = oxidationTime  # in hr
        if (initialOxideThicknessAvailable == "Y"):
            self.initialOxideThickness = initialOxideThickness
        else:
            if oxidationType == "Wet":
                self.initialOxideThickness = 0
            else:
                self.initialOxideThickness = 0.025

    def calculateOxideThickness(self):
        if (self.oxidationType == "Wet" and self.crystalOrientation == 100):
            linearCoefficient = 9.7 * (10 ** 7)
            parabolicCoefficient = 386
            linearActivationEnergy = 2.05
            parabolicActivationEnergy = 0.78

        elif (self.oxidationType == "Wet" and self.crystalOrientation == 111):
            linearCoefficient = 1.63 * (10 ** 8)
            parabolicCoefficient = 386
            linearActivationEnergy = 2.05
            parabolicActivationEnergy = 0.78

        elif (self.oxidationType == "Dry" and self.crystalOrientation == 100):
            linearCoefficient = 3.71 * (10 ** 6)
            parabolicCoefficient = 772
            linearActivationEnergy = 2
            parabolicActivationEnergy = 1.23

        elif (self.oxidationType == "Dry" and self.crystalOrientation == 111):
            linearCoefficient = 6.23 * (10 ** 6)
            parabolicCoefficient = 772
            linearActivationEnergy = 2
            parabolicActivationEnergy = 1.23

        BbyA = linearCoefficient * \
            math.exp(-1 * linearActivationEnergy /
                     (boltzmannConstant * self.temperature))
        B = parabolicCoefficient * \
            math.exp(-1 * parabolicActivationEnergy /
                     (boltzmannConstant * self.temperature))

        A = B / BbyA

        tau = self.initialOxideThickness ** 2 / B + self.initialOxideThickness / BbyA

        finalOxideThickness = 0.5 * A * \
            (math.sqrt(1 + (4 * B / A ** 2) * (self.oxidationTime + tau)) - 1)


        return finalOxideThickness
