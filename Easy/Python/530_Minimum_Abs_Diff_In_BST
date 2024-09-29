#To address this problem, you have to know the various forms of traversal with a binary search tree. The three types are post-order, pre-order,..
#..and in-order. For this problem, we have to go in-order, which is from left to right in a binary search tree. Binary search trees have a right and left..
#..tree from the root. Every binary search tree has branches and leafs. Branches are nodes that have children and leafs have no children.
#To approach this problem, we first conduct an in-order traversal to retrieve all the values from the list in order by inputting the root node.
#After that, we calculate the minimum difference by first setting a variable equal to the highest possible value, which is float('inf'), which..
#..represents infinity. Then, we iterate through the list from index 1 (not 0 since we compare the i and i-1 index, not i and i + 1 index).
#If the two current indices subtracted is less than the current value stored in min_diff, then min_diff becomes equal to that value. Then, we simply..
#..just return min_diff. I'd recommend looking at the different types of traversals for binary search trees.

#Time complexity: O(n)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        
        # Helper function for traversal (in-order).
        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Traverse left subtree.
            values.append(node.val)  # Store the node value.
            inorder(node.right)  # Traverse right subtree.
        
        # Perform in-order traversal on the root to get values in order.
        inorder(root)
        
        # Calculate the minimum absolute difference between consecutive values (i and i-1).
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])
        
        return min_diff

#EX: 
#               4
#              / \
#             2   6 
#            / \ / \
#           1  3 5  7

#For this binary search tree, we traverse from left to right, so the values get stored in an array in this order:..
#..[1,2,3,4,5,6,7]. Then, we iterate through and subtract the ith and ith - 1 values in the array to find the min_diff.
#Step 1: min_diff = infinity. 2 - 1 = 1, which is < infinity, so min_diff is now 1.
#Step 2: min_diff = 1. 3-2 = 1, which is equal to 1, so nothing happens, so min_diff is still 1.
#..this will happen for all values in the list, and in this particular list, all the values subtracted with this pattern yield 1.
#So, our final answer would just be 1.