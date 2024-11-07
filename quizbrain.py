class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_no < len(self.question_list)
 

    def next_question(self):
        correct_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q:{self.question_no}={correct_question.text} 'True or False' : \n")
        self.check_answer(user_answer,correct_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong Answer")
        print(f"Wrong! The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_no}")
        print("\n")