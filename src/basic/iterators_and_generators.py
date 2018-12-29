"""
    Iterables are objects that can return one of their elements at a time, SUCH 
AS A LIST. Many of the built-in functions we have used so far, like enumerate,
return an iterator

    An ITERATOR is an object that represents a stream of data. This is 
different from a list, which is also an ITERABLE, but not an ITERATOR because 
it is not a stream of data.

    Generators are a simple way to create iterators using functions. You can 
also define iterators using classe
"""

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0, debug=False):
    if debug:
        print("start debug")
        print(iterable)
        print("end debug")
        
    count = start
    for element in iterable:
        yield count, element
        count += 1
        
def test_my_enumerate(iterable, start=0, debug=False):
    for i, lesson in my_enumerate(iterable, start, debug):
        print("Lesson {}: {}".format(i, lesson))
        
print("\nTesting test_my_enumerate")        
print("\n@test_my_enumerate 1")
test_my_enumerate(["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"], 1)
print("\n@test_my_enumerate 2")
test_my_enumerate(['a', 'b', 'c'], debug=True)
print("\n@test_my_enumerate 3")
test_my_enumerate(['a', 'b', 'c'], 6)
print("\n@test_my_enumerate 4")
test_my_enumerate('python', 2)

print("\nTesting Chunker\n")

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
