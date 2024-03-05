#program to find the nearest vowel of a given alphabet
def nearest_vowel():
    letter=input("Enter the letter:").lower()
    vowels=['a','e','i','o','u']
    dist_list=[]
    for vowel in vowels:
        dist_list.append(abs(ord(letter)-ord(vowel))) #finding the distance b/w each vowel and the letter using ascii(ord)
    ind=dist_list.index(min(dist_list)) #finding index of minimum distance 
    print(f"The nearest vowel of {letter} is {vowels[ind]}")
nearest_vowel()
