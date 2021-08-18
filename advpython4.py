x =10
y=20

print(globals())

def func():
    string = 'hello'
    print(locals())
    print(string)

#namespace and scope

#global namespace
#local namespace
#built in namespace
#enclosing function namespace

#LEGB rule


#L - local
#E - enclosing func nameapsce
#G - Global namespace
#B - built in namespace


string = 'hello'
def func1():
    def func2():
        print(string)




