def has_duplicates(l):
    for i in l:
        for i in range(0,len(l)):
            for j in l:
                for j in range(i+1,len(l)):
                    if l[i]==l[j]:
                        return True
    return False
print(has_duplicates([1,2,3,4]))
