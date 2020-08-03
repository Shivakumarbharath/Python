def decorstr(func):
    def wrapper(name):
        result = func(name)
        result += '\nhow are you'
        return result

    return wrapper


@decorstr
def f1(name):
    return name


print(f1('Bharath'))
