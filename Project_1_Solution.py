#   Problem Generator, ignore this code block.
import random
import string
random.seed(9)


class Problem:
    def __init__(self):
        self._EXTENSION_LIST = ["txt", "zip", "pdf", "docx", "jpeg", "png", "xlsx", "html"]
        self._RANDOM_CASES = self.cases()
        self._CORNER_CASES = self.corner_cases()
        self.CASES = random.sample(self._RANDOM_CASES + self._CORNER_CASES, random.randint(20, 50))

    def cases(self):
        store = []
        for i in range(random.randint(10, 100)):
            x = random.choice(self._EXTENSION_LIST)
            prefix = "".join(random.sample(string.ascii_lowercase, random.randint(3, 7)))
            store.append("%s_%d.%s" % (prefix, random.randint(1, 10), x))
        return store

    def corner_cases(self):
        store = []
        for i in range(random.randint(10, 100)):
            x = random.choice(self._EXTENSION_LIST)
            store.append("%s_%d.%s" % (x, random.randint(1, 10), x))
        return store


_GENERATOR = Problem()
#   Problem Generator, ignore this code block.

data = _GENERATOR.CASES #   This line of code generates the data for the problem. Further, you may be asked to reset
                        #   reset the data. At that point just copy and paste this line.

#   Problem 1). Find the type of the variable "data" and store it in a variable called "data_type". Print "data_type".
#   Hint: type(<variable name>) returns the type of the variable.

data_type = type(data)
print(data_type)

#   Problem 2). Find the length of the variable "data" and store it in a variable called "data_length".
#               Print "data_length".
#               Hint: len(<variable name>) returns the length of the variable

data_length = len(data)
print(data_length)

#   Problem 3). Print the 10th element of the variable "data".
#   Hint: Use list subset, <list>[x]

print(data[9])

#   Problem 4). Print the 10th index of the variable "data"
#   Hint: Use list subset, <list>[x]

print(data[10])

#   Problem 5). Are the values from the previous two questions the same? Use an if statement to print the answer.

print(data[9] == data[10])
#   Takeaway: A list is indexed from 0 to N-1 in the computer, N being the number of elements in the list. Mth element
#   just means the Mth element from the starting of the list. Mth Element = M-1th Index


#   Concept 1 : if-else conditional statement
#   The following statements read as:
#   1.1. "a == b ": Is a equal to b, returns either True or False
#   1.2. "a != b": Is a not equal to b, returns either True or False
#   1.3. "a in b": Whether a is contained in b
#   if <A True Value is Encountered>:
#       <Do this>
#   else:
#       <Do Something Else>

#   Problem 6). Check whether "_RANDOM_STRING is contained in the list. Print the "Yes" if it is, otherwise print No.
#   Hint: Refer the Concept 1: if-else statement structure and bullet Point 1.3
_RANDOM_STRING = random.choice(data)

if _RANDOM_STRING in data:
    print("Yes")
else:
    print("No")

#   Concept 2 : range(x)
#   The above statement specifies a progression from "0" to "x-1", 1 step at a time.
#   Remember counting from "0" to "x-1" is the same as counting from 1 to x. As in 0, 1, 2, 3 and 1, 2, 3, 4
#   have the same number of elements.

#   Problem 7). Print range(4)
print(range(4))
#   This just specifies a progression from "0" to "3"

#   Concept 3 : for-loop:
#   for i in range(x>):
#       print(i)
#   This statements iterated "i" from "0" to "x-1" and it will print all the values which "i" will take.

#   Problem 8). Using for-loop print numbers from 0 to 3.
#   Hint: Use concept 2 and 3

for i in range(4):
    print(i)

#   Problem 9). Print all the elements contained in the variable "data".
#   Hint: use concept 2 and 3, data_length and <list[i]>

for i in range(data_length):
    print(data[i])

#   Concept 4: List iteration
#   for i in <list>:
#       print(i)
#   "i" iterates over every element of the list because list is iterable (FACT)

#   Problem 10). Print all the elements of the variable "data" using the iteration method.
#   Hint: Use concept 4

print("------") #   Ignore

for i in data:
    print(i)