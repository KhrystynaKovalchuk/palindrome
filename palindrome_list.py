"""
Palindrome class realization.
"""

from arraystack import ArrayStack

class Palindrome:
    """
    Class for serching for palindromes.
    """
    def read_file(self, file):
        """
        Reads file and writes data to the list.
        """
        result = []
        file_open = open(file, "r", encoding="utf-8")
        for line in file_open.readlines():
            if " +cs=" in line:
                result.append(line[line.index("=")+1:line.index("\n")])
            elif " " in line:
                result.append(line[:line.index(" ")])
            elif "\n" in line:
                result.append(line[:line.index("\n")])
            else:
                result.append(line)
        result_new = list(dict.fromkeys(result))
        return result_new

    def find_palindromes(self, file1, file2):
        """
        Search for palindromes and writes them into the file.
        """
        result = []
        pros = []
        strings = self.read_file(file1)
        stack = ArrayStack()
        for word in strings:
            if len(word) == 1:
                result.append(word)
            else:
                for i in range(len(word)):
                    stack.push(word[i])
                while not stack.isEmpty():
                    pros.append(stack.pop())
                if pros == list(word):
                    result.append(word)
                pros.clear()
        self.write_to_file(file2, result)
        return result

    def write_to_file(self, file, words):
        """
        Writes data to file.
        """
        file_open = open(file, "w", encoding="utf-8")
        for word in words[:-1]:
            file_open.write(word+"\n")
        file_open.write(words[-1])
        file_open.close()



a = Palindrome()
# print(a.read_file("words.txt"))
# print(a.read_file("base (1).lst"))
print(a.find_palindromes("check.txt", "checking.txt"))
# print(a.find_palindromes("base (1).lst", "palindrome_uk.txt"))