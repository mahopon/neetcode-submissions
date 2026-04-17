class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_str = sorted(s)
            res[tuple(sorted_str)].append(s)
        return [l for l in res.values()]