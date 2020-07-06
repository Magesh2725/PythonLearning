#map function
def square(num):
    return num ** 2

my_array=[2,3,4,5,6,7,8]

print(list(map(square,my_array)))

#filter function
def check_name_withA(name):
    return name[0]=='A'

my_name_list=['Anish','Magesh','Anirudh','Elavarasan']

print(list(filter(check_name_withA,my_name_list)))

#lambda -> function without name - one time usage

print(list(map(lambda  name: name.upper(),my_name_list)))
