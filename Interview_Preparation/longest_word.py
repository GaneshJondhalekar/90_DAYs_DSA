#Write a function to find the longest word in a given string.

s = "The quick brown fox jumps over the lazy dog"
# Output: "jumps"
s=s.split(" ")
lon=s[0]
for i in s[1:]:
    if len(i)>=len(lon):
        lon=i
        
print(lon)
            
    
