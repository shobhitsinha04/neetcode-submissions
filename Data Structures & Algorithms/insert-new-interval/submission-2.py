class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0 
        n = len(intervals)
        # this is berfor ethe newInterval has come into play
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # this is handling the merging of the intervals
        start, end = newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # then yuoi carry on with the rest 
        while i < n:
            result.append(intervals[i])
            i += 1
        return result