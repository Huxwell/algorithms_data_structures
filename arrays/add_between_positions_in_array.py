#!/bin/python3
# A very tricky problem : https://www.hackerrank.com/challenges/crush/problem
# Example :
#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of  between the indices  and  inclusive:
#
# index->	 1 2 3  4  5 6 7 8 9 10
# 	[0,0,0, 0, 0,0,0,0,0, 0]
# 	[3,3,3, 3, 3,0,0,0,0, 0]
# 	[3,3,3,10,10,7,7,7,0, 0]
# 	[3,3,3,10,10,8,8,8,1, 0]
# It is easy with linear complexity per query, but it is hard to get constant per query.
# The solution is to only store difference between values on subsequent positions instead of storing the actual values.

import os


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l = n
    n = [0] * n
    for beg, end, val in queries:
        n[beg - 1] += val
        if end < l:
            n[end] -= val

    prev = n[0]
    for i in range(1, l):
        n[i] = prev + n[i]
        prev = n[i]
    return max(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()