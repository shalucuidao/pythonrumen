
from collections import deque
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right



def maxDepth(root) -> int:
	if root is None:
		return 0

	leftdepth = maxDepth(root.left)
	rightdepth = maxDepth(root.right)

	return max(leftdepth, rightdepth) + 1


class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if root is None:
			return []

		cur = [root]
		ans = []

		while cur:
		    nxt = []
		    vals = []
		    for node in cur:
		        vals.append(node.val) # 没想到的
		        if node.left:nxt.append(node.left)
		        if node.right:nxt.append(node.right)
		    ans.append(vals)

		    cur = nxt

		return ans
	def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
		if root is None:
			return []

		ans = []
		q = deque([root])

		while q:
			vals = []
			for _ in range(len(q)):
				node = q.popleft()
				vals.append(node.val)
				if node.left: q.append(node.left)
				if node.right: q.append(node.right)
			ans.append(vals)
		return ans

if __name__ == '__main__':
    lis = [4,5]
    lis2 =[]
    lis2.append(lis[::-1])
    print(lis2)

	# root = TreeNode(3, TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
	# depth = maxDepth(root)
	# print(depth)

