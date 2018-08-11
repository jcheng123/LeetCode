class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 1
        while i < len(A) - 1:
            if A[i - 1] < A[i]:
                i = i + 1
                continue
            else:
                break

        return i - 1


def main():
    solution = Solution()
    A = [1, 2, 1, 0]
    print(solution.peakIndexInMountainArray(A))

if __name__ == "__main__":
    main()