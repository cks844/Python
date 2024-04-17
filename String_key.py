#Input : 'AbC' (key = 2)
#Output : 'dEf'

def add(inp,key):
    inp = inp
    new_str = ""
    for i in inp:
        if i.islower():
            i = i.upper()
            new_str += chr(ord(i)+2)
        elif i.upper():
            i = i.lower()
            new_str += chr(ord(i)+2)
    return new_str
