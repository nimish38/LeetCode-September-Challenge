class Solution(object):
    def sortArray(self, nums):
        def Partition(A,p,r):
            pivot = A[(p+2*r)//3]
            i = p-1
            j = r+1
            while True:
                i += 1
                while A[i] < pivot:
                    i += 1
                j -= 1
                while A[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                A[i],A[j] = A[j],A[i]

        def Quicksort(A,p,r):
            if p < r:
                q = Partition(A,p,r)
                Quicksort(A,p,q)
                Quicksort(A,q+1,r)
            return A

        Quicksort(nums,0,len(nums)-1)
