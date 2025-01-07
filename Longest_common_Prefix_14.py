from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return s[:i]
    
    # Take user input
if __name__ == "__main__":
    print("Enter strings separated by spaces:")
    user_input = input().strip()
    strs = user_input.split()  # Split the input into a list of strings
    
    # Create an instance of Solution and call the function
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    
    print("Longest Common Prefix:", result)