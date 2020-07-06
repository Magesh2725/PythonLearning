#Usually the scope of referring variables follow below hierarchy
#Local
#Enclosing
#Global
#Built-in

#understand about 'global' keyword

x=100

def func_scope():
    global x
    x=700
    print('Enclosing '+f'value of X is {x}')
    def func_local():
        x=500
        print('Local scope '+f'values of X is {x}')
    func_local()
print('Global '+f'value of X is {x}')
func_scope()
print('Global '+f'value of X is {x}')

