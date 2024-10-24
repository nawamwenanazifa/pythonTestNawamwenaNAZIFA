# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

#SOLUTION
def calculate_grade(score):
 if 90 <= score <= 100:
    return "A"
 elif 80 <= score <= 89:
    return "B"
 elif 70 <= score <= 79:
    return "C"
 elif 60 <= score <= 69:
    return "D"
 elif 50 <= score <= 59:
    return "E"
 elif 40   <= score <= 49: 

    return "F"

def grade_students():
    num_students = int(input("Enter  the number of students: "))
    for i in range(num_students):
        score = int(input(f"Enter the score for students {i+1}: "))
        grade = calculate_grade(score)
        print(f"Student {i+1}'s grade: {grade}")
grade_students()