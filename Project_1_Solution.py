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



