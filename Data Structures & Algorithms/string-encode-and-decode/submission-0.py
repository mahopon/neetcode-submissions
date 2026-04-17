class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        newStr = []
        for s in strs:
            sLen = len(s)
            newStr.append(f"{sLen}#{s}")
        return "".join(newStr)
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        ptr = 0
        res = []
        currCount = 0
        while ptr < len(s):
            iPtr = ptr
            # Up to #
            while s[iPtr] != '#':
                iPtr += 1

            length = int(s[ptr:iPtr])
            # Ignore #
            ptr = iPtr + 1

            word = s[ptr:ptr + length]
            res.append(word)

            ptr += length

        return res
