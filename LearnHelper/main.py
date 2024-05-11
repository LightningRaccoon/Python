import tkinter as tk
import random
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
from xlrd.sheet import Sheet
import openpyxl
import os
from PIL import Image, ImageTk

# Global variables
current_question_index = 0  # Start from the one because the first row is the header
achieved_points = 0
all_points = 0
validated = False
flipped = False


def load_sheet_from_excel(file_name: str):
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_name
    wb = openpyxl.load_workbook(path)
    sheet = wb.active

    return sheet


def get_questions(sheet: Sheet):
    # Load the questions from the Excel sheet
    questions = []
    for row in sheet.iter_rows(values_only=True):
        question = (row[0], row[1], row[4])
        questions.append(question)
    return questions


def load_images_from_folder(folder_path: str):
    # Load only png files from the folder
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            path = os.path.join(folder_path, filename)
            with Image.open(path) as img:
                img.thumbnail((400, 200))
                image_list.append(ImageTk.PhotoImage(img))
    return image_list


def start_program():
    global current_question_index
    current_question_index = 0

def start_card():
    next_card()


def flip_card():
    global flipped
    stringTuple = (str(questions[current_question_index][0]), questions[current_question_index][1],
                   str(questions[current_question_index][2]))
    current_question = (stringTuple[0] + '. ' + stringTuple[1])
    if not flipped:
        flip_label.config(image=images[current_question_index-1], text='')
        flipped = True
    else:
        flip_label.config(text=current_question, image='')
        flipped = False

def next_card():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(questions):
        stringTuple = (str(questions[current_question_index][0]), questions[current_question_index][1],
                       str(questions[current_question_index][2]))
        current_question = (stringTuple[0] + '. ' + stringTuple[1])
        flip_label.config(text=current_question, image='')



def previous_card():
    global current_question_index
    if current_question_index > 1:
        current_question_index -= 1
        stringTuple = (str(questions[current_question_index][0]), questions[current_question_index][1],
                       str(questions[current_question_index][2]))
        current_question = (stringTuple[0] + '. ' + stringTuple[1])
        flip_label.config(text=current_question, image='')


def start_ABCD():
    global current_question_index, current_question_points, current_question, achieved_points
    global validated
    global all_points
    global validation_message
    current_question_index = 0
    current_question_points = 0
    current_question = ''
    achieved_points = 0
    validated = False
    all_points = 0
    validation_message.set('')
    next_ABCD()

def validate_ABCD():
    global all_points
    global achieved_points
    global validated
    global validation_message
    if selected_answer.get() != -1:
        if not validated:
            validated = True
            if selected_answer.get() == correct_answer_index:
                achieved_points += current_question_points
                #messagebox.showinfo("Validation", "Correct answer! You have " + str(achieved_points) + " points.")
                validation_message.set("Correct answer! You got " + str(current_question_points) + " points.")
            else:
                #messagebox.showinfo("Validation", "Incorrect answer! You have " + str(achieved_points) + " points.")
                validation_message.set("Incorrect answer!")
            points_label.config(text='Points: ' + str(achieved_points) + '/' + str(all_points))
    else:
        #messagebox.showinfo("Validation", "You don't select any answer!")
        validation_message.set("You didn't select any answer!")


def next_ABCD():
    global current_question_index, current_question_points, current_question
    global validated
    global all_points
    global validation_message
    current_question_index += 1
    if current_question_index < len(images):
        clear_abcd_display()
        stringTuple = (str(questions[current_question_index][0]), questions[current_question_index][1], str(questions[current_question_index][2]))
        current_question = (stringTuple[0] + '. ' + stringTuple[1] + " (" + stringTuple[2] + " points)")
        current_question_points = questions[current_question_index][2]
        all_points += current_question_points
        frame_question.set(current_question)
        place_answers()
        validated = False
        validation_message.set('')


def get_random_answer_index(current_index):
    random_index = current_index
    while random_index == current_index:
        random_index = random.randint(0, len(images) - 1)
    return random_index


def get_random_place():
    return random.randint(0, 3)


def clear_abcd_display():
    global var1, var2, var3, var4
    frame_question.set('')
    var1 = tk.PhotoImage()
    selected_answer.set(0)


