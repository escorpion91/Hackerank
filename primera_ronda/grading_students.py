def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            residuo = grade % 5

            if residuo >= 3:
                grade += (5 - residuo)

        res.append(grade)
    return res
