"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from __future__ import print_function


def euler_001_a(limit):
    s1, s2 = set(range(0, limit, 3)), set(range(0, limit, 5))

    return sum(s1.union(s2))


def euler_001_b(limit):
    return sum(i for i in xrange(limit) if not (i % 3 and i % 5))


def euler_001_c(limit):
    l = [i for i in xrange(limit) if not (i % 3 and i % 5)]

    return reduce(lambda x, y: x + y, l)

response = euler_001_a(1000)
# response = euler_001_b(1000)
# response = euler_001_c(1000)

print(response)
