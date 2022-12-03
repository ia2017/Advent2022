def Day1():

    file = "Inputs/Day1.txt"
    with open(file) as f:
        lines = f.read().splitlines()

    #print(lines)

    workingList = []
    sum=0
    for i in range(len(lines)):
        if lines[i] == "":
            workingList.append(sum)
            sum=0
        else:
            sum+=int(lines[i])

    maxSum = max(workingList)
    print("Max sum: " + str(maxSum))

    workingList.sort()

    top3Sum = 0
    for i in workingList[-3:]:
        top3Sum += i
    print("Top 3 Sum: " + str(top3Sum))

def Day2():
    file = "Inputs/Day2.txt"
    with open(file) as f:
        lines = f.read().splitlines()

    workingScore = 0

    #dict = {"Rock" : ["A", "X"], "Paper" : ["B", "Y"], "Scissors" : ["C", "Z"]}

    for line in lines:
        # For chosen
        if line[2] == "X":
            workingScore +=1
        elif line[2] == "Y":
            workingScore +=2
        elif line[2] == "Z":
            workingScore +=3

        # For draws
        if line[0] == "A" and line[2] == "X":
            workingScore+=3
        elif line[0] == "B" and line[2] == "Y":
            workingScore+=3

        elif line[0] == "C" and line[2] == "Z":
            workingScore+=3

        # For wins
        elif line[0] == "A" and line[2] == "Y":
            workingScore += 6
        elif line[0] == "B" and line[2] == "Z":
            workingScore += 6
        elif line[0] == "C" and line[2] == "X":
            workingScore += 6

    print("Part 1: " + str(workingScore))

    # For Part 2

    workingScore = 0

    for line in lines:

        # For loss
        if line[2] == "X":
            if line[0] == "A":
                workingScore += 3
            elif line[0] == "B":
                workingScore += 1
            elif line[0] == "C":
                workingScore += 2

        if line[2] == "Y":
            if line[0] == "A":
                workingScore += 1 + 3
            elif line[0] == "B":
                workingScore += 2 + 3
            elif line[0] == "C":
                workingScore += 3 + 3

        if line[2] == "Z":
            if line[0] == "A":
                workingScore += 2 + 6
            elif line[0] == "B":
                workingScore += 3 + 6
            elif line[0] == "C":
                workingScore += 1 + 6

    print("Part 2 : " + str(workingScore))



def Day3():

    file = "Inputs/Day3.txt"
    with open(file) as f:
        lines = f.read().splitlines()

    sum=0

    for line in lines:
        midpoint = int(len(line) / 2)

        for chr in line[:midpoint]:
            if chr in line[midpoint:]:
                workingChar = chr
                break

        if workingChar.isupper() == True:
            sum += ord(chr) - 64 + 26

        else:
            sum += ord(chr) - 96

    print(sum)

    # Part 2
    i = 0
    sum = 0
    workingLines = []

    for line in lines:

        if i == 2:
            for chr in line:
                if chr in workingLines[0] and chr in workingLines[1]:
                    workingChar = chr
                    break

            if workingChar.isupper() == True:
                sum += ord(chr) - 64 + 26

            else:
                sum += ord(chr) - 96

            workingLines = []

            i=0
        else:
            workingLines.append(line)
            i+=1


    print(sum)




