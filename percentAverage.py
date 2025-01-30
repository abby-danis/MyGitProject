def calcTotal(marks):
    total = 0
    for n in range(0, len(marks)):
        total += marks[n]
    return total

testMarks = []
testMarks.append(int(input("Please enter mark #1: ")))
testMarks.append(int(input("Please enter mark #2: ")))
# todo, add prompt for 3rd mark

total = calcTotal(testMarks)
print("Total: ",str(total)+"\n")