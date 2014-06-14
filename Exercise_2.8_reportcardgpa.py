'''
Write a function report card where the user can enter each of his grades,
after which the program prints out a report card with GPA.
Remember to ask the user how many classes he took
(think -why would we need to ask this?
Could we write the program a different way, which wouldn’t need that info?).
'''

def report_card():
    
    # Takes a numerical grade [0, 100] and converts it into GPA [0, 4]
    def gpa(grade):
        if(grade >= 93):
            return 4.0
        elif(grade >= 90):
            return 3.67
        elif(grade >= 87):
            return 3.33
        elif(grade >= 83):
            return 3.0
        elif(grade >= 80):
            return 2.67
        elif(grade >= 77):
            return 2.33
        elif(grade >= 73):
            return 2.0
        elif(grade >= 70):
            return 1.67
        elif(grade >= 67):
            return 1.33
        elif(grade >= 63):
            return 1.0
        elif(grade >= 60):
            return 0.67
        else:
            return 0.0

    # Takes a list of numbers and returns the average of all the numbers in the list.
    def avgGPA(listofgpa):
        total = 0
        length = len(listofgpa)
        for gpa in listofgpa:
            total += gpa
        return total/length

    classes = input("How many classes did you take? ")
    classNames = []
    gradeList = []
    gpaList = []
    
    for i in range(classes):
        classNames.append(raw_input("Name of class #" + str(i+1) + "? "))
        grade = input("What was your grade on a scale of 0 to 100? ")
        gradeList.append(grade)
        gpaList.append(gpa(grade))

    print
    print "=====REPORT CARD====="
    for i in range(classes):
        print classNames[i] + " .... " + str(gradeList[i]) + " .... " + str(gpaList[i])
    print "Overall GPA: " + str(avgGPA(gpaList))


report_card()