def place_answers():
    global var1, var2, var3, var4
    global selected_answer
    global correct_answer_index
    global option1, option2, option3, option4
    correct_answer_index = get_random_place()
    selected_answer.set(-1)
    if correct_answer_index == 0:
        var1 = images[current_question_index-1]
        var2 = images[get_random_answer_index(current_question_index)]
        var3 = images[get_random_answer_index(current_question_index)]
        var4 = images[get_random_answer_index(current_question_index)]
    elif correct_answer_index == 1:
        var1 = images[get_random_answer_index(current_question_index)]
        var2 = images[current_question_index-1]
        var3 = images[get_random_answer_index(current_question_index)]
        var4 = images[get_random_answer_index(current_question_index)]
    elif correct_answer_index == 2:
        var1 = images[get_random_answer_index(current_question_index)]
        var2 = images[get_random_answer_index(current_question_index)]
        var3 = images[current_question_index-1]
        var4 = images[get_random_answer_index(current_question_index)]
    else:
        var1 = images[get_random_answer_index(current_question_index)]
        var2 = images[get_random_answer_index(current_question_index)]
        var3 = images[get_random_answer_index(current_question_index)]
        var4 = images[current_question_index-1]

    option1.config(image=var1)
    option2.config(image=var2)
    option3.config(image=var3)
    option4.config(image=var4)


def reset_points():
    global achieved_points
    global all_points
    global current_question_index
    achieved_points = 0
    all_points = 0
    current_question_index = 0
    points_label.config(text='Points: ' + str(achieved_points) + '/' + str(all_points))


def tab_changed(event):
    if notebook.index('current') == 0:
        start_card()
    else:
        start_ABCD()


if __name__ == '__main__':
    # Set up tkinter window
    root = tk.Tk()
    root.title("LearnHelper")
    root.geometry('800x800')

    # Set up style
    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 14))

    # Load the images
    images = load_images_from_folder('Source')

    # Load the Excel sheet
    sheet = load_sheet_from_excel('VizsgaKerdesek.xlsx')
    questions = get_questions(sheet)


    # Set up the notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # # Main page frame
    # main_frame = ttk.Frame(notebook)
    # notebook.add(main_frame, text='Main')
    start_program()

    # Flip frame
    flip_frame = ttk.Frame(notebook)
    notebook.add(flip_frame, text='Flip')


    # Question label
    flip_label = ttk.Label(flip_frame, image='', text='', font=('TkDefaultFont', 16))
    flip_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    ttk.Button(flip_frame, text='Flip', command=flip_card).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(flip_frame, text='Next', command=next_card).pack(side=tk.RIGHT, padx=10, pady=10)
    ttk.Button(flip_frame, text='Previous', command=previous_card).pack(side=tk.LEFT, padx=10, pady=10)

    # A-B-C-D frame
    abcd_frame = ttk.Frame(notebook, borderwidth=1, relief="solid")
    notebook.add(abcd_frame, text='A-B-C-D')

    current_question_points = 0
    current_question = ''
    selected_answer = tk.IntVar()
    frame_question = tk.StringVar(abcd_frame, value=current_question)
    validation_message = tk.StringVar(abcd_frame, value='Monkey')

    var1 = tk.PhotoImage()
    var2 = tk.PhotoImage()
    var3 = tk.PhotoImage()
    var4 = tk.PhotoImage()

    question2_label = ttk.Label(abcd_frame, textvariable=frame_question, font=('TkDefaultFont', 12), borderwidth=1, relief="solid")
    question2_label.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)

    correct_answer_index = tk.IntVar()

    option_frame = tk.Frame(abcd_frame, borderwidth=1, relief="solid", height=800)
    option_frame.pack(padx=5, pady=0, fill=tk.BOTH)

    option1 = ttk.Radiobutton(option_frame, image=var1,  value=0, variable=selected_answer)
    option1.pack(anchor=tk.W, padx=10, pady=10)

    option2 = ttk.Radiobutton(option_frame, image=var2, value=1, variable=selected_answer)
    option2.pack(anchor=tk.W, padx=10, pady=10)

    option3 = ttk.Radiobutton(option_frame, image=var3, value=2, variable=selected_answer)
    option3.pack(anchor=tk.W, padx=10, pady=10)

    option4 = ttk.Radiobutton(option_frame, image=var4, value=3, variable=selected_answer)
    option4.pack(anchor=tk.W, padx=10, pady=10)

    validation_frame = ttk.Frame(abcd_frame, borderwidth=1, relief="solid")
    validation_frame.pack(padx=5, pady=0, fill=tk.BOTH)

    validation_label = ttk.Label(validation_frame, textvariable=validation_message, borderwidth=1, relief="solid")
    validation_label.pack(side=tk.LEFT, padx=5, pady=10)

    # button_frame = ttk.Frame(abcd_frame)
    # button_frame.pack(padx=1, pady=10)

    # Button to validate the answer
    ttk.Button(abcd_frame, text='Next', command=next_ABCD).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(abcd_frame, text='Validate', command=validate_ABCD).pack(side=tk.RIGHT, padx=10, pady=10)

    # Label for the points
    points_label = ttk.Label(abcd_frame, text='Points: ' + str(achieved_points) + '/' + str(all_points), borderwidth=1, relief="solid")
    points_label.pack(side=tk.RIGHT, padx=10, pady=20)

    root.bind("<<NotebookTabChanged>>", tab_changed)
    root.mainloop()
