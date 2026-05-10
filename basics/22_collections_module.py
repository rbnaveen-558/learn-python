"""
Python Collections Module Examples

The collections module provides specialized container datatypes that provide alternatives to Python's general purpose built-in containers.
"""

from collections import namedtuple, deque, Counter, OrderedDict, defaultdict

# 1. namedtuple - Factory function for creating tuple subclasses with named fields
print("=== namedtuple Examples ===")

# Create a namedtuple for a Point
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
p2 = Point(30, 40)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"p1.x = {p1.x}, p1.y = {p1.y}")
print(f"Distance from origin: {p1.x + p1.y}")

# 2. deque - Double-ended queue for fast appends and pops from both ends
print("\n=== deque Examples ===")

# Create a deque
d = deque([1, 2, 3, 4, 5])
print(f"Initial deque: {d}")

# Append to right
d.append(6)
print(f"After append(6): {d}")

# Append to left
d.appendleft(0)
print(f"After appendleft(0): {d}")

# Pop from right
right = d.pop()
print(f"Popped from right: {right}, deque: {d}")

# Pop from left
left = d.popleft()
print(f"Popped from left: {left}, deque: {d}")

# Rotate
d.rotate(2)
print(f"After rotate(2): {d}")

# 3. Counter - Dict subclass for counting hashable objects
print("\n=== Counter Examples ===")

# Count elements in a list
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = Counter(words)
print(f"Word counts: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# Count characters in a string
text = "hello world"
char_count = Counter(text)
print(f"Character counts: {char_count}")

# Update counts
word_count.update(['apple', 'date'])
print(f"After update: {word_count}")

# 4. OrderedDict - Dict that remembers insertion order
print("\n=== OrderedDict Examples ===")

# Create an OrderedDict
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"OrderedDict: {od}")

# Move an item to the end
od.move_to_end('first')
print(f"After move_to_end('first'): {od}")

# Pop last item
last = od.popitem(last=True)
print(f"Popped last: {last}, remaining: {od}")

# 5. defaultdict - Dict subclass that calls a factory function to supply missing values
print("\n=== defaultdict Examples ===")

# Create a defaultdict with list as default factory
dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
dd_list['fruits'].append('banana')
dd_list['vegetables'].append('carrot')
print(f"defaultdict with list: {dd_list}")

# Create a defaultdict with int as default factory (for counting)
dd_int = defaultdict(int)
words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
for word in words:
    dd_int[word] += 1
print(f"defaultdict with int: {dd_int}")

# Create a defaultdict with set as default factory
dd_set = defaultdict(set)
dd_set['group1'].add('alice')
dd_set['group1'].add('bob')
dd_set['group2'].add('charlie')
print(f"defaultdict with set: {dd_set}")

print("\n=== Additional Examples ===")

# ChainMap - For combining multiple dicts
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined = ChainMap(dict1, dict2)
print(f"ChainMap: {combined}")
print(f"combined['b'] = {combined['b']} (from first dict)")

# UserList, UserDict, UserString - For subclassing
from collections import UserList
class MyList(UserList):
    def sum(self):
        return sum(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(f"MyList sum: {my_list.sum()}")