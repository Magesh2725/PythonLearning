def summer_69(arr):
    i=0
    flag=0
    for item in arr:
        if item==6:
            flag=1
        if item==9:
            flag=0
        if flag==0 and item!=9:
            i=item+i

    print(i)

def check_007(arr):
    flag=3
    zero_count=0
    for item in arr:
        if item==0 and zero_count<3:
            flag=flag-1
            zero_count+=1
        if flag==1 and item==7:
            flag=flag-1


    if flag==0:
        print(True)
    else:
        print(False)


summer_69([4,5,6,8,9])
summer_69([2,1,6,9,11])

check_007([1,2,4,0,0,7,5])
check_007([1,7,2,0,4,5,0])
check_007([1,7,4,0,7,7,8])
