#! /home/laojiang/anaconda3/bin/python
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = ""
        for i in str:
            if i >= 'A' and i <= 'Z':
               s = s + i.lower()
            else:
               s = s + i
        return s

def main():
    solution = Solution()
    s = solution.toLowerCase('AAAzzz')
    print(s)


if __name__ == "__main__":
    main()