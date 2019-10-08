f = open('data.csv', 'r')
text = ""
firstCycle = True
for line in f:
    if firstCycle:
        firstCycle = False
        text = text + line + "\n"
        continue
    line = line.replace(",", ".")
    text = text + line + "\n"

w = open('newData.csv', 'w')
w.write(text)
w.close()