from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])
        next_queue = deque()
        steps = 0

        while queue:
            for it in range(len(queue)):
                current_word = queue.popleft()
                for i in range(len(current_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = current_word[:i] + c + current_word[i+1:]

                        if new_word == endWord:
                            return steps + 1

                        if new_word in wordSet:
                            next_queue.append(new_word)
                            wordSet.remove(new_word)
            steps += 1
            queue = next_queue
            next_queue = deque()

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"]))
