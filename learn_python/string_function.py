string="welcome to all"
print(string)
print(type(string))
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())
print(string.count("e"))
print(string.endswith("ll"))
print(string.find("a"))
print(string.replace("o","a"))
s="naveen123"
print("is upper : ",s.isupper())
print("is lower : ",s.islower())
print("is alpha : ",s.isalpha())
print("is alpha num : ",s.isalnum())
s1="he\nis\ngood"
print(s1)
print(s1.splitlines())
print(s1.splitlines(True))
#split the word using , , space, _, - .
s2="goodmorning to all"
print(s2.split(" "))
s2="goodmorning to all, friends"
print(s2.split(","))
s3= " welcome "

#remove whitespace  using strip
print(len(s3))
print(len(s3.strip()))
