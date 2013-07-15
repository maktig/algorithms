#!/usr/bin/env python
#
# generates a list of numbers in shuffled order
#
# uses last element as the pivot point
#
# reorders array as such:
#   if i < pivot, swap before pivot
#   if i > pivot, swap after pivot
#
import random

# creates a list of numbers and shuffles the order
i_max = 10
list = [i for i in range(1,i_max+1)]
random.shuffle(list)

print 'List before:', list

pivot = list[-1]
print 'Pivot number:', pivot

# boundary pivot point
j = 0
# loop through list and swap values
for i,n in enumerate(list):
    if n <= list[-1]:
        list[j], list[i] = list[i], list[j]
        j += 1

print 'List after:', list
