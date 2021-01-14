"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/14 11:42'
"""
class QuickSort():
    def main(self,A):
        self.quick_sort(A,0,len(A) - 1)
        return print(A)
    def quick_sort(self,A,p,r):
        if p < r:
            q = self.partition(A,p,r)
            self.quick_sort(A, p, q - 1)
            self.quick_sort(A, q + 1, r)
    def partition(self,A,p,r):
        x = A[r]
        i = p -1
        for j in range(p,r):
            if A[j] <= x:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i + 1],A[r] = A[r], A[i + 1]
        return i + 1
A = [0,5,2,-2,77,66]
quicksort = QuickSort()
quicksort.main(A)