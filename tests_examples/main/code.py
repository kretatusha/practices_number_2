
def square_it(income):
    if not isinstance(income, int):
        raise TypeError("say something")
    return income**2

def square_three():
    return square_it(3)
