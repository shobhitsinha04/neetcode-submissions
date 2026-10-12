class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if not intervals:
        #     return []
        # intervals.sort()
        # res = [intervals[0]]
        # for start, end in intervals[1:]:
        #     last_end = res[-1][1]
        #     if start <= last_end:
        #         res[-1][1] = max(last_end, end)
        #     else:
        #         res.append([start, end])
        # return res
        if not intervals:
            return []
        intervals.sort()
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
