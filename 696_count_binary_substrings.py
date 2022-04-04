class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return 0
        curr_length = 1
        prev_length = 0
        p = s[0]
        res=0
        for i in range(1,len(s)):
            if s[i]==p:
                curr_length+=1
            else:
                prev_length = curr_length
                curr_length=1
            if prev_length>=curr_length:
                res+=1
            p = s[i]
        return res