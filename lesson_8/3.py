import sys

def swallow_output(func):
    def wrapper(*args, **kwargs):
        sys.stdout = None
        result = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return result
    return wrapper

@swallow_output
def my_function():
    print("Этот текст будет 'съеден' декоратором.")
