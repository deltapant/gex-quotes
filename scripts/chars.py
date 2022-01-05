def calc(string):
    characters = list(string)
    ascii_values = []
    for i in range(0, len(characters)):
        ascii_values.append(str(ord(characters[i])))

    total1 = ''.join(ascii_values)
    print(total1)
    total1_list = list(total1)
    
    total2_values = []
    for i in range(0, len(total1)):
        if total1[i] == '7':
            
    

calc('ABC')
