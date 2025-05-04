# Task 1
marks = [
    [85, 90, 78],
    [76, 88, 85],
    [90, 92, 89]
]

for i, student_marks in enumerate(marks):
    total = sum(student_marks)
    average = total / len(student_marks)
    print(f"Student {i+1} - Total: {total}, Average: {average:.2f}")