import re


def name_proc(x):
    x = x.strip()


file = open(r"C:\Users\sonin\Downloads\Binder10101.txt", "r")
file1 = open(r"C:\Users\sonin\Downloads\Binder10187.txt", "r")
file2 = open(r"C:\Users\sonin\Downloads\Binder10806.txt", "r")
contents = file2.read()
PATT1 = re.compile(r"Student Details\n")
PATT2 = re.compile(r"Student\s(.+)\s")
PATT3 = re.compile(r"Thesis\/dissertation\s?title\s?\s?(.+)")
PATT3_1 = re.compile(r"Thesis\/dissertation (.+)")
PATT4 = re.compile(r"length of confidentiality (.+)")
PATT5 = re.compile(r"Length of delay (.+)")
contents = re.sub(PATT1, "", contents)
student = re.search(PATT2, contents).group(1)
title = re.search(PATT3_1, contents).group(1)
confidentiality = re.search(PATT4, contents.lower())
delay = re.search(PATT5, contents.lower())
print(student)
print(title)
if confidentiality:
    print("Conf: %s" % confidentiality.group(1))
if delay:
    print("Delay: %s" % delay.group(1))
