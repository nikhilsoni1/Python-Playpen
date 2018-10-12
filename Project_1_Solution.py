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

data = _GENERATOR.CASES #   This line of code generates the data for the problem. Furhter, you may be asked to reset
                        #   reset the data. At that point just copy and paste this line.


