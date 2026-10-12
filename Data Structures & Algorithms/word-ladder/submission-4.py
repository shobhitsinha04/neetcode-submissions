class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # we are going to make a dict that will store all possible patterns 
        # and the value to each pattern would be all words that can be 
        # formed by it
        nei = collections.defaultdict(list)
        # default dict used as you can have no value and itll be chilling 
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nword in nei[pattern]:
                        if nword not in visit:
                            visit.add(nword)
                            q.append(nword)
            res += 1
        return 0