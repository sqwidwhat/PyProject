student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = []

for values in student_scores:
    if student_scores[values] > 90 and student_scores[values] <= 100:
        student_scores[values] = "Luar Biasa"
    elif student_scores[values] > 81 and student_scores[values] <= 90:
        student_scores[values] = "Melebihi Harapan"
    elif student_scores[values] > 71 and student_scores[values] <= 80:
        student_scores[values] = "Dapat Diterima"
    else:
        student_scores[values] = "Gagal"
    student_grades = student_scores

for key in student_grades:
    print(key)
    print(student_grades[key])