a=5
def func():
    b=4 # local variable only works inside func()
    global a
    print(a)
func()