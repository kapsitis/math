import requests

def main(): 
    response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=0&single=true&output=csv')
    assert response.status_code == 200, 'Wrong status code'
    print(response.content)


if __name__ == '__main__':
    main()


