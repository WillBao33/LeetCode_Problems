class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i]+'*'+word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            curr_word, steps = queue.popleft()
            for i in range(len(curr_word)):
                intermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return steps + 1
                    if word not in seen:
                        seen.add(word)
                        queue.append((word, steps + 1))
            all_combo_dict[intermediate_word] = []

        return 0
