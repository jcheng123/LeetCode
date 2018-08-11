class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        nlist = []
        for j in range(n + 1):
            nlist.append(0) # ignore nlist[0], and nlist[i] denotes the least number of the square number.

        while i * i <= n:
        	nlist[i * i] = 1
        	i = i + 1


        for i in range(1, n + 1):
        	if nlist[i] == 1:
        		continue

        	num = i	
        	for j in range(1, i // 2 + 1):
        	    num = min(num, nlist[i - j] + nlist[j])

        	nlist[i] = num

        return nlist[n]

def main():
	solution = Solution()
	num = solution.numSquares(376)
	print(num)


if __name__ == "__main__":
	main()


