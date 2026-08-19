class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum() is True:
                cleaned_string += char.lower()
        
        if cleaned_string == cleaned_string[::-1]:
            return True
        else:
            return False