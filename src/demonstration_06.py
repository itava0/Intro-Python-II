"""
Challenge #6:
Return the number (count) of vowels in the given string.
We will consider `a, e, i, o, u as vowels for this challenge (but not y).
The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    vowels = 'aeiou'
    result = [each_vowel for each_vowel in input_str if each_vowel in vowels]
    print(len(result))

input_str = input()

get_count(input_str)