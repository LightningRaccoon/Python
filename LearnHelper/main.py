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
                img.thumbnail((500, 200))
                image_list.append(ImageTk.PhotoImage(img))
    return image_list

def flip_card():
    return None
    # question_label.config(text=questions[current_question_index][0])
    # image = Image.open(BytesIO(images[current_question_index]))
    # image = image.resize((200, 200))
    # photo = ImageTk.PhotoImage(image)
    # image_label.config(image=photo)
    # image_label.image = photo

def next_card():
    return None
    # global current_question_index
    # current_question_index = (current_question_index + 1) % len(questions)
    # flip_card()


def previous_card():
    return None
    # global current_question_index
    # current_question_index = (current_question_index - 1) % len(questions)
    # flip_card()


def validate_ABCD():
    global all_points
    global achieved_points
    all_points += current_question_points
    if selected_answer.get() == correct_answer_index:
        achieved_points += current_question_points
        messagebox.showinfo("Validation", "Correct answer! You have " + str(achieved_points) + " points.")
    else:
        messagebox.showinfo("Validation", "Incorrect answer! You have " + str(achieved_points) + " points.")
    points_label.config(text='Points: ' + str(achieved_points) + '/' + str(all_points))


def next_ABCD():
    global current_question_index, current_question_points, current_question
    current_question_index += 1
    if current_question_index < len(images):
        clear_abcd_display()
        stringTuple = (str(questions[current_question_index][0]), questions[current_question_index][1])
        current_question = (stringTuple[0] + '. ' + stringTuple[1])
        current_question_points = questions[current_question_index][2]
        frame_question.set(current_question)
        place_answers()


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
        var1 = images[current_question_index]
        var2 = images[get_random_answer_index(current_question_index)]
        var3 = images[get_random_answer_index(current_question_index)]
        var4 = images[get_random_answer_index(current_question_index)]
    elif correct_answer_index == 1:
        var1 = images[get_random_answer_index(current_question_index)]
        var2 = images[current_question_index]
        var3 = images[get_random_answer_index(current_question_index)]
        var4 = images[get_random_answer_index(current_question_index)]
    elif correct_answer_index == 2:
        var1 = images[get_random_answer_index(current_question_index)]
        var2 = images[get_random_answer_index(current_question_index)]
        var3 = images[current_question_index]
        var4 = images[get_random_answer_index(current_question_index)]
    else:
        var1 = images[get_random_answer_index(current_question_index)]
        var2 = images[get_random_answer_index(current_question_index)]
        var3 = images[get_random_answer_index(current_question_index)]
        var4 = images[current_question_index]

    option1.config(image=var1)
    option2.config(image=var2)
    option3.config(image=var3)
    option4.config(image=var4)


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
    images = load_images_from_folder('VizsgaKerdesek_elemei')

    # Load the Excel sheet
    sheet = load_sheet_from_excel('VizsgaKerdesek.xlsx')
    questions = get_questions(sheet)


    # Set up the notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Main page frame
    main_frame = ttk.Frame(notebook)
    notebook.add(main_frame, text='Main')

    # Flip frame
    flip_frame = ttk.Frame(notebook)
    notebook.add(flip_frame, text='Flip')

    question_label = ttk.Label(flip_frame, text='', font=('TkDefaultFont', 24))
    question_label.pack(fill=tk.BOTH, expand=True)

    image_label = ttk.Label(flip_frame)
    image_label.pack(fill=tk.BOTH, expand=True)

    ttk.Button(flip_frame, text='Flip', command=flip_card).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(flip_frame, text='Next', command=next_card).pack(side=tk.RIGHT, padx=10, pady=10)
    ttk.Button(flip_frame, text='Previous', command=previous_card).pack(side=tk.LEFT, padx=10, pady=10)

    # A-B-C-D frame
    abcd_frame = ttk.Frame(notebook)
    notebook.add(abcd_frame, text='A-B-C-D')

    current_question_points = 0
    current_question = ''
    selected_answer = tk.IntVar()
    frame_question = tk.StringVar(abcd_frame, value=current_question)

    var1 = tk.PhotoImage()
    var2 = tk.PhotoImage()
    var3 = tk.PhotoImage()
    var4 = tk.PhotoImage()

    question2_label = ttk.Label(abcd_frame, textvariable=frame_question, font=('TkDefaultFont', 12))
    question2_label.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)

    correct_answer_index = tk.IntVar()

    option1 = ttk.Radiobutton(abcd_frame, image=var1,  value=0, variable=selected_answer)
    option1.pack(anchor=tk.W, padx=10, pady=10)

    option2 = ttk.Radiobutton(abcd_frame, image=var2, value=1, variable=selected_answer)
    option2.pack(anchor=tk.W, padx=10, pady=10)

    option3 = ttk.Radiobutton(abcd_frame, image=var3, value=2, variable=selected_answer)
    option3.pack(anchor=tk.W, padx=10, pady=10)

    option4 = ttk.Radiobutton(abcd_frame, image=var4, value=3, variable=selected_answer)
    option4.pack(anchor=tk.W, padx=10, pady=10)

    #Set up the question
    next_ABCD()

    button_frame = ttk.Frame(abcd_frame)
    button_frame.pack(padx=10, pady=10)

    # Button to validate the answer
    nextButton = ttk.Button(button_frame, text='Next', command=next_ABCD)
    nextButton.pack(side=tk.LEFT, padx=10, pady=10)

    validateButton = ttk.Button(button_frame, text='Validate', command=validate_ABCD)
    validateButton.pack(side=tk.RIGHT, padx=10, pady=10)

    # Label for the points
    points_label = ttk.Label(button_frame, text='Points: ' + str(achieved_points) + '/' + str(all_points))
    points_label.pack(side=tk.RIGHT, padx=10, pady=20)

    root.mainloop()
