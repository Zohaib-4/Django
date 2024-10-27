import time as t

def time_it(func):
    def wrapper():
        x=t.time()
        print(x)
        func()
        y=t.time()
        print(x)
        # print(y-x)
    return wrapper

@time_it
def fact():
    fact1 = 1
    for x in range(1,200):
        fact1=fact1*x
        

fact()
