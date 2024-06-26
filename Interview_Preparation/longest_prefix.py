'''
Write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string.
'''

def longest_prefix():
    strs = ["flower", "flow", "flight"]
    prefix=strs[0]
    
    
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix=prefix[:-1]#iterate fron 0 to -1 so it will skip last character each time
            if prefix=="":
                return None
    return prefix
    
print(longest_prefix())