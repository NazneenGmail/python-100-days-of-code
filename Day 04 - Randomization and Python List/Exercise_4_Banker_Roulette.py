import random
friends = ["Alice", "Bob", "Charlie", "David", "Emma"]

print("\nUsing RandomRang")
index = random.randrange(0, len(friends))
print(friends[index])

print("\nUseing Random Choice, which accepts a sequence as argument")
print(random.choice(friends))
