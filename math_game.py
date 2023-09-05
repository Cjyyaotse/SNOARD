import tkinter as tk
import random
from tkinter import messagebox
def math_section():
    class MathQuiz:
        score_after_snake = score

        def __init__(self, root):
            self.root = root
            self.root.title("Timed Math Quiz")

            self.score = score_after_snake
            self.time_left = 10

            self.question_label = tk.Label(root, text="")
            self.question_label.pack(pady=10)

            self.answer_entry = tk.Entry(root)
            self.answer_entry.pack(pady=5)

            self.score_label = tk.Label(root, text=(f"Score:{score_after_snake}"))
            self.score_label.pack()

            self.timer_label = tk.Label(root, text="Time left: 5")
            self.timer_label.pack()

            self.start_button = tk.Button(root, text="Start", command=self.start_quiz)
            self.start_button.pack(pady=10)

            self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
            self.submit_button.pack()

        def start_quiz(self):
            self.score = score_after_snake
            self.time_left = 10
            self.score_label.config(text=f"Score: {self.score_after_snake}")
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.start_button.config(state=tk.DISABLED)
            self.ask_question()
            self.update_timer()

        def submit_answer(self):
            self.score = score_after_snake
            user_answer = self.answer_entry.get()

            try:
                user_answer = int(user_answer)
                if user_answer == self.answer:
                    messagebox.showinfo("Result", "Correct!")
                    self.score = int(self.score) + 5
                else:
                    messagebox.showinfo("Result", "Incorrect. Try again.")
                    self.score = self.score
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")
            return self.score

        def ask_question(self):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            self.answer = num1 + num2
            question_text = f"What is {num1} + {num2}?"
            self.question_label.config(text=question_text)
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.focus_set()

        '''def check_answer(self):
            user_answer = self.answer_entry.get()
            if user_answer.isdigit() and int(user_answer) == self.answer:
                self.score += 1
                self.score_label.config(text=f"Score: {score}")
            self.ask_question()
          '''

        def update_timer(self):
            if self.time_left > 0:
                self.time_left -= 1
                self.timer_label.config(text=f"Time left: {self.time_left}")
                self.root.after(1000, self.update_timer)
            else:
                self.start_button.config(state=tk.NORMAL)
                messagebox.showinfo("Time's Up!", f"Your final score: {self.score}")


    root = tk.Tk()
    quiz = MathQuiz(root)
    root.mainloop()