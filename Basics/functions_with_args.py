def myfunc(*args):
    print(args)
    print(sum(args))

def myfunckeyargs(**kwargs):
    print(kwargs.keys())
    print('this is the value {}'.format(kwargs['animal']))


myfunc(10,20,30,40,50,80)
myfunckeyargs(animal='horse')