mylist=[1,2,3,4,5,6,7]
for num in mylist:
    print(num)

name='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for ltr in name:
    print (ltr)

#Tuple unpacking

mylistOftuples=[(1,2),(3,4),(5,6)]
for a,b in mylistOftuples:
    print(a)
    print(b)

my_dict={'key1':'door','key2':'window','key3':'lock'}

for m,n in my_dict.items():
    print(m+'__>'+n)
