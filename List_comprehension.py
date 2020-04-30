
# In this example we will see how to write list comprehensions to make our tasks easier

# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is
# the result of some operations applied to each member of another sequence
# or iterable, or to create a subsequence of those elements that satisfy a certain condition.

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

# Side Effect of above operation:It creates a variable(or overwrites) named 'x'
# that still exists after the loop completes. To get rid of this Side Effect we use List comprehensions.

# List comprehension:
numbers = [i for i in range(10)]
print(numbers)

# Let us see few more examples
squares = [i * i for i in range(10)]
print(squares)

# This is same as:
squares = []
for i in range(10):
    squares.append(i * i)

# Some more:
odds = [i for i in numbers if i % 2 != 0]
print(odds)

# This is same as:
odds = []
for i in numbers:
    if i % 2 != 0:
        odds.append(i)

# We can also use functions in comprehensions
def isSqaure(x):
    import math
    sqrt = int(math.sqrt(x))
    return x == sqrt * sqrt

squares = [x for x in range(100) if isSqaure(x) == True]
print(squares)

# Some Complex comprehensions:
pairs = [[x, x * x] for x in numbers]
print(pairs)