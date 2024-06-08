#Read the marks of the student if marks > 80 distintion else if 60 < marks < 80 else if marks < 60 fail else invalid
m = input("Enter ")
marks = []
for i in range(5):
    n = int(input(f"Enter marks of subject {i+1}:"))
    marks.append(n)

i = 0
for mark in marks:
    i = i+1
    if(mark > 80):
        print("Subject", i, ": Distinction")
    elif(mark >= 60 and mark < 80):
        print("Subject", i, ": Passed")
    elif(mark < 60):
        print("Subject", i, ": Failed")
    else:
        print("Invalid marks")