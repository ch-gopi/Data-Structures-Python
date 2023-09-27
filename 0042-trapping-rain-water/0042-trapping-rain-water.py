class Solution:
    def trap(self, height: List[int]) -> int:
        A=list(height)
        n=len(A)
        lm=[0]*n
        rm=[0]*n
        lm[0]=A[0]
        rm[n-1]=A[n-1]
        for i in range(1,n):
            if lm[i-1]<A[i]:
                lm[i]=A[i]
            else:
                lm[i]=lm[i-1]
        for i in range(n-2,0,-1):
            if rm[i+1]>A[i]:
                rm[i] = rm[i+1]
            else:
                rm[i] = A[i]
        summ=0
        x=0
        for i in range(1,n-1):
         x=min(lm[i-1],rm[i+1])-A[i]
         if x>0:
           summ=summ+x
        return summ
        