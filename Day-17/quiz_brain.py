import random
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if len(self.question_list) == 0:
            print("You've completed the quiz!")
            print(f"Your final score: {self.score}/{self.question_number}")
            return False
        else:
            return True

    def next_question(self):
        current_question = random.choice(self.question_list)
        self.question_list.remove(current_question)
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False)? ").lower()
        correct_answer = current_question.answer.lower()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, u_answer, corr_answer):
        if u_answer == corr_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")
