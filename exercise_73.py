class Solution:
    def findZeros(self, nums):
        for num in nums:
            if num == 0:
              return True

        return False
                
    def setZeros(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

