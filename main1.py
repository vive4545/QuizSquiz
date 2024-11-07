from question_models import Question
from data import question_data
from quizbrain import QuizBrain

emt = []
for ques in question_data:
    txt = ques["question"]
    ans = ques["correct_answer"]
    new = Question(q_text = txt, q_answer= ans)
    emt.append(new)

quiz = QuizBrain(emt)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz ")
print(f"Your Final Score was : 10/{len(emt)}")