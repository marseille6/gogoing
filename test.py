"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/13 10:33'
"""
a = "123"
s = "231"
d = "312"
print(sorted(s))
dic = {}
dic[''.join(sorted(a))] = 1
dic[''.join(sorted(s))] += 1
dic[''.join(sorted(d))] += 1
print(dic)
for a,b in dic.items():
    print(a)
    print(b)

a = "1"
a = a + "2"
print(a)
print(ord('a'))

from collections import deque