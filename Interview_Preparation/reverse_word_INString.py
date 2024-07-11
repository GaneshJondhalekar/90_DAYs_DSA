'''
Write a function to reverse the order of words in a given string. Words are separated by spaces.

Input: s = "Hello world this is a test"
Output: "test a is this world Hello"

'''

s = "Hello world this is a test"

l=s.split(" ")

r=" ".join(i for i in l[::-1])
print(r)

