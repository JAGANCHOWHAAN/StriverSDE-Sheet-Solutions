class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A_repeated=sum(A)-sum(set(A)) #set function is to remove the duplicates
        n=len(A)
        sum_n=int((n*(n+1))/2) #sum of first n natural number formula
        B_missing=sum_n-sum(set(A))
        return [A_repeated,B_missing]