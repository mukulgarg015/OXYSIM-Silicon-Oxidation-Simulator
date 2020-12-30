import math

boltzmannConstant = 8.617 * 10 ** (-5)


class SingleStageOxidationMassoud:

    crystalOrientation = 0
    oxidationType = " "
    temperature = 0
    oxidationTime = 0
    initialOxideThickness = 0
    initialOxideThicknessAvailable = " "

    def __init__(self, crystalOrientation, oxidationType, temperature, oxidationTime, initialOxideThickness, initialOxideThicknessAvailable):
        self.crystalOrientation = crystalOrientation
        self.oxidationType = oxidationType
        self.temperature = temperature
        self.oxidationTime = oxidationTime
        if (initialOxideThicknessAvailable == "Y"):
            self.initialOxideThickness = initialOxideThickness
        else:
            if oxidationType == "Wet":
                self.initialOxideThickness = 0
            else:
                self.initialOxideThickness = 0

    def calculateOxideThickness(self):

        if self.oxidationType == "Wet":
            if self.crystalOrientation == 100:
                linearCoefficient = 9.7 * (10 ** 7)
                parabolicCoefficient = 386
                linearActivationEnergy = 2.05
                parabolicActivationEnergy = 0.78

            elif self.crystalOrientation == 111:
                linearCoefficient = 1.63 * (10 ** 8)
                parabolicCoefficient = 386
                linearActivationEnergy = 2.05
                parabolicActivationEnergy = 0.78

            BbyA = linearCoefficient * \
                math.exp(-1 * linearActivationEnergy /
                         (boltzmannConstant * self.temperature))
            B = parabolicCoefficient * \
                math.exp(-1 * parabolicActivationEnergy /
                         (boltzmannConstant * self.temperature))

            A = B/BbyA

            tau = self.initialOxideThickness ** 2 / B + self.initialOxideThickness / BbyA

            finalOxideThickness = 0.5 * A * \
                (math.sqrt(1 + (4 * B / A ** 2) * (self.oxidationTime + tau)) - 1)
            return finalOxideThickness

        elif self.oxidationType == "Dry":
            if (self.crystalOrientation == 111 and self.temperature < 1273):
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

            elif (self.crystalOrientation == 111 and self.temperature >= 1273):
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

            elif (self.crystalOrientation == 100 and self.temperature < 1273):
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

            elif (self.crystalOrientation == 100 and self.temperature >= 1273):
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
                         (boltzmannConstant * self.temperature))
            B = parabolicCoefficient * \
                math.exp(-1 * parabolicActivationEnergy /
                         (boltzmannConstant * self.temperature))

            A = B/BbyA

            k1 = k1Coefficient * \
                math.exp(-1 * ActivationEnergyk1 /
                         (boltzmannConstant * self.temperature))

            k2 = k2Coefficient * \
                math.exp(-1 * ActivationEnergyk2 /
                         (boltzmannConstant * self.temperature))

            tau1 = tau1Coefficient * \
                math.exp(-1 * ActivationEnergytau1 /
                         (boltzmannConstant * self.temperature))

            tau2 = tau2Coefficient * \
                math.exp(-1 * ActivationEnergytau2 /
                         (boltzmannConstant * self.temperature))

            m1 = k1 * tau1
            m2 = k2 * tau2
            m0 = (self.initialOxideThickness ** 2) * 10**6 + \
                A * self.initialOxideThickness * 1000

            finalOxideThickness = (math.sqrt((A ** 2 / 4) + B * (self.oxidationTime * 60) + m1 * (
                1 - math.exp(-1 * self.oxidationTime * 60 / tau1)) + m2 * (1 - math.exp(-1 * self.oxidationTime * 60 / tau2)) + m0) - A/2)

        return (finalOxideThickness/1000)