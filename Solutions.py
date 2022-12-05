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

def Day4():

    file = "Inputs/Day4.txt"

    with open(file) as f:
        lines = f.read().splitlines()

    count = 0
    count2 = 0
    for line in lines:
        line = line.split(",")
        pairs = []

        workingMin = 1e9
        workingMax = -1e9

        for subline in line:
            subline = subline.split("-")
            subline[0] = int(subline[0])
            subline[1] = int(subline[1])

            pairs.append(subline)

        if (pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]) or (pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1]):
            count += 1
            count2 += 1
        elif (pairs[0][0] >= pairs[1][1] and pairs[0][1] <= pairs[1][0]) or (pairs[0][0] <= pairs[1][1] and pairs[0][1] >= pairs[1][0]):
            count2 += 1

    print(count)
    print(count2)

def Day5():

    file = "Inputs/Day5.txt"

    with open(file) as f:
        lines = f.read().splitlines()

    currentRow = 0

    stacks = [[],[],[],[],[],[],[],[],[]]
    orders = []

    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []

    delta = 4
    for row in lines:

        currentRow += 1

        if currentRow < 9:

            if currentRow > 4:
                stacks[0].append(row[1])
                stacks[1].append(row[1 + delta])
                stacks[2].append(row[1 + delta * 2])
                stacks[3].append(row[1 + delta * 3])
                stacks[4].append(row[1 + delta * 4])
                stacks[5].append(row[1 + delta * 5])
                stacks[6].append(row[1 + delta * 6])
                stacks[7].append(row[1 + delta * 7])
                stacks[8].append(row[1+ delta*8])

            else:
                stacks[0].append(row[1])
                stacks[1].append(row[1 + delta])
                stacks[2].append(row[1 + delta * 2])
                stacks[3].append(row[1 + delta * 3])
                stacks[4].append(row[1 + delta * 4])
                stacks[5].append(row[1 + delta * 5])
                stacks[6].append(row[1 + delta * 6])
                stacks[7].append(row[1 + delta * 7])

        if currentRow == 9:
            for i in range(len(stacks)):
                for j in range(len(stacks[i])):
                    if " " in stacks[i]:
                        stacks[i].remove(" ")




        elif currentRow > 10:
            row=row.replace("move ", "").replace("from ", "").replace("to ", "")
            row=row.split(" ")
            orders.append(row)
            #print(row)
            origin = int(row[1]) - 1
            dest = int(row[2]) - 1
            load = int(row[0])

            for i in range(load):
                continue


















