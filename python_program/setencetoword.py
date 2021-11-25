'''def sentence(s):
    word=""
    for i in range(0,len(s)):
        if ((s[i]==' ') or (s[i]==',')):
            print(word)
            word=""
        else:
            word+=s[i]
    print(word)     
s=input("Enter the sentence:")
sentence(s)'''
def sentence(s):
    word=""
    for i in range(0,len(s)):
        if s[i].isalpha():
            word+=s[i]
        elif not(s[i].isalpha()):
            print(word)
            word=""
    print(word)
s=input("Enter the string:")
sentence(s)

