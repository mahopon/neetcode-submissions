class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = collections.Counter(s)
        count_2 = collections.Counter(t)

        if count_1 == count_2:
            return True
        return False