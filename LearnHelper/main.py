import tkinter as tk
from random import random
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

import openpyxl
from openpyxl_image_loader import SheetImageLoader
import xlrd
from xlrd.sheet import Sheet
from openpyxl import load_workbook
import pandas as pd
import base64
from io import BytesIO

import openpyxl
import pandas as pd

from openpyxl_image_loader import SheetImageLoader
import os

from PIL import Image, ImageTk


def load_sheet_from_excel(file_name: str):
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_name
    wb = openpyxl.load_workbook(path)
    sheet = wb.active

    return sheet

def get_questions(sheet: Sheet):
    # Load the questions from the excel sheet
    questions = []
    for row in sheet.iter_rows(values_only=True):
        question = (row[0], row[1], row[4])
        questions.append(question)
    return questions


def load_images_from_folder(folder_path: str):
    # Load only png files from the folder
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            with open(os.path.join(folder_path, filename), 'rb') as f:
                image = f.read()
                images.append(image)
    return images



if __name__ == '__main__':
    # Set up tkinter window
    root = tk.Tk()
    root.title("LearnHelper")
    root.geometry('800x400')

    # Set up style
    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 14))

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

    question2_label = ttk.Label(abcd_frame, text='', font=('TkDefaultFont', 24))
    question2_label.pack(fill=tk.BOTH, expand=True)

    randomPlace = random.randint(0, 3)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()
    var4 = tk.StringVar()








    # Load the images
    images = load_images_from_folder('VizsgaKerdesek_elemei')

    # Load the excel sheet
    sheet = load_sheet_from_excel('VizsgaKerdesek.xlsx')
    questions = get_questions(sheet)


    root.mainloop()





