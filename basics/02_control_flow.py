# Sample: Python Control Flow

# if, elif, else
score = 85
if score > 90:
    print("Excellent")
elif score > 75:
    print("Good")
else:
    print("Needs Improvement")

# for loop
for fruit in ["apple", "banana", "cherry"]:
    print("Fruit:", fruit)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# break, continue, pass
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("Loop index:", i)
    pass
