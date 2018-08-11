class Solution:
	def findTheDifference(self, s, t):
		sl = list(s)
		tl = list(t)
		sl.sort()
		tl.sort()

		for i in range(len(sl)):
			if sl[i] != tl[i]:
				return tl[i]

		return tl[-1]


def main():
	solution = Solution()
	print(solution.findTheDifference('abc', 'akd'))


if __name__ == "__main__":
	main()
