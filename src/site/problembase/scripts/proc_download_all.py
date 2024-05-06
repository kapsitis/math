import requests

old_topics = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=0&single=true&output=csv'
new_topics = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv'
question_types = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=56933932&single=true&output=csv'
strategies = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=491213146&single=true&output=csv'
problems_ru = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1619668403&single=true&output=csv'

def get_spreadsheets():
    response = requests.get(old_topics)
    open("resources/old_topics.csv", "wb").write(response.content)
    response = requests.get(new_topics)
    open("resources/new_topics.csv", "wb").write(response.content)
    response = requests.get(question_types)
    open("resources/question_types.csv", "wb").write(response.content)
    response = requests.get(strategies)
    open("resources/strategies.csv", "wb").write(response.content)
    response = requests.get(problems_ru)
    open("resources/problems_ru.csv", "wb").write(response.content)


if __name__ == '__main__': 
    get_spreadsheets()
