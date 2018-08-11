class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        index = 1
        length = len(nums)
        while index < length:

            while index < length  and nums[index - 1] == nums[index]:
                nums.pop(index)
                length = length - 1
            index = index + 1
        return length

def main():
    solution = Solution()
    print(solution.removeDuplicates([1, 1]))

if __name__ == "__main__":
    main()