class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dis = 0
       
        while max(x, y) > 0:
        	x1 = x % 2
        	y1 = y % 2
        	x  = x // 2
        	y  = y // 2

        	if x1 != y1:
        		dis = dis + 1

        return dis


def main():
	solution = Solution()
	dis = solution.hammingDistance(5, 4)
	print("dis is ", dis)


if __name__ == "__main__":
	main()

