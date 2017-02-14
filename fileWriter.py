from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
import numpy


class ExcelWriter:

    def write(self, dest_filename, data):

        wb = Workbook()
        ws1 = wb.active
        ws1.title = "Sheet1"

        n_row = data.shape[0]
        n_col = data.shape[1]
        

        for row in range(0,n_row):
            ws1.append(data[row].tolist())

        wb.save(filename = dest_filename)
