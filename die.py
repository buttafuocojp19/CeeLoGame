#!/usr/bin/env python
__author__ = "James Buttafuoco"

from random import randint


class Die(object):
    def __init__(self, openingNumberOfSides=6, openingStartingValue=1, openingIncrement=1, openingColor="White", openingName="Bones"):
        self.numberOfSides = openingNumberOfSides
        self.startingValue = openingStartingValue
        self.increment = openingIncrement
        self.color = openingColor
        self.name = openingName
        self.value = 1

    def __str__(self):
        return "{5} die named {0} has {1} sides, starts at {2} increments by {4} and has a current value of {3}".format(self.name, self.numberOfSides, self.startingValue * self.increment, self.value, self.increment, self.color)

    def roll(self):
        self.value = randint(self.startingValue, self.numberOfSides + (self.startingValue - 1)) * self.increment
        return self.value

    def setValue(self, newValue):
        if self.startingValue * self.increment <= newValue <= self.numberOfSides * self.increment and \
           not newValue % self.increment:   # Test for a value within range and a multiple of the increment.
            self.value = newValue
        else:
            raise ValueError

    def getValue(self):
        return self.value

    def setNumberOfSides(self, newNumberOfSides):
        self.numberOfSides = newNumberOfSides

    def getNumberOfSides(self):
        return self.numberOfSides

    def setStartingValue(self, newStartingValue):
        self.startingValue = newStartingValue

    def getStartingValue(self):
        return self.startingValue

    def setIncrement(self, newIncrement):
        self.increment = newIncrement

    def getIncrement(self):
        return self.increment

    def setColor(self, newColor):
        if type(newColor) is str:
            self.color = newColor
        else:
            raise ValueError

    def getColor(self):
        return self.color

    def setName(self, newName):
        if type(newName) is str:
            self.name = newName
        else:
            raise ValueError

    def getName(self):
        return self.name

