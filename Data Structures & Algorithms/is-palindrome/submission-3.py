class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [i for i in s.lower().split()]
        splitted_string = "".join([i for i in "".join(x) if i.isalnum()])
        return splitted_string == splitted_string[::-1]