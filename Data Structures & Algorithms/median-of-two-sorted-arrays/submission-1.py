class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        
        n = len(nums1)
        m = len(nums2)
        mid = (n+m)//2

        start = 0
        end = len(nums1)
        while start <= end:
            middle1 = (start+end)//2
            middle2 = mid - middle1

            if middle1 == 0:
                left1 = -float("inf")
            else:
                left1 = nums1[middle1 - 1]

            if middle1 == n:
                right1 = float("inf")
            else:
                right1 = nums1[middle1]

            if middle2 == 0:
                left2 = -float("inf")
            else:
                left2 = nums2[middle2 - 1]

            if middle2 == m:
                right2 = float("inf")
            else:
                right2 = nums2[middle2]

            if left1 > right2:
                end = middle1 - 1
            elif right1 < left2:
                start = middle1 + 1      
            else:
                break

        if (n+m)%2:
            return min(right1, right2)
        else:
            return (max(left1,left2) + min(right1,right2))/2


