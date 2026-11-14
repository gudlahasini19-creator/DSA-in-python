class Solution(object):
    def isPalindrome(self, s):
        """
        Problem: LeetCode 125 - Valid Palindrome
        Approach: Two Pointers (Inward Convergence)
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        l = 0
        r = len(s) - 1

        while l < r:
            # 1. Skip non-alphanumeric characters on the left
            while l < r and not s[l].isalnum():
                l += 1
            
            # 2. Skip non-alphanumeric characters on the right
            while l < r and not s[r].isalnum():
                r -= 1

            # 3. Compare characters in lowercase
            if s[l].lower() != s[r].lower():
                return False

            # 4. Move inward
            l += 1
            r -= 1

        return True
