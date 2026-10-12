class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # number -> frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1 
        sorted_nums = sorted(count, key = lambda x: count[x], reverse = True)
        return sorted_nums[:k]



        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1 #+ count.get(num, 0)
        # freq = [ [] for i in range(len(nums)+1)]
        # for num, cnt in count.items():
        #     freq[cnt].append(num)
        # res = []
        # for i in range(len(freq)-1, 0,-1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res


        # count = defaultdict(int)
        # ret = []
        # for num in nums:
        #     count[num] += 1
        # top = heapq.nlargest(k, count.items(), key = lambda x : x[1])
        # for num, _ in top:
        #     ret.append(num)
        # return ret
        