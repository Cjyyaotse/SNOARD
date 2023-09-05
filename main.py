
# Delete the home page after the snake game page has been pop up
from tkinter import *
import random
from tkinter import messagebox
import tkinter as tk

score = 0
direction = 'down'
GAME_HEIGHT = 600
GAME_WIDTH = 600
SPEED = 180
SPACE_SIZE = 20
BODY_PARTS = 1
SNAKE_COLOUR = '#00FF00'
FOOD_COLOUR = '#FF0000'

# A function that defines a canvas page for rules of the game when the rules button is clicked#


def rules():
    rule = Toplevel()
    rule.title('RULES')
    rule.geometry('400x300')
    rule.iconbitmap(r'favicon.ico')
    background = PhotoImage(file='snake_game_bg.png')
    canvas2 = Canvas(rule, bg='white', )
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=background,
                         anchor="nw")

    canvas2.create_text(190, 100, font='gameplay 10 bold', text=
                'WELCOME TO THE CWC SNAKE GAME.\n\nHERE ARE THE RULES OF SNAKE\n\nGame begins with a'
                ' running snake.\nYou need to eat fruits to grow.\nIf any part of the snake body touches\n'
                ' the boundaries you are dead.\nIf two parts on the snake body touch\n each other you are dead\n\n'
                'After a collision, you have  chance to answer\n a math question in 10 seconds to increase your score by 5\n.'
                'HAVE FUN!!')


# A function that defines a canvas page for controls of the game when the rules button is clicked#

def controls():
    control = Toplevel()
    control.title('CONTROLS')
    # Changes icon to an imported image#
    control.iconbitmap(r'favicon.ico')
    control.config(bg="blue")
    control.geometry('550x300')
    canvas2 = Canvas(control, bg='white')
    canvas2.pack(fill="both", expand=True)
    canvas2.create_text(260, 100, font='gameplay 10 bold', text=
                'WELCOME TO THE CWC SNAKE GAME.\n\n'
                'HERE ARE THE CONTROLS OF SNAKE\n\nNAVIGATION KEYS ON KEYBOARD ARE'
                '\n USED TO MOVE THE SNAKE IN ALL DIRECTIONS RESPECTIVELY.\nPRESS LEFT ALT ON KEYBOARD TO PAUSE AND UNPAUSE\n'
                'AFTER COLLISION, USE THE NUMERIC KEYS TO ENTER ANSWER TO QUESTION\n'
                ' HAVE FUN!!')


# A levels-button intended to be added to this game later#


def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_WIDTH:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True


def change_direction(new_direction):
    global direction
    if direction == "left":
        # if direction != "right":
        direction = new_direction
    elif direction == "right":
        # if direction != "left":
        direction = new_direction
    elif direction == "up":
        # if direction != "down":
        direction = new_direction
    elif direction == "down":
        # if direction != "up":
        direction = new_direction


