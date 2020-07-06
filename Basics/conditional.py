x=0

while x<5:
    print(x)
    x=x+1
else:
    print('end')

for m in range(1,11):
    if(m==5):
        break
    print(m)

#range enumerate zip  in keyword min max random lib input casting
my_lis=[*range(10)]#-needs * operator to unpack
print(my_lis)

just='words'
for m,n in enumerate(just):
    print(m)

list1=[*range(10)]
list2=[*range(5)]

combine=zip(list1,list2)
for item in combine:
    print(item)

print('s' in just)

from random import shuffle
shuffle(list1)
print(list1)

from random import randint
print(randint(0,100))

name=input('sollu name')
print(int(name))
