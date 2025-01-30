def calcTotal(marks):
    total = 0
    for n in range(0, len(marks)):
        total += marks[n]
    return total

def averageGrade(marks):
   total = calcTotal(marks)
   average = total / len(marks)
   return average 

def calcGPA(average):
    return (average/100)*4
    


testMarks = []
testMarks.append(int(input("Please enter mark #1: ")))
testMarks.append(int(input("Please enter mark #2: ")))
testMarks.append(int(input("Please enter mark #3: ")))

total = calcTotal(testMarks)
average = averageGrade(testMarks)
Gpa = calcGPA(average)

print("Total: ",str(total)+"\n")
print("Average Grade: ",average)
print("GPA: ", Gpa)
