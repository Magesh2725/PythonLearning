mylist=[1,2,3,4]
mylist.insert(2,100)
print(mylist)

def pig_latin(word):
    first=word[0]
    if first in 'aeiou':
        return word+'ay'
    else:
        return word[1:]+first+'ay'


print(pig_latin('word'))
print(pig_latin('yakkai'))
