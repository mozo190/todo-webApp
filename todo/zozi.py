password = '12345678aaaA'


def strength(passw):
    if len(passw) <= 8:
        return 'Weak Password'

    if not any(car.isupper() for car in passw):
        return "Weak Password"
    if not any(car.isdigit() for car in passw):
        return "Weak Password"
    else:
        return 'Strong Password'


print(strength(password))


def foo(arg):
    avrg = sum(arg) / len(arg)
    return avrg


print(foo([1, 2, 3, 4, 5]))


def greet(name):
    return f'Hi {name}'


print(greet('Zozi'))


def strings(str1, str2):
    return str1 + " " + str2


print(strings('Zozi', 'Mwale'))


def greets(name):
    name = name.capitalize()
    return f'Hi {name}'


print(greets('zozi'))


def speed(distance, time):
    return distance / time


print(speed(5, 300))
