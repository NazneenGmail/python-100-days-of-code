student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    if 90 < student_scores[name] < 101:
        student_grades[name] = "Outstanding"
    elif 80 < student_scores[name] < 91:
        student_grades[name] = "Exceeds Expectations"
    elif 70 < student_scores[name] < 81:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

for name in student_grades:
    print(f"{name} : {student_scores[name]} : {student_grades[name]}")