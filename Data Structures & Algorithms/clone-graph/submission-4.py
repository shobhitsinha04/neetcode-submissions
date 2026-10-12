"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}

        def dfs(node):
            if node in old_new:
                return old_new[node]
            copy = Node(node.val)
            old_new[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        if node:
            return dfs(node)
        else:
            None




        # if not node:
        #     return None
        # oldtonew = {}
        # copy = Node(node.val)
        # oldtonew[node] = copy

        # q = deque([node])
        # while q:
        #     cur = q.popleft()
        #     for n in cur.neighbors:
        #         if n not in oldtonew:
        #             oldtonew[n] = Node(n.val)
        #             q.append(n)
        #         oldtonew[cur].neighbors.append(oldtonew[n])
        # return oldtonew[node]