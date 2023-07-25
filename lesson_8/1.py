def retry(func):
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        else:
            print("Функция уже была вызвана ранее")
    wrapper.called = False
    return wrapper

@retry
def function():
    print("Привет!")
