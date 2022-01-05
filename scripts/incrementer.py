def hamming_distance(a, b):
    sum = 0
    for i in range(0, len(a)):
        if int(a[i]) == int(b[i]):
            continue
        elif int(a[i]) != int(b[i]):
            sum += 1
    return sum
        
        
        
print(hamming_distance("1010","0101"))