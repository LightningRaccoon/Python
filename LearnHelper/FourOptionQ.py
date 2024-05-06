import tkinter as tk
from tkinter import ttk, messagebox

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_answer": "Leonardo da Vinci"
    }
]

class FourOptionQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Four Option Quiz")

        self.question_index = 0
        self.score = 0

        # Initialize option_vars as a list to store radio button variables
        self.option_vars = []

        self.create_question_frame()
        self.create_options_frame()

    def create_question_frame(self):
        self.question_frame = ttk.Frame(self.root, padding=20)
        self.question_frame.pack()

        self.question_label = ttk.Label(self.question_frame, text="")
        self.question_label.pack()

        self.next_button = ttk.Button(self.question_frame, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.display_question()

    def create_options_frame(self):
        self.options_frame = ttk.Frame(self.root, padding=20)
        self.options_frame.pack()

        # Create radio buttons for options and store their variables in option_vars
        for i in range(4):
            var = tk.StringVar()
            self.option_vars.append(var)
            option_button = ttk.Radiobutton(self.options_frame, text="", variable=var, value="", command=self.save_answer)
            option_button.pack(anchor=tk.W)

    def display_question(self):
        if self.question_index < len(questions):
            question_data = questions[self.question_index]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.option_vars[i].set(question_data["options"][i])

    def save_answer(self):
        # No need to implement save_answer for now
        pass

    def next_question(self):
        self.question_index += 1
        self.clear_options()

        if self.question_index < len(questions):
            self.display_question()
        else:
            self.show_result()

    def clear_options(self):
        for var in self.option_vars:
            var.set("")

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(questions)}")

def main():
    root = tk.Tk()
    app = FourOptionQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
