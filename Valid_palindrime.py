class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=''
        for i in s:
            if(i.isalnum()):
                d=d+i
        d=d.lower()
        if(d==d[::-1]):
            return 1
        return 0
                
