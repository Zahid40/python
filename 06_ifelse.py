subject = input("Enter your subject code : ")
marks = int(input("Enter your marks: "))

passing_marks = 0
if subject[0] == "M" or subject[0] == "m":
    passing_marks = 40
elif subject[0] == "B" or subject[0] == "b":
    passing_marks = 36
else:
    print(
        "Invalid subject code, please enter a valid code starting with 'M' or 'B'"
    ), exit(0)

if marks > passing_marks:
    print("Pass ho gaya bsdk")
elif marks == passing_marks:
    print("Laagte Lagte rahe gaye")
else:
    print("Dubara padh bsdk "), exit(0)
