class Solution:
   def containDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums_set) < len(nums):
               return True
        return False

def main():
    solution = Solution()
    nums = [1, 4, 2, 2]
    print(solution.containDuplicate(nums))

if __name__=="__main__":
    main()
