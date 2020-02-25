# List Overlap
# Alexander Fraser
# 24 Febuary 2020

"""
Requirements:
- random

Write a program that returns a list that contains only
the elements that are common between the lists
(without duplicates). Make sure your program works on two
lists of different sizes.
"""

from random import randint

def generateRandomList():

    inputList = []
    listLength = randint(1,20)

    for x in range(0, listLength):
        inputList.append(randint(1,10))

    return inputList

def compareLists(list1, list2):
    outputList = []

    for element in list1:
        if (element in list2) and (element not in outputList):
            outputList.append(element)

    outputList = sorted(outputList)
    return outputList

def main():
    list1 = generateRandomList()
    list2 = generateRandomList()
    outputList = compareLists(list1, list2)
    print(list1, "\n", list2, "\n", outputList)

if __name__ == "__main__":
    main()