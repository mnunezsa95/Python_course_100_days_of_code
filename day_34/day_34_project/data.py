import requests


BASE_URL = "https://opentdb.com/api.php"
parameters = {"amount": 10, "type": "boolean"}
get_questions = requests.get(url=BASE_URL, params=parameters)
get_questions.raise_for_status()

question_data = get_questions.json()["results"]
