from functools import reduce

li1 = ["Naveen", "Shubham", "Geol", "Kumar"]

# Build the interleaved list of tuples manually without zip_longest
max_len = max(len(name) for name in li1)
interleaved_tuples = [tuple(name[i] if i < len(name) else '' for name in li1) for i in range(max_len)]

print("Interleaved tuples:", interleaved_tuples)

print(''.join(interleaved_tuples[0]))  # Output: "NSGK"

# Solution 1: Using join and generator expression
interleaved_join = ''.join(''.join(chars) for chars in interleaved_tuples)

# Solution 2: Using reduce
interleaved_reduce = reduce(lambda acc, chars: acc + ''.join(chars), interleaved_tuples, '')

print("Using join:", interleaved_join)
print("Using reduce:", interleaved_reduce)