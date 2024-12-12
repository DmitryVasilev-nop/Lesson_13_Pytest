def hello_who(name):
    return f"Hello, {name}"

def salary(hours, salary_by_hours):
    k = 2
    return hours * salary_by_hours * k

def beta(number):
    if number % 2 == 0:
        return 'четное'
    else:
        return 'не четное'