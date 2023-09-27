class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        if n== 0 or n== 1:
            return 0
        i=0
        j=n-1
        ans=float("-inf")
        while(i<j):
            x=min(height[i],height[j])*(j-i)
            ans=max(ans,x)
            
            if min(height[i],height[j])==height[i]:
                i=i+1
            else:
                j=j-1
        return ans
            
        