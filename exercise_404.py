class TreeNode:
      def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None

class Solution:
      def sumOfLeftLeaves(self, root):
          """
          :type root: TreeNode
          :rtype: int
          """

          if root == None:
             return 0
          
          if root.left == None:
             return self.sumOfLeftLeaves(root.right)
          
          if root.left.left == None and root.left.right == None:
             return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + root.left.val



def main():
    # [3,9,20,null,null,15,7]
    p1 = TreeNode(3)
    p2 = TreeNode(9)
    p3 = TreeNode(20)
    p4 = None
    p5 = None
    p6 = TreeNode(15)
    p7 = TreeNode(7)

    p1.left = p2
    p1.right = p3

    p2.left = p4
    p2.right = p5

    p3.left = p6
    p3.right = p7

    solution = Solution()
    print('start!')
    print(solution.sumOfLeftLeaves(p1))

if __name__ == "__main__":
  main()

    
