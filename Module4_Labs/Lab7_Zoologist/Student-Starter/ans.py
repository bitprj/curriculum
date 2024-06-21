from math import log
from math import sqrt
import csv

def readFileintoDict():
    filename= "Animals.txt"
    with open(filename, 'r') as file:
        result = {}
        index = 0
        for line in file.read().split("\n"):
            noTabs = line.split("\t")
            lastElement = noTabs[len(noTabs) - 1]
            result[index] = lastElement
            index += 1
    return result

# Not needed for checkpoint
# def assignRankings(equations):
#     # rank values descending order
#     rankings = []
#     while (not max(equations) == -1):
#         nextValue = max(equations)
#         index = equations.index(nextValue) # find index
#         rankings.append(index)
#         equations[index] = -1
#     # get ascending order
#     rankings.reverse()
#     return rankings

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
    # Not needed for checkpoint
    # ranks = assignRankings(equations.copy()) # ranks = {index : rank}

    # for i in range(len(ranks)):
        # print(animals[ranks[i]])

    invalidInput=True
    while (invalidInput):
        print("Please chose a sorting method:")
        print("1.(Bubble) Sort")
        print("2.(Insertion) Sort")
        print("3.(Selection) Sort")
        x=input("")
        if(x=="1"or x=="bubble"):
            invalidInput=False
        elif(x=="2"or x=="insertion"):
            invalidInput=False
        elif(x=="3"or x=="selection"):
            invalidInput=False
        else:
            print("Not a valid input, try again.")
main()
