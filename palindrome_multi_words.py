#palindrome-word program to check whether palindrome from a list of words

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
word1=['1Mam','Sir']
fun = map(palindrome,word1)
print(list(fun))
