
linesCount = 0

def runFile(name):
    print("Loading file:",name)
    global linesCount
    with open(name, 'r',encoding='utf8') as file:
        # read a list of lines into data
        data = file.readlines()

    data = [line.rstrip('\n') for line in data]
    newData = []

    for line in data:
        if line and line[0] != "[" and not line.strip().isdigit() and (inrange(line[-1] or line[-1] == '♪')):
            newL = reversePunctuation(line)
            newData = newData + [newL]
        else:
            newData = newData + [line]

    newData = [line + "\n" for line in newData]
    suffix = name[name.rfind(('.')):]
    newName = name[0:name.rfind('.')]+ "_flipped"+ suffix
    print("Fliiped ", linesCount, "rows out of ", len(data))
    print("Writing new file:",newName)
    with open(newName, 'w', encoding='utf8') as file:
        file.writelines( newData )

def inrange(char):
    if (char >= ' ' and char < '0') or (char > '9' and char < 'A') or char == '♪':
        return True
    else: return False


def reversePunctuation(line):
    global linesCount
    counter = 1;
    newLine = ''
    if line == '' or line.strip() == '':
        return line
    else:

        linesCount += 1
        while inrange(line[-counter]):
            newLine += line[-counter]
            counter = counter+1

        newLine = newLine[::-1]
        newLine = newLine + line[0:-counter+1]
        return newLine

