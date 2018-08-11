class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        i = length - 1

        while i >= 0:
            num = 1
            while i >= num and nums[i - num] == nums[i]:
                num = num + 1 # num is the number of nums[i]


            if num > 2:
               for j in range(2, num):
                   print(nums.pop(i))
                   i = i - 1
                   num = num - 1
                   
            i = i - num

        return nums

def main():
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 1, 2, 3, 4, 5, 7]))


if __name__ == "__main__":
    main()
            





            
            
        
