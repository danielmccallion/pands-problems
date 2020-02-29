# Daniel Mc Callion
# Using random and pop keep printing a random list of 10 removing
# one number each time until the list is empty

import random

queue = []
queue_length = 10
range_max = 100

for n in range(0, queue_length):
    queue.append(random.randint(0, range_max))

print(f"Queue is {queue}")

while len(queue) != 0:
    print(f"Current number is {queue[0]} and the queue is {queue[1:]}")
    queue.pop(0)

print("The queue is now empty")