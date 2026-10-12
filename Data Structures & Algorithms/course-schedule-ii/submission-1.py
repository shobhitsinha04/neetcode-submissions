class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph[b] -> courses that depend on b
        graph = [ [] for _ in range(numCourses)]

        indegree = [0] * numCourses # prereqs per course

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        # courses with no prereqs
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            course = q.popleft()
            order.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        if len(order) != numCourses:
            return []
        return order