student_scores = [77, 73, 99, 87, 88, 97, 98, 96, 55, 66, 77, 88, 92, 93, 100, 54, 56, 67, 89, 65, 64, 63, 62, 61, 91,
                  92, 93, 94, 95]

resultFunctionSum = sum(student_scores)
total = 0
for score in student_scores:
    total += score

if total == resultFunctionSum:
    print("Sum using For loop is correct: {:d}".format(total))
else:
    print("Please check logic for sum calculation")

max_score = max(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

if max_score == highest_score:
    print("Highest_score using For loop is correct: {:d}".format(highest_score))
else:
    print("Please check logic for max calculation")