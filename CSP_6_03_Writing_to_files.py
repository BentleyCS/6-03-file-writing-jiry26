import random


#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    with open(fileName, "w") as file:
        for n in inputList:
            file.write(f"{n}\n")
    return fileName
#writeFile([1,"hello",49,"haha"],"random file")


def sortNames(sourceName, targetName):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    randomList = []
    with open(sourceName, "r") as sourceFile:
        with open(targetName, "w") as targetFile:
            for line in sourceFile:
                randomList.append(line)
            randomList.sort()
            for n in randomList:
                targetFile.write(n)
#sortNames("fileName","targetName")

def get_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def highScore( newScore: int):
    scoresList = []
    with open("scores.txt", "a") as file:
        file.write(f"{newScore}\n")
    with open("scores.txt", "r") as file:
        for line in file:
            scoresList.append(int(line))
    avg = get_average(scoresList)
    return(avg)

    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    pass
print(highScore(30))
#highScore(random.randint(1,100))

