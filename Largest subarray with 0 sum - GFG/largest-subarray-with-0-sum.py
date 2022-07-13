#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        hash_map={}
        max_len=0
        curr_sum=0
        for i in range(n):
            curr_sum+=arr[i]
            if arr[i] is 0 and max_len is 0:
                max_len=1
            if curr_sum is 0:
                max_len=i+1
            if curr_sum in hash_map:
                max_len=max(max_len,i-hash_map[curr_sum])
            else:
                hash_map[curr_sum]=i
        return max_len
            
        #Code here

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends