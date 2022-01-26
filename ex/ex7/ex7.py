#! /usr/bin/python3

def open_file_read(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Cannot open', filename)
        return False
    else:
        return file

def quiz_dictionary_create(filename):
    file = open_file_read(filename)
    if file:
        quizzes = {}
        for line in file:
            fields = line.split()
            first_name = fields[0]
            last_name = fields[1]
            sort_name = first_name + ", " + last_name
            fields.remove(first_name)
            fields.remove(last_name)
            quizzes[sort_name] = fields
        return quizzes

def average_quizzes(qz_dict):
    for sort_name in sorted(qz_dict):
        total = 0
        scores_list = qz_dict[sort_name]
        for score in scores_list:
            total += int(score)
        quiz_count = len(scores_list)
        average = round(total/quiz_count)
        print(sort_name, average)

quizzes = quiz_dictionary_create('xxx')
quizzes = quiz_dictionary_create('student_scores.txt')
average_quizzes(quizzes)