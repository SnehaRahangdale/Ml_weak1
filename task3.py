# Task 3
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

def search_name(roll_no):
    return student_dict.get(roll_no, "Student not found")

print(search_name(101))
print(search_name(105))