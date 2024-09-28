print("Exam Grade Calculator!")

Subject = input("What is the subject you want to calculate your grade at? ")

MaxScore = float(input("What is the maximum score for this subject? "))

Score = float(input("What is your score in this subject? "))

Grade = (round(Score / MaxScore, 2)) * 100

if Grade >= 90:
    print("Your score in", Subject, "is", Grade, "%", "which is an A+")
elif 90 > Grade > 79:
    print("Your score in", Subject, "is", Grade, "%", "which is an A-")
elif 80 > Grade > 69:
    print("Your score in", Subject, "is", Grade, "%", "which is a B")
elif 70 > Grade > 59:
    print("Your score in", Subject, "is", Grade, "%", "which is a C")
elif 60 > Grade > 49:
    print("Your score in", Subject, "is", Grade, "%", "which is a D")
else:
    print("Your score in", Subject, "is", Grade, "%", "which is a U")