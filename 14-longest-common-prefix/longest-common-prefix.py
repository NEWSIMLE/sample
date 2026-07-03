class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        words=strs
        small=min(words,key=len)
        pre=""
        for i in range (len(small)):
            check=True
            for word in words:
                if small[i]!=word[i]:
                    check=False
                    break
            if check ==True:
                pre+=small[i]
            else:
                break
        return pre