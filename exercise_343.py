class Solution:

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            else:
              for j in range(i + 1, len(nums)):
                  if nums[j] == 0:
                      continue
                  else:
                     nums[j], nums[i] = nums[i], nums[j]
                     break

def main():
    solution = Solution()
    NUMS = [0, 0, 4, 1, 2, 3, 0, 0]
    solution.moveZeroes(NUMS)
    print(NUMS)


if __name__ == "__main__":
    main()
