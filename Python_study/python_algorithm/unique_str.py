# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

class Solution:
    def CheckArray(self,noRepetiton,j) -> bool:
        for i in range(len(noRepetiton)):
            if j == noRepetiton[i]:
                return False
        return True

    def isUnique(self, astr: str) -> bool:
        noRepetiton = []
        for i in astr:
            if self.CheckArray(noRepetiton,i):
                noRepetiton.append(i)
            else:
                return False
        return True
if __name__ == '__main__':
    mySolution = Solution()
    mySolution.isUnique("leetcode")