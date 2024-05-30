'''
Write a function that determines if two given strings are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. 
Consider case sensitivity and ignore spaces.
'''
s1="listen"
s2="silent"

d1={}
d2={}

for char in s1:
    d1[char]=d1.get(char,0)+1
    
for char in s2:
    d2[char]=d2.get(char,0)+1

if d1==d2:
    print("Anagram")
else:
    print("Not")