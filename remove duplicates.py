def remove_duplicates(l):
    b=[]
    for i in l:
        if i not in b:
            b.append(i)
    return b
print(remove_duplicates([1,2,2,3,3,4]))