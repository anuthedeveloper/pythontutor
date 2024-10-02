import time

def timed_executions(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to complete executions")
        return value
    return wrapper

@timed_executions
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result    


myfunction(300000)