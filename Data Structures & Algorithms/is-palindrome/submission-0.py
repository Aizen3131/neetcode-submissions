class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = s.replace(" ", "")
        ss = ""
        for x in stri:
            if x.isalnum():
                ss += x

        ss = ss.lower()
        z = ss[::-1]

        print(ss)
        print(z)

        return z == ss