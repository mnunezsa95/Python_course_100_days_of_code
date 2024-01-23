class QuizBrain:
    # QuizBrain gets initalized with 3 attributes (2 are default)
    # When initializing QuizBrain, MUST passed in a question list
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        # the correct_answer can be attained using answer attribute of the question dictionary
        if user_answer == correct_answer.lower():  # compare answers
            print("You got it right!")
            self.score += 1  # increase score if correct
        else:
            print("That's wrong")  # let user know they are wrong

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()

    def next_question(self):
        # Create current_question variable, by accessing the index of the question_list
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # Increase question_number
        # Ask user for answer
        user_answer = input(
            f"Q. {self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Compares the current question number against the total number of questions and returns True or False"""
        length_of_list = len(self.question_list)
        return self.question_number < length_of_list
