#python program to prompt for a score between 0.0 and 1.0. Create a function called ComputeGrade that takes a score as its parameter and returns a grade as a string. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table.

grade = {
    0.9:"A",
    0.8:"B",
    0.7:"C",
    0.6:"D",
    0.5:"E",
}

def ComputeGrade(score):
    if score > 0.9:
        print(grade[0.9])
    elif score > 0.8:
        print(grade[0.8])
    elif score > 0.8:
        print(grade[0.7])
    elif score > 0.8:
        print(grade[0.6])
    else:
        print(grade[0.5])

while True:
    try:
        score = float(input("Enter the score of student:"))
        if score>=0.0 and score<=1.0:
            ComputeGrade(score)
            break
        else:
            print("Enter a valid score ranging between 0-1")
    except:
        print("Invalid input ")


