#URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。
# （注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        result = []
        for i in range(length):
            if S[i] == " ":
                result.append("%20")  # 遇到空格时替换为'%20'
            else:
                result.append(S[i])  # 其他字符直接追加
        return "".join(result)  # 将列表连接成字符串
