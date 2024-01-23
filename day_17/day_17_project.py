# ------------------------------------------------------------------------------------------------ #
#                                             Quiz Game                                            #
# ------------------------------------------------------------------------------------------------ #

from day_17_project_question_model import Question  # Import Question class
from day_17_project_data import question_data  # Import question_data
from day_17_project_quiz_brain import QuizBrain  # Import QuizBrain class

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)  # create object instance
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
