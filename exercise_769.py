class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ref = sorted(arr)
        for i in range(len(ref)):
            