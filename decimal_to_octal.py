def decimal_to_octal(dec):
    oct = 0
    count = 1
    while(dec != 0):
        rem = dec % 8 
        oct += rem * count
        count = count * 10
        dec = dec // 8
    return(oct)
l=[1792,2357,3825,4665]
inp=map(decimal_to_octal,l)  
print(list(inp))
