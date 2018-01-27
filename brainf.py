"""o
This is the core brainf interpreter, but it needs some improvement.

1. Add while loop support: []
2. Use an abstract syntax tree to parse input






"""

from Tape import Tape


class Brainf:
    def __init__(self):
        self.tape = Tape()

        self.functions = {
            "+":self.tape.increment,
            "-":self.tape.decrement,
            ">":self.tape.moveRight,
            "<":self.tape.moveLeft,
            ".":self.printVal,
            ",":self.getInput
        }


    def printVal(self):
        print(self.tape.getVal())

    def getInput(self):
        i = input("input: ")
        self.tape.setVal(int(i));
        
    def process(self, characters):
        for char in characters:
            self.functions[char]()

    def repl(self):
        while True:
            self.process(input(">>> "))
        
if __name__ == "__main__":
    b = Brainf()
    b.repl()
    

        



