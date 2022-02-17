import time

def timer(func):
    def wrapper(*args,**kw):
        t1 = time.time()
        func(*args,**kw)
        t2 = time.time()

        cost_time = t2 - t1
        print('cost time %s.'%cost_time)
    return wrapper