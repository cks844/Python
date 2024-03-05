#palindrome-word program that checks spaces,integers and lowercase 
def palindrome(word1):
    word1=word1.lower()
    word1=word1.replace(' ','')
    word2=''
    word3=''
    for i in word1:
       if i.isdigit():
           continue
       else:
           word3 += i
    for i in word3:
        word2 = i+word2 
    if word3 == word2:
        print('Palindrome')
    else:
        print('Not')
word1='1 Mam'
palindrome(word1)

#without using is.digit()

def palindrome(word1):
    word1=word1.lower()
    word1=word1.replace(' ','')
    word2=''
    word3=''
    check='1234567890'
    for i in word1:
       if i not in check:
           word3 += i
    for i in word3:
        word2 = i+word2 
    if word3 == word2:
        print('Palindrome')
    else:
        print('Not')
word1='1M2am'
palindrome(word1)
