#!/bin/python3
# Hackerrank problem : https://www.hackerrank.com/challenges/sparse-arrays
# This is probably not the solution that the authors expected, but it works OK within time limits.
# The problem was probably targeting C++ and - as the name suggests - using sparse arrays.

import os
from collections import Counter


# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    l = []
    c = Counter(strings)
    for q in queries:
        l.append(0 if q not in c.keys() else c[q])
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
