from contracts import contract

@contract(x='float', returns='float,>=0')
def foo(x):
    pass

foo(-1)



