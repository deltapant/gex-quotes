def double_every_other(lst):
    for i in range(1, len(lst), 2):
        lst[i] = lst[i]* 2
    return lst
        
    

print(double_every_other([1,2,3,4]))
    

        