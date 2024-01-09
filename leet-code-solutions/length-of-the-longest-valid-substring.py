class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        seen = set(forbidden)
        res, left = 0, 0

        for i in range(len(word)):
            for j in range(max(left, i-9), i+1):
                if word[j:i+1] in seen:
                    left = j+ 1

            res = max(res, i - left+1)

        return res