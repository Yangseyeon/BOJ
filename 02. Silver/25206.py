import sys
grade_list = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
all_grade = 0
all_credit = 0

for _ in range(20):
    _, credit, grade= sys.stdin.readline().strip().split()
    if grade != "P":
        all_grade += float(credit) * grade_list[grade]
        all_credit += float(credit)

print("%.6f" %(all_grade / all_credit))
