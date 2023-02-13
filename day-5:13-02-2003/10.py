def reverse_words(s):
    
    return ' '.join(s.split()[::-1])

s=input("enter the string")

print(reverse_words(s))
