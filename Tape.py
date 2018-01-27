"""

In this file we represent the infinite tape which is the state
of a brainf machine


"""


# All classes inherit from Object by default
class Tape:
    """
    Invariant: The pointer is valid.
    """

    def __init__(self):
        self.tape = [0]
        self.pointer = 0

    def getLen(self):
        return len(self.tape)

    def moveRight(self):
        self.pointer += 1
        if self.getLen() == self.pointer:
            self.tape.append(0)

    def moveLeft(self):
        self.pointer -= 1
        if self.pointer < 0:
            raise IndexError("Moving before tape start")

    def increment(self):
        self.tape[self.pointer] += 1

    def decrement(self):
        self.tape[self.pointer] -= 1

    def getVal(self):
        return self.tape[self.pointer];
        

    def setVal(self, val):
        assert(type(val) is int)
        self.tape[self.pointer] = val
        return None;

    


