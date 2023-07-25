import functools

users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login_required(func):
    func.called = False
  
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if username in users and users[username] == password:
                print("Авторизация успешна")
                wrapper.called = True
            else:
                print("Неверные логин или пароль")
                return
        return func(*args, **kwargs)
    return wrapper

@login_required
def function1():
    print("Добро пожаловать!")
  
function1()
