class QuizBrain:
    def __init__(self, q_list):
        self.question_no= 0
        self.question_list= q_list
        self.score = 0

    def end_or_not(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_q= self.question_list[self.question_no]
        self.question_no += 1
        ans= input(f"Q.{self.question_no}: {current_q.text} (True/False): ").lower()
        self.check_answer(ans, current_q.ans)

    def check_answer(self,ans, correct_ans):
        if ans == correct_ans.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("You got it wrong!")

        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_no}\n")