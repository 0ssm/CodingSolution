class Solution(object):
    def isPalindrome(self,n):
        st = str(n)
        rev = st[::-1]
        if rev == st:
            return rev
        if rev == n:
            print("palindrome")
        else:
            print("not palindrome")
print(Solution().isPalindrome(n = 121))