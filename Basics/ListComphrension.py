input=''
inr=[1,100,1000]
age=[20,15,16,18,34,56]


mylist=[x for x in input]
my_GBP_list=[x*96.0 for x in inr]
my_age=['adult' if x>18 else 'teenage' for x in age]

print(mylist)
print(my_GBP_list)
print(my_age)