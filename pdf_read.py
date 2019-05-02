import PyPDF2 as pdf
import re
import os
import pandas as pd
import itertools as IT
import tempfile


def unique(path, sep=''):
    def name_sequence():
        count = IT.count()
        yield ''
        while True:
            yield '{s}{n:d}'.format(s=sep, n=next(count))
    orig = tempfile._name_sequence
    with tempfile._once_lock:
        tempfile._name_sequence = name_sequence()
        path = os.path.normpath(path)
        dirname, basename = os.path.split(path)
        filename, ext = os.path.splitext(basename)
        fd, filename = tempfile.mkstemp(dir=dirname, prefix=filename, suffix=ext)
        tempfile._name_sequence = orig
    return filename


path = r"C:/Users/sonin/PycharmProjects/Python_Playpen/input/stuff"
pdf_paths = [os.path.normpath(os.path.join(path, i)) for i in os.listdir(path)]
print(pdf_paths)
file = open(pdf_paths[0], "rb")
pdf_file = pdf.PdfFileReader(file)
pages = pdf_file.pages

print(pages[0].extractText())
file.close()