from collections import Counter
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)
