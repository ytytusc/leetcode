class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        
        from collections import deque
        
        queue = deque([beginWord])
        visited = set([beginWord])
        
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return distance
                neighbors = self.get_neighbors(curr)
                for neighbor in neighbors:
                    if neighbor not in wordList or neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        return 0
        
    def get_neighbors(self,word):
        neighbors = []
        
        for i in range(len(word)):
            pre = word[:i]
            post = word[i+1:]
            
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[i]:
                    continue
                neighbor = pre + char + post
                neighbors.append(neighbor)
        
        return neighbors
