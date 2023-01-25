def add_score(subject_score, student, subject, score):
    if student in subject_score:
        subject_score[student][subject] = score
    else:
        subject_score[student] = {subject : score}
    return subject_score

def calc_average_score(subject_score):
    return_dict = {}
    print(subject_score) 
    for student in subject_score:
        sum = 0
        scores = 0
        print(len(subject_score[student]))
        for subject in subject_score[student]:
            sum += 1
            scores += subject_score[student][subject]
        return_dict[student] = '{:.2f}'.format(scores / sum)
    return return_dict


dict = {"65010001" : {"py" : 50},"65010049" : {"Test1" : 40}}

dict = add_score(dict,"65010049","Test2",10)
dict = add_score(dict,"65010049","Test3",20)

print(calc_average_score(dict))