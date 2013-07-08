#!/usr/bin/env python

def mergesort(numbers):
    if len(numbers) > 1:
        s1, s2 = split(numbers)
        s1, inv1 = mergesort(s1)
        s2, inv2 = mergesort(s2)
        merged, inv_cnt = merge(s1, s2, inv1, inv2)
        return merged, inv_cnt
    else:
        return numbers, 0

def merge(s1, s2, inv1, inv2):
    s = []
    s1_idx = 0
    s2_idx = 0
    inv = (inv1 + inv2)
    size1 = len(s1)
    size2 = len(s2)

    while s1_idx < size1 and s2_idx < size2:
        if s1[s1_idx] <= s2[s2_idx]:
            s.append(s1[s1_idx])
            s1_idx += 1
        else:
            s.append(s2[s2_idx])
            s2_idx += 1
            inv += size1 - s1_idx

    for i in range(s1_idx, size1):
        s.append(s1[i])

    for i in range(s2_idx, size2):
        s.append(s2[i])

    return s, inv

def split(numbers):
    size = len(numbers)
    half = size / 2
    s1 = [numbers[i] for i in range(0, half)]
    s2 = [numbers[i] for i in range(half, size)]
    return s1, s2

# test file with max number of inversions for 100,000 numbers -- n*(n-1)/2 = 4,999,950,000
file = 'IntegerArray2.txt'

# assignment file
file = 'IntegerArray.txt'

with open(file) as f:
    numbers = [int(i) for i in f]

print 'before mergesort:', numbers

sorted, inversion_count = mergesort(numbers)

print 'after mergesort:', sorted
print 'inversion count:', inversion_count
