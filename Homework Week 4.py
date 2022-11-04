"""
Two Sum
-------------------------------------------------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to target.

You may assume that each input would have at least one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE 1:
---------------------------------------------------------------
Input: nums = [2,7,11,15], target = 9
Output: [2, 7]
Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

EXAMPLE 2:
---------------------------------------------------------------
Input: nums = [3,2,4], target = 6
Output: [2, 4]

EXAMPLE 3:
---------------------------------------------------------------
Input: nums = [3,3], target = 6
Output: [3, 3]

NOTES:
---------------------------------------------------------------
- An input MAY HAVE no two numbers at all (an empty one still counts as a solution) - in this case, return a empty array
- It's an array of integer numbers - these numbers are not necessarily distinct / unique
- Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there anyway you could've done...
...better or not? Why or why not? Justify.
"""


class Answer:
    def twoSum(self, numbers, target):
        dict = {}
        for x, number in enumerate(numbers):
            number2 = target - number
            if number in dict:
                return [dict[number], x]
            else:
                dict[number2] = x
        return []


array = [7, 11, 19, 8]
target = 27
ans = Answer()
print(ans.twoSum(array, target))


"""The big O time and space complexity is O(n). To make it better I could have returned the value instead of the index
as I wasn't able to make it work."""