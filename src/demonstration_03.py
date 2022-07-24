"""
Challenge #3:
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20
Notes:
- Bonus: Try to complete this challenge in one line!
"""


# def multiply_nums(nums):
#   mylist = [int(x) for x in nums.split(',')]
#   result = 1
#   for x in mylist:
#     result = result * x
#   return result

from functools import reduce 

# multiply all values in the
# list using lambda function and reduce()
def multiply_nums(nums):
  return reduce((lambda x, y: x * y), [int(x) for x in nums.split(',')])

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))