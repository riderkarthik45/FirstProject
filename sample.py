from multipledispatch import dispatch

@dispatch(int)
def fun(a):
    print('Python')

@dispatch(int, int)
def fun(a, b):
    print("Java")

@dispatch(int, int, int)
def fun(a, b, c):
    print("HTML")

fun(20, 30)
