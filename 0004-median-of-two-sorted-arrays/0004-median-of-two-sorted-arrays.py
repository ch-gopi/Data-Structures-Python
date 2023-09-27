from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the shorter array
        
        x = len(nums1)
        y = len(nums2)
        
        l = 0
        r = x
        
        while l <= r:
            ptX = (l + r) // 2
            ptY = (x + y + 1) // 2 - ptX
            
            maxleftX = float("-inf") if ptX == 0 else nums1[ptX - 1]
            minrightX = float("inf") if ptX == x else nums1[ptX]
            
            maxleftY = float("-inf") if ptY == 0 else nums2[ptY - 1]
            minrightY = float("inf") if ptY == y else nums2[ptY]
            
            if maxleftX <= minrightY and maxleftY <= minrightX:
                if (x + y) % 2 == 0:
                    return (max(maxleftX, maxleftY) + min(minrightX, minrightY)) / 2.0
                else:
                    return max(maxleftX, maxleftY)
            elif maxleftX > minrightY:
                r = ptX - 1
            else:
                l = ptX + 1

        