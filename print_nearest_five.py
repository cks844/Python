#Python program to char value + nearest_five values of the char value
# Input : 'G'
# Output : 'GHIJKL'
def print_nearest_five(string):
    asc = ord(string) # converting to ascii
    str =  ""
    for i in range(asc,asc+6):
        str = str+chr(i) #chr(i) for converting asci to char
    return str
print_nearest_five('G')
