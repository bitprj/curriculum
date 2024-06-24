from math import log
from math import sqrt
import csv
def assignRankings(equations):
    # rank values descending order
    rankings = []
    while (not max(equations) == -1):
        nextValue = max(equations)
        index = equations.index(nextValue) # find index
        rankings.append(index)
        equations[index] = -1
    # get ascending order
    rankings.reverse()
    return rankings
def bubbleSort(arr):
    n = len(arr)
    print(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        print(arr)
def selectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
def readFileintoDict():
    filename= “Animals.txt”
    with open(filename, ‘r’) as file:
        result = {}
        index = 0
        for line in file.read().split(“\n”):
            noTabs = line.split(“\t”)
            lastElement = noTabs[len(noTabs) - 1]
            result[index] = lastElement
            index += 1
    return result
def main():
    n = 1
    equations = [
        n**2,
        20*n**2+5*n+7,
        n+log(n)+7,
        3**n,
        log(n)/(n**2),
        (n+1)/(sqrt(1+n**2)),
        (n**n)/(sqrt(log(n**4))+10),
        n*log(n**2),
        6**n,
        sqrt(log(n)),
        n**n,
        n**3*log(n)+100,
        sqrt(n**3),
        n**3,
        (n+1)/(sqrt(1+n**2))
    ]
    animals = readFileintoDict() # animals = {index : animalName}
    ranks = assignRankings(equations.copy()) # ranks = {index : rank}
    for i in range(len(ranks)):
        print(animals[ranks[i]])
    invalidInput=True
    while (invalidInput):
        print(“Please chose a sorting method:“)
        print(“1.(Bubble) Sort”)
        print(“2.(Insertion) Sort”)
        print(“3.(Selection) Sort”)
        x=input(“”)
        if(x==“1”or x==“bubble”):
            bubbleSort(ranks.copy())
            invalidInput=False
        elif(x==“2”or x==“insertion”):
            insertionSort(ranks.copy())
            invalidInput=False
        elif(x==“3”or x==“selection”):
            selectionSort(ranks.copy())
            invalidInput=False
        else:
            print(“Not a valid input, try again.“)