def start_game():
    score = 0
    window = Toplevel()
    window.title("2D SNAKE GAME")
    window.iconbitmap(r'favicon.ico')
    label = Label(window, font='arial 20 bold', text='<CodewithCollins>').pack(side=BOTTOM)  # footer
    label = Label(window, bg="white", text='score:{}'.format(score), font=('gameplay', 40))
    label.pack()
    paused = False

    canvas = Canvas(window, bg="blue", height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack(fill="both", expand=True)

    def next_turn(snake, food):
        x, y = snake.coordinates[0]
        if direction == 'up':
            y = y - SPACE_SIZE
        elif direction == 'down':
            y = y + SPACE_SIZE
        elif direction == 'left':
            x = x - SPACE_SIZE
        elif direction == 'right':
            x = x + SPACE_SIZE

        snake.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score

            score = score + 1
            label.config(text='score:{}'.format(score))
            canvas.delete("food")
            food = Food()

        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            score_after_snake = score
            canvas.delete(ALL)
            background1 = PhotoImage(file='snake_game_bg.png')
            canvas.create_image(0, 0, image=background1, anchor="nw")
            canvas.create_text(300, 200, font=("gameplay", 40),
                               text="SNAKE DIED", fill="red", tag="game over")

            # The beginning of the math aspect#

            class MathQuiz:

                score_after_snake = score

                def __init__(self, root):
                    score_after_snake = score
                    self.root = root
                    self.root.title("Timed Math Quiz")

                    self.score = score_after_snake
                    self.time_left = 10

                    self.question_label = tk.Label(root, text="")
                    self.question_label.pack(pady=10)

                    self.answer_entry = tk.Entry(root)
                    self.answer_entry.pack(pady=5)

                    self.score_label = tk.Label(root, text=f"Score:{score_after_snake}")
                    self.score_label.pack()

                    self.timer_label = tk.Label(root, text="Time left: 10")
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
                            self.score = int(self.score) + 5
                            self.time_left = 0
                            messagebox.showinfo("Correct")
                            self.root.destroy()
                            window.destroy()
                        else:
                            self.score = self.score
                            messagebox.showinfo("Wrong!" )
                            self.root.destroy()
                            window.destroy()
                    except ValueError:
                        messagebox.showerror("Error", "Please enter a valid number.")
                    return self.score

                def ask_question(self):
                    num1 = random.randint(2, 9)
                    num2 = random.randint(2, 9)
                    num3 = random.randint(5, 9)
                    num4 = random.randint(1, 9)
                    self.answer = num1 * num2 + num3 - num4
                    question_text = f"What is {num1} x {num2} + {num3} - {num4}?"
                    self.question_label.config(text=question_text)
                    self.answer_entry.delete(0, tk.END)
                    self.answer_entry.focus_set()

                def update_timer(self):
                    if self.time_left > 0:
                        self.time_left -= 1
                        self.timer_label.config(text=f"Time left: {self.time_left}")
                        self.root.after(1000, self.update_timer)
                    else:
                        self.start_button.config(state=tk.NORMAL)
                        messagebox.showinfo("Time's Up!", f"Your final score: {self.score}")
                        window.destroy()

            root = tk.Tk()
            MathQuiz(root)
            root.mainloop()

        else:
            if score < 3:
                window.after(SPEED, next_turn, snake, food)
            elif score < 6:
                window.after(160, next_turn, snake, food)
            elif score < 9:
                window.after(140, next_turn, snake, food)
            elif score < 12:
                window.after(120, next_turn, snake, food)
            elif score < 16:
                window.after(100, next_turn, snake, food)
            elif score < 20:
                window.after(80, next_turn, snake, food)
            elif score < 25:
                window.after(60, next_turn, snake, food)
            else:
                window.after(40, next_turn, snake, food)

    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)

    class Food:
        def __init__(self):
            x = (random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE)
            y = (random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE)
            self.coordinates = [x, y]
            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag='food')

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)


# Homepage configurations
home = Tk()
home.title('2D SNAKE')
home.iconbitmap(r'favicon.ico')
home.geometry('300x300')
background = PhotoImage(file='snake_game_bg.png')

# Label_1 = Label(home, fg='blue', bg='white', text = 'HOMEPAGE',font=("gameplay", 10)).pack(side=TOP)
canvas1 = Canvas(home,bg="blue", width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=background, anchor="nw")
startgame_btn = Button(home, text='START GAME', fg='blue', font=('gameplay', 10), command=start_game)
startgame_btn.place(x=100, y=50)

rules_btn = Button(home, text='RULES', fg='blue', font=('gameplay', 10), command=rules)
rules_btn.place(x=100, y=100)

controls_btn = Button(home, text='CONTROLS', fg='blue', font=('gameplay', 10), command=controls)
controls_btn.place(x=100, y=150)

'''levels_btn = Button(home,text='DIFFICULTY',fg='blue',font=('gameplay',10),command=level)
levels_btn.place(x=100,y=200)'''
home.bind("<Left>", lambda event: change_direction('left'))
home.bind("<Right>", lambda event: change_direction('right'))
home.bind("<Up>", lambda event: change_direction('up'))
home.bind("<Down>", lambda event: change_direction('down'))


home.mainloop()