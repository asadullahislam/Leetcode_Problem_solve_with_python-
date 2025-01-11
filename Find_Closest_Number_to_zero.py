from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]  # Initialize closest to the first element
        
        for x in nums:
            # Check if the current number is closer to zero
            if abs(x) < abs(closest):
                closest = x
            # If equally close to zero, choose the larger number
            elif abs(x) == abs(closest) and x > closest:
                closest = x
        
        return closest

# User input system
if __name__ == "__main__":
    # Ask the user to input a list of numbers separated by spaces
    input_nums = input("Enter a list of integers separated by spaces: ")
    
    # Convert the input string into a list of integers
    nums = list(map(int, input_nums.split()))
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the findClosestNumber method and print the result
    closest_number = solution.findClosestNumber(nums)
    print("The number closest to zero is:", closest_number)
