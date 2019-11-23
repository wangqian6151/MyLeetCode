# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
#
# 你可以假设 nums1 和 nums2 不会同时为空。 
#
# 示例 1: 
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 
#
# 示例 2: 
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
# 
# Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = int((m + n - 1) / 2)
        lo, hi = 0, m
        while lo < hi:
            i = int((lo + hi) / 2)
            if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0
# leetcode submit region end(Prohibit modification and deletion)
