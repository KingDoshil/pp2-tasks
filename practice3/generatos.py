# generators.py
# Iterator and generator exercises

# =========================
# Exercise 1: Custom Iterator
# =========================
# Create an iterator that returns numbers from 1 to n (inclusive).

class CountToN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# =========================
# Exercise 2: Simple Generator
# =========================
# Write a generator that yields squares of numbers from 1 to n.

def squares(n):
    for i in range(1, n + 1):
        yield i * i


# =========================
# Exercise 3: Even Numbers Generator
# =========================
# Generate all even numbers from 0 up to n (inclusive).

def evens(n):
    for i in range(0, n + 1, 2):
        yield i


# =========================
# Exercise 4: Fibonacci Generator
# =========================
# Generate the first n Fibonacci numbers.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# =========================
# Exercise 5: Infinite Generator
# =========================
# Create an infinite generator of natural numbers starting from 1.

def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1


# =========================
# Exercise 6: Generator Expression
# =========================
# Use a generator expression to generate cubes of numbers from 1 to n.

def cubes(n):
    return (i ** 3 for i in range(1, n + 1))


# =========================
# Exercise 7: String Iterator
# =========================
# Create an iterator over words in a sentence.

class WordIterator:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


# =========================
# Tests / Examples
# =========================
if __name__ == "__main__":
    print("Exercise 1:")
    for x in CountToN(5):
        print(x, end=" ")
    print("\n")

    print("Exercise 2:")
    print(list(squares(5)))

    print("Exercise 3:")
    print(list(evens(10)))

    print("Exercise 4:")
    print(list(fibonacci(7)))

    print("Exercise 5:")
    gen = infinite_numbers()
    for _ in range(5):
        print(next(gen), end=" ")
    print("\n")

    print("Exercise 6:")
    print(list(cubes(4)))

    print("Exercise 7:")
    for w in WordIterator("Generators are very useful"):
        print(w)