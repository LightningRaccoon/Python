import tkinter as tk
from tkinter import ttk

class ABCDTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ABCD Test")

        # Initialize variables to store answers
        self.orientation_answer = tk.StringVar()
        self.memory_answer = tk.StringVar()
        self.attention_answer = tk.StringVar()
        self.language_answer = tk.StringVar()

        # Question frames
        self.create_orientation_frame()
        self.create_memory_frame()
        self.create_attention_frame()
        self.create_language_frame()

        # Submit button
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_answers)
        submit_button.pack(pady=20)

    def create_orientation_frame(self):
        orientation_frame = ttk.Frame(self.root, padding=(20, 10))
        orientation_frame.pack(fill=tk.BOTH)

        orientation_label = ttk.Label(orientation_frame, text="1. What is the current year?")
        orientation_label.pack(side=tk.LEFT, padx=10)

        orientation_entry = ttk.Entry(orientation_frame, textvariable=self.orientation_answer)
        orientation_entry.pack(side=tk.LEFT)

    def create_memory_frame(self):
        memory_frame = ttk.Frame(self.root, padding=(20, 10))
        memory_frame.pack(fill=tk.BOTH)

        memory_label = ttk.Label(memory_frame, text="2. Repeat the phrase: 'Apple, Table, Penny'")
        memory_label.pack(side=tk.LEFT, padx=10)

        memory_entry = ttk.Entry(memory_frame, textvariable=self.memory_answer)
        memory_entry.pack(side=tk.LEFT)

    def create_attention_frame(self):
        attention_frame = ttk.Frame(self.root, padding=(20, 10))
        attention_frame.pack(fill=tk.BOTH)

        attention_label = ttk.Label(attention_frame, text="3. Count backwards from 100 by 3's")
        attention_label.pack(side=tk.LEFT, padx=10)

        attention_entry = ttk.Entry(attention_frame, textvariable=self.attention_answer)
        attention_entry.pack(side=tk.LEFT)

    def create_language_frame(self):
        language_frame = ttk.Frame(self.root, padding=(20, 10))
        language_frame.pack(fill=tk.BOTH)

        language_label = ttk.Label(language_frame, text="4. Name a type of fruit that starts with 'B'")
        language_label.pack(side=tk.LEFT, padx=10)

        language_entry = ttk.Entry(language_frame, textvariable=self.language_answer)
        language_entry.pack(side=tk.LEFT)

    def submit_answers(self):
        orientation_score = self.check_orientation()
        memory_score = self.check_memory()
        attention_score = self.check_attention()
        language_score = self.check_language()

        total_score = orientation_score + memory_score + attention_score + language_score
        result_text = f"Total Score: {total_score} / 4"
        result_label = ttk.Label(self.root, text=result_text, font=("Helvetica", 14, "bold"))
        result_label.pack(pady=20)

    def check_orientation(self):
        expected_year = "2024"  # Change this to the current year
        user_answer = self.orientation_answer.get()
        return 1 if user_answer == expected_year else 0

    def check_memory(self):
        expected_phrase = "Apple, Table, Penny"
        user_answer = self.memory_answer.get()
        return 1 if user_answer.lower() == expected_phrase.lower() else 0

    def check_attention(self):
        expected_countdown = "91, 88, 85, 82, 79, 76, 73, 70, 67, 64, 61, 58, 55, 52, 49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1"
        user_answer = self.attention_answer.get()
        return 1 if user_answer == expected_countdown else 0

    def check_language(self):
        expected_fruit = "Banana"
        user_answer = self.language_answer.get()
        return 1 if user_answer.lower() == expected_fruit.lower() else 0

def main():
    root = tk.Tk()
    app = ABCDTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
