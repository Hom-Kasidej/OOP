def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    scores = 0
    sum = 0
    for subject in subject_score:
        sum += 1
        scores += subject_score[subject]
    return "{:.2f}".format(scores / sum)


dict = {'python' : 50}

add_score(dict,"Test",10)

print(dict)

print(calc_average_score(dict))