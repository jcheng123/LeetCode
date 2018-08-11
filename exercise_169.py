class Solution:
      def majorityElement(self, nums):
           nums_dict = {}
           for num in nums:
              if not num in num_dict.keys():
                   nums_dict[num] = 1
              else:
                   nums_dict[num] = nums_dict[num] + 1
           
           appearance_num = {}
           for item in nums_dict:
               appearance_num[item[1]].append(item[0])
           
           break_point = -1
           for num in appearance_num.keys():
               if num >= floor(len(nums)/2):
                  break_point = num
                  break
           
           return break_point

           
