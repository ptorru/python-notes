__version__ = '0.1.0'

a = 42

# you can use variables to define defaults
# these are samples when the function is defined
def question(answer=a):
    return a

a = 34

# positional args are a tuple
# keyword args are a dict
def print_point(x, y, color="", w=0, h=0):
    print(f"position: {x},{y} - color:{color} - shape: {w},{h}")

# you can also use the params tuple and dict:
def foo(*args, **kwargs):
    if "bar" in kwargs.keys():
        return kwargs["bar"] + args[0]
    else:
        return args[0] + args[1]
