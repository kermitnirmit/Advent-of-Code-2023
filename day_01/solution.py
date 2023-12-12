import re
f = [x for x in open("input.txt").read().strip().split("\n")]

s = 0

v = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
for line in f:
    firstNum = re.search(r"\d", line) # first digit
    if firstNum:
        firstNum = (firstNum.start(), int(firstNum.group())) #index, value
    else:
        firstNum = (0, 0)
    for q in v:
        if line.find(q) != -1 and line.find(q) <= firstNum[0]:
            firstNum = (line.find(q), v[q])
    lastNum = re.search(r"\d", line[::-1])
    if lastNum:
        lastNum = (len(line) - lastNum.start() - 1, int(lastNum.group()))
    else:
        lastNum = (0,0)
    # print(lastNum)
    for q in v:
        if line.rfind(q) != -1 and line.rfind(q) > lastNum[0]:
            lastNum = (line.rfind(q), v[q])
    # print(firstNum[1] * 10 + lastNum[1])
    s += (firstNum[1] * 10 + lastNum[1])
print(s)