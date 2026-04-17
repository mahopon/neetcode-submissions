class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = defaultdict(int)
        count_2 = defaultdict(int)

        for letter in s:
            count_1[letter] += 1
        for letter in t:
            count_2[letter] += 1

        if count_1 == count_2:
            return True
        return False