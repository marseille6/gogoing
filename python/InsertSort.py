"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/14 13:21'
"""
class InsertSort():
    def insert_sort(self,A):
        for j in range(1,len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        return A
a = [7,0,2,5,12,89,2,-2]
insertSort = InsertSort()
insertSort.insert_sort(a)
print(a)