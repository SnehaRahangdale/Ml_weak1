# Task 3: Grading System
marks = int(input("Enter marks (0-100): "))

if 90 <= marks <= 100:
    grade = 'A'
elif 75 <= marks < 90:
    grade = 'B'
elif 60 <= marks < 75:
    grade = 'C'
elif 40 <= marks < 60:
    grade = 'D'
elif 0 <= marks < 40:
    grade = 'Fail'
else:
    grade = 'Invalid marks'

print(f"Your grade is: {grade}")
