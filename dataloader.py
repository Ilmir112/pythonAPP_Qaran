import csv
from collections import defaultdict




# Function importing data from CSV file
def data_from_csv(question, firstanswer, secondanswer, thirdanswer, fourthanswer, rightanswer):
    with open("data/Questions.csv", "r", encoding = 'utf-8') as file:
        csv_data = csv.reader(file)
        for row in csv_data:
            # Assigning each row item to a specific category
            number, text,  first, second, third, fourth, right = row
            # Creating Python dictionary with this data
            question.append(text)
            firstanswer.append(first)
            secondanswer.append(second)
            thirdanswer.append(third)
            fourthanswer.append(fourth)
            rightanswer.append(right)
        return question, firstanswer, secondanswer, thirdanswer, fourthanswer, rightanswer





# def get_scores():
#     hiscores_columns = defaultdict(list)
#     with open('data/hiscores.csv', 'r') as data:
#         reader = csv.DictReader(data)
#         for row in reader:
#             # Assigning values from each column to a list
#             for (column, value) in row.items():
#                 hiscores_columns[column].append(value)
#     return hiscores_columns