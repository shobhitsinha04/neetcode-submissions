class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # building graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        taken = 0 

        while q:
            course = q.popleft()
            taken += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return taken == numCourses

        # graph[1] = [0]
        # indegree = [1,0]
        # course 1 has indegree 0, add to queue
        # course 1, taken =1 
        # therefore indegree of course 0 goes to 0, add to queue
        # take course 0, taken = 2
        # taken == 2 == numCourses
        # true


        # premap = { i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     premap[crs].append(pre)
        
        # visit = set()

        # def dfs(c):
        #     if c in visit:
        #         return False # cycle is there then
        #     if premap[c] == []:
        #         return True # all pres done
            
        #     visit.add(c)

        #     for pre in premap[c]:
        #         if not dfs(pre):
        #             return False
        #     visit.remove(c)
        #     premap[c] = []
        #     return True

        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True