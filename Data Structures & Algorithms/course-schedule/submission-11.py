class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i: [] for i in range(numCourses)}
        print(premap)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        visit = set()

        def dfs(c):
            if c in visit:
                return False # cycle is there then
            if premap[c] == []:
                return True # all pres done
            
            visit.add(c)

            for pre in premap[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            premap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        print(premap)
        return True