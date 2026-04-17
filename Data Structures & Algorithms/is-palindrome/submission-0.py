class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r"[^0-9A-Za-z]", "", s)
        lower_s = new_s.lower()

        mid = len(lower_s) // 2
        for i in range(mid):
            if lower_s[i] != lower_s[len(lower_s) - 1 - i]:
                return False
        return True