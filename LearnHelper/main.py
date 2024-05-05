import tkinter as tk
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

def load_dataframe(dataframe_file_path: str, dataframe_sheet_name: str) -> pd.DataFrame:
    pxl_doc = openpyxl.load_workbook(dataframe_file_path)
    pxl_sheet = pxl_doc[dataframe_sheet_name]
    pxl_image_loader = SheetImageLoader(pxl_sheet)
    pd_df = pd.read_excel(dataframe_file_path, sheet_name=dataframe_sheet_name)
    for pd_row_idx, pd_row_data in pd_df.iterrows():
        for pd_column_idx, _pd_cell_data in enumerate(pd_row_data):
            # Offset as openpyxl sheets index by one, and also offset the row index by one more to account for the header row
            pxl_cell_coord_str = pxl_sheet.cell(pd_row_idx + 2, pd_column_idx + 1).coordinate
            if pxl_image_loader.image_in(pxl_cell_coord_str):
            # Now that we have a cell that contains an image, we want to convert it to
            # base64, and it make it nice and HTML, so that it loads in a front end
                pxl_pil_img = pxl_image_loader.get(pxl_cell_coord_str)
                with BytesIO() as pxl_pil_buffered:
                    pxl_pil_img.save(pxl_pil_buffered, format="JPG")
                    pxl_pil_img_b64_str = base64.b64encode(pxl_pil_buffered.getvalue())
                    pd_df.iat[pd_row_idx, pd_column_idx] = '<img src="data:image/jpg;base64,' + \
                                                                pxl_pil_img_b64_str.decode('utf-8') + \
                                                                f'" alt="{pxl_cell_coord_str}" />'
    return pd_df



def LoadExcelFile():
    excel_path = "E:\Programozas\Github Repos\Python\LearnHelper\VizsgaKerdesek.xlsx"
    df = pd.read_excel(excel_path, sheet_name='alap')  # Specify sheet name if needed

    # Display the contents of the DataFrame
    print(df)


if __name__ == '__main__':
    # Set up tkinter window
    root = tk.Tk()
    root.title("LearnHelper")
    root.geometry('800x400')

    # Set up style
    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButton', font=('TkDefaultFont', 14))

    LoadExcelFile()
    print(load_dataframe("E:\Programozas\Github Repos\Python\LearnHelper\VizsgaKerdesek.xlsx", "alap"))


