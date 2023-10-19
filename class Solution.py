class Solution:
    def countVowels(self, word: str) -> int:
        count, vowelSum = 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i, char in enumerate(word, start=1):
            if char in vowels:
                vowelSum += i
            count += vowelSum

        return count
