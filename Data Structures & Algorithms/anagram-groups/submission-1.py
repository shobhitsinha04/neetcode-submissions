class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_maps = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
            h_maps[tuple(count)].append(s)
        return list(h_maps.values())
