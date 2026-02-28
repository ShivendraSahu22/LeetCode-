class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_length = len(pref)
        for s in strs[1:]:
            while pref != s[0:pref_length]:
                pref_length -= 1
                if pref_length == 0:
                    return ""
                pref = pref [ 0:pref_length]
        return pref